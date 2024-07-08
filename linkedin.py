from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import expected_conditions as EC



class WebDriverManager:
    def __init__(self):
        self.driver = None
        # self.initialize_driver()

    def initialize_driver(self):
        if not self.driver:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--disable-infobars')
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
            # Set window size to half the screen size
            screen_width = self.driver.execute_script("return window.screen.width;")
            screen_height = self.driver.execute_script("return window.screen.height;")
            self.driver.set_window_size(screen_width // 2, screen_height)
            # Optionally, you can set the window position if needed
            self.driver.set_window_position(0, 0) 
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()




from selenium.webdriver.support.ui import WebDriverWait

class TakeScreenshot(WebDriverManager):
    def __init__(self):
        super().__init__()
        self.initialize_driver()
        self.url = 'https://np.linkedin.com/jobs/view/mid-level-java-developer-at-code-himalaya-3969037879?trk=public_jobs_topcard-title'

    
    def fetch_data(self):
        try:
            self.driver.get(self.url)
            target_div = self.driver.find_element(By.CLASS_NAME, "core-rail")
            top_card = target_div.find_element(By.CLASS_NAME, 'top-card-layout__entity-info-container ')
            position = top_card.find_element(By.TAG_NAME, 'h1')
            company_link = target_div.find_element(By.CSS_SELECTOR, 'a.topcard__org-name-link.topcard__flavor--black-link')
            company_name = company_link.text
            # Retrieve the href attribute of the anchor element
            company_url = company_link.get_attribute('href')
            show_more = target_div.find_element(By.CLASS_NAME, 'decorated-job-posting__details')
            show_more_button = target_div.find_element(By.CSS_SELECTOR, 'button.show-more-less-html__button.show-more-less-button.show-more-less-html__button--more')
            show_more_button.click()

            about_job = about_job = target_div.find_element(By.CSS_SELECTOR, 'div.show-more-less-html__markup.relative.overflow-hidden')

            print(position.text)
            print(company_name)
            print(about_job.text)
            time.sleep(10)
        except Exception as e:
            print(e)



TakeScreenshot().fetch_data()