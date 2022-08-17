from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
import random
import time

'''
Username: bobbybackupy
Password: Argyleawesome123!
Secret answer: Hemingway
Portal link: https://www.upwork.com/ab/account-security/login

# This user uses OTP for MFA. 
Authenticator secret key: J6PM J5GN XMGV U47A
'''

username = "bobbybackupy"
password = "Argyleawesome123!"

CHROME_PATH = './chromedriver'
ua = UserAgent()
user_agent = ua.load()
# options = webdriver.FirefoxOptions()
# profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-popup-blocking")
options.add_argument("disable-infobars")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--no-sandbox")
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("user_agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0")
# options.add_argument('--disable-extensions')
# # options.add_argument('--profile-directory=Default')
# # options.add_argument("--incognito")
# # options.add_argument("--disable-plugins-discovery")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-blink-features=AutomationControlled')
# prefs = {"profile.default_content_setting_values.notifications": 2}
# options.add_experimental_option("prefs", prefs)

url = "https://www.upwork.com/ab/account-security/login"

my_driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
my_driver.execute_script("navigator.webdriver=false")
my_driver.maximize_window()
wait = WebDriverWait(my_driver, 20)
time.sleep(4)
my_driver.get(url)
time.sleep(random.randint(1,4))
wait.until(cond.element_to_be_clickable((By.ID, 'login_username')))
my_driver.find_element((By.ID),'login_username').click()
time.sleep(random.randint(1,4))
for key in username:
    my_driver.find_element((By.ID),'login_username').send_keys(key)
    time.sleep(0.2)
time.sleep(random.randint(1,4))
my_driver.find_element((By.ID),'login_password_continue').click()
wait.until(cond.element_to_be_clickable((By.ID, 'login_password')))
time.sleep(random.randint(1,4))
my_driver.find_element((By.ID),'login_password').send_keys(password)
time.sleep(random.randint(1,4))
my_driver.find_element((By.ID),'login_control_continue').click()
import code
code.interact(local=locals())
wait.until(cond.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/aside/div/div[1]/div[1]/section/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/button')))
my_driver.find_element((By.XPATH), '//*[@id="main"]/div/div/aside/div/div[1]/div[1]/section/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div[3]/div/button').click()
wait.until(cond.visibility_of_all_elements_located((By.CLASS_NAME, "up-card-section")))
print("Hallo wie gehts?")
time.sleep(5)
