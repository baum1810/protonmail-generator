from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests, random
from time import sleep
import undetected_chromedriver as uc
from os import system
option = uc.ChromeOptions()
#PROXY = "154.83.29.201:999" #delete the # to enable proxies u also need to put a http proxie inside
#option.add_argument('--proxy-server=%s' % PROXY) #delete the # to enable proxies 
def cls():
    system("cls")

option.add_argument('--disable-notifications')
option.add_extension("Noptcha--ReCAPTCHA---hCAPTCHA-Solver.crx")
option.add_extension("I-don-t-care-about-cookies.crx")
option.add_argument('--lang=en')
option.headless = False
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--disable-gpu')
#option.add_argument('--incognito')
option.add_argument('--mute-audio')
option.add_argument('--ignore-certificate-errors')
option.add_argument('--disable-web-security')
option.add_argument('--disable-logging')
#driver = webdriver.Chrome("chromedriver.exe", options=option)

def main():
    driver = uc.Chrome(options=option)
    driver.get("https://account.proton.me/signup?plan=free&billing=24&currency=EUR&language=en")
    cls()
    r = requests.get("https://randomuser.me/api/").text
    sad, asd = r.split(',"username":"')
    name, asdf = asd.split('","password":"')
    password, asdsa = asdf.split('","salt":"')
    driver.switch_to.frame(0)
    driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(f'{name}.baum')
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, value='//*[@id="password"]').send_keys(password+password)
    driver.find_element(By.XPATH, value='//*[@id="repeat-password"]').send_keys(password+password)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button').click()
    sleep(3)
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    if not "CAPTCHA" in source_code:
        cls()
        print("captcha not found please complete verification")
        input("press enter when done")

 
    print("Waiting 20 seconds please be paitent")
    sleep(20)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div/div/main/div[2]/form/button').click()
    sleep(5)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div/div/main/div[2]/form/button[2]').click()
    sleep(1)
    driver.find_element(By.XPATH, value='/html/body/div[4]/dialog/div/div[3]/button[1]').click()
    sleep(3)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[3]/div/div/main/div[2]/ul/li[1]/button').click()
    f = open("accs.txt" , "a")
    f.write(f"{name}.baum@proton.me:{password}{password}\n")
    f.close()
    driver.quit()
    print(f"Account \nemail: {name}.baum@proton.me generated")
    main()

main()
