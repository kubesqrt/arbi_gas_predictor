from selenium import webdriver
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from queue import Queue

def price_estimator():
    while True:
        chromeOptions = Options()
        chromeOptions.add_argument("--kiosk")   
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.get("https://arbiscan.io/blocks")
        x = {INSERT SECONDS}
        try:
    
            element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div[2]/table/tbody/tr[1]/td[1]/a"))
    ).click()
            element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div/div[3]/div/div[2]/a"))
    ).click()
            element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div[3]/table/tbody/tr/td[2]/span/a"))
    ).click()
            element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[4]/div/div[2]/div[1]/div/span/a/span"))
    ).click()
            gas = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='ContentPlaceHolder1_spanActualGasPrice']"))
    )
            time.sleep(2)
            gas_ = gas.text
            gas_ = re.findall("\d+", str(gas_))
            gas_ = float(gas_[1])/1000000000
            print(gas_)
            #out_q.put(gas_)
        finally:
            driver.quit()
            time.sleep(x)
