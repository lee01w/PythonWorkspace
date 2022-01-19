import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

# 가는 날 클릭
browser.find_element(By.XPATH, "//button[contains(text(),'가는 날')]").click()

# 이번달 17일, 다음달 17일 선택
time.sleep(1)
browser.find_elements(By.XPATH, "//b[contains(text(),'17')]")[0].click()
browser.find_elements(By.XPATH, "//b[contains(text(),'17')]")[1].click()

browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[7]/div/ul/li[1]/button").click()

time.sleep(1)
browser.find_elements(By.XPATH, "//a[contains(@class,'recommend_anchor__1qmYP')]")[0].click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]")))
    print(elem.text)
finally:
    browser.quit()