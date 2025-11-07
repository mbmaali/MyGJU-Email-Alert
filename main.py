import requests
from bs4 import BeautifulSoup
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time



mygju_username =  "REDACTED"
mygju_password = "REDACTED"

mygju_url = "https://mygju.gju.edu.jo/faces/index.xhtml"
mygju_login_url = "https://mygju.gju.edu.jo/faces/index.xhtml"
mygju_schedule_url = "https://mygju.gju.edu.jo/faces/schedules/student_schedule.xhtml"

username_field_xpath = """//*[@id="j_idt15:login_username"]"""
password_field_xpath = """//*[@id="j_idt15:login_password"]""" 
login_as_student_button_xpath = """/html/body/div[1]/div[2]/form/center/fieldset/div/button[1]/span"""




chromedriver_path = "chromedriver.exe"  






def check_website_status():
    try:
        response = requests.get(mygju_url, timeout=5)
        if response.status_code == 200:
            print("Website is working")
            return 200
        
        else:
            return f"Website returned error {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Website is not working ({e})"

def start_driver_and_login():
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(mygju_login_url)
    time.sleep(5)
    login_as_student_button = driver.find_element(By.XPATH, login_as_student_button_xpath)
    username_field = driver.find_element(By.XPATH, username_field_xpath)  
    password_field = driver.find_element(By.XPATH, password_field_xpath)  
    username_field.send_keys(mygju_username)
    password_field.send_keys(mygju_password)
    time.sleep(1)
    login_as_student_button.click()
    time.sleep(1)
    driver.get(mygju_schedule_url)

  



    

def main():
    if check_website_status() == 200:
        start_driver_and_login()

    else:
        print("error")


if __name__ == "__main__":
    main()