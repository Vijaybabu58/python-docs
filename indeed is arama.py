from selenium import webdriver
#selenium uzerinden eristigimiz herhangi bir siteden klavyeyle islem yapmak istiyossak ayri bi modul cekmeliyiz
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_experimental_option("excludeSwitches",["enable-logging"])


driver=webdriver.Chrome(executable_path=r"C:/Users/yesim/OneDrive/Masaüstü/chromedriver.exe",chrome_options=options)
url="https://tr.indeed.com/?r=us"
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)

isarama=driver.find_element_by_css_selector("#text-input-what")
isarama1=driver.find_element_by_css_selector("#text-input-where")
isarama.send_keys("intern")
isarama1.send_keys("Stockholm")
isarama1.send_keys(Keys.ENTER)
isarama2=driver.find_element_by_css_selector("#resultsCol > div.no_results > div > p > a")
isarama2.click()