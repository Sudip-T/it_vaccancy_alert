import os
import ctypes
from selenium import webdriver
from .models import JobListing
from django.conf import settings
from selenium.webdriver.common.by import By
from django.shortcuts import get_object_or_404
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            # options.add_argument('--headless')
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
    def __init__(self, img_dir = 'vaccancy'):
        super().__init__()
        self.initialize_driver()
        self.url = 'http://localhost:8000/job/'
        self.img_dir = img_dir
    
    def take_screenshot(self,job_id):
        self.driver.get(f'{self.url}{job_id}/')
        container = self.driver.find_element(By.CLASS_NAME, 'content')
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



class PostOnFacebook(WebDriverManager):
    def __init__(self, job_id):
        super().__init__()
        self.job_id = job_id


    def get_job_data(self):
        job = get_object_or_404(JobListing, id=self.job_id)
        company = job.company
        additional_info = job.add_info.all()
        return job, company, additional_info
    
    def run(self):
        job, company, extra_data = self.get_job_data()
        self.make_post()
        return self.format_post()

    def format_post(self):
        a = 0
        post = f"\n{'company.name'} is #hiring {'job.position'}\n\n"
        post += '🚀Position : Mid-Level Java Developer\n'
        if a==0:
            post += 'Employment Type: {job.Employement_type}\n'
        if a==0:
            post += 'Location: {company.address}\n'
        if a==0:
            post += 'Experience: {job.experience}\n\n'

        if a==0:
            post += 'Apply Here : {job.link}\n\n'


        if a==0:
            post += '#vaccancy #itjobs\n'

        

        # print(post.encode('utf-8').decode('utf-8'))
        return post

            
    #         🔑 Roles Available:
    #         """
    #         for info in additional_info:
    #             post += f"{info.header}: {info.content}\n"

    #         post += f"""
    #         💼 Key Responsibilities:

            
    #         🔗 Apply Now!
    #         {job.application_link if job.application_link else 'https://www.linkedin.com/jobs/search/'}
    #         """
    #         return post

    def load_cookie(self):
        try:
            with open('image_gen/cookies_976-2453564.pkl', 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
        except Exception as e:
            print(f"Error loading cookies: {e}")
            time.sleep(5)

    def make_post(self):
        self.initialize_driver()
        self.driver.get('https://www.facebook.com/')
        self.load_cookie()
        self.driver.refresh()
        time.sleep(1)
        self.make_posts()
        # job, company, add_info = self.get_job_data()
        # post_format = self.format_post(job, company, add_info)

        # return post_format
    def make_posts(self) -> None:
        try:
            s = time.time()
            create_post_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Photo/video')]"))
            )
            create_post_button.click()
            time.sleep(1)

            active_post_area = self.driver.switch_to.active_element
            bmp_caption = ''.join(char for char in self.format_post() if ord(char) <= 0xFFFF)
            active_post_area.send_keys(bmp_caption)

            post_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']"))
            )
            # post_button.click()

            time.sleep(100)
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located((By.XPATH, "//span[text()='Post']"))
            )
            # self.success_count += 1
            print(f"{'-'*30} Post submitted successfully {'-'*30}")
            # logging.info(f"Post submitted successfully (Success Count: {self.success_count})")
            print(f"{'-'*30} Time Taken : {time.time()-s} {'-'*30}")
            time.sleep(100)
        except Exception as e:
            print(e)