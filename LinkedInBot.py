from selenium import webdriver
from selenium.webdriver.common.by import By
import tabula as tb
import pandas as pd
import time
from selenium.webdriver import Keys
import CONSTANTS

# For Loading All the recruters linkedin profile url for sending msgs
def read_pdf_file():
    df = pd.read_csv("List-of-Top-Pakistani-Recruiters - List-of-Top-Pakistani-Recruiters.csv")
    return df

dataframe = read_pdf_file()

# This is for testing purpose
url_list = [
    "https://www.linkedin.com/in/zamama-zaman-682091154/",
    "https://www.linkedin.com/in/mubashar-azad/"
]

driver = webdriver.Chrome("chromedrive2r.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get("https://www.linkedin.com/home")
driver.implicitly_wait(0.5)
driver.find_element(By.XPATH, "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']").click()
username = driver.find_element(By.XPATH, "//input[@id='username']")
username.send_keys(CONSTANTS.EMAIL)
driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys(CONSTANTS.PASSWORD)
driver.find_element(By.XPATH, "//button[@aria-label = 'Sign in']").click()

msg = f'''
    Dear Sir,
            I am looking for a Python Developer role as` a software engineer with deep knowledge in software design, development, and testing. Seeking to utilise broad educational background with excellent analytical technical, and programming skills to thrive as a software engineer. 
Regards:
Muhammad Usman
Software Engineer
Note This message is being sent to you by python code created by Muhammad Usman
'''

# to send your resume to all the recruters on linkedin just uncomment the forloop
for i in dataframe.URL:
    driver.get(i)
    driver.find_element(By.XPATH, "(//a[contains(@class, 'message-anywhere-button pvs-profile-actions__action artdeco-button')])[2]").click()

    driver.find_element(By.XPATH, "//div[@class='msg-form__msg-content-container--scrollable scrollable relative']").click()
    message = driver.find_element(By.XPATH, "//div[@role='textbox']/p")
    message.send_keys(msg)
    # Place ths complete path to the folder where your resume is located mine is
    driver.find_element(By.XPATH, "(//input[@type='file'])[1]").send_keys("C://Users/usman/VsCode Projects/BotRemote/MuhammadUsman.pdf")
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@data-control-name='overlay.close_conversation_window']").click()


# driver.close()