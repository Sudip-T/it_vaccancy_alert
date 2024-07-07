import os
import time
import ctypes
import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .models import JobListing
from django.shortcuts import get_object_or_404
from django.conf import settings


class WebDriverManager:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        if not self.driver:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--disable-infobars')
            options.add_argument('--headless')
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            # self.driver.maximize_window()
            self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': '''
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    });
                '''
            })
            # Set the window to full screen
            user32 = ctypes.windll.user32
            screen_width = user32.GetSystemMetrics(0)
            screen_height = user32.GetSystemMetrics(1)
            self.driver.set_window_position(0, 0)
            self.driver.set_window_size(screen_width, screen_height)

        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()


class TakeScreenshot(WebDriverManager):
    def __init__(self, img_dir = 'screenshots'):
        super().__init__()
        self.initialize_driver()
        self.url = 'http://localhost:8000/job/'
        self.img_dir = img_dir
    
    def take_screenshot(self,job_id):
        self.driver.get(f'{self.url}{job_id}/')
        container = self.driver.find_element(By.CLASS_NAME, 'container')
        position = self.driver.find_element(By.CLASS_NAME, 'position-title').text
        position = position.lower().replace(' ','_')

        # time_now = datetime.datetime.now()
        # date_str = time_now.strftime("%Y%m%d%H%M%S")

        # current_dir = Path(__file__).resolve().parent
        media_root = settings.MEDIA_ROOT
        img_dir = os.path.join(media_root, self.img_dir)
        os.makedirs(img_dir, exist_ok=True)

        file_name = f'{job_id}_{position}.png'
        full_file_path = os.path.join(img_dir, file_name)
        
        container.screenshot(full_file_path)
        self.update_vacancy_image(job_id, os.path.join(self.img_dir, file_name))
        return f"Screenshot saved to : {full_file_path}"

    def update_vacancy_image(self, id, img) -> None:
            job_listing = get_object_or_404(JobListing, id=id)
            job_listing.vac_img = img
            job_listing.save()

