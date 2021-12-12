from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_driver = webdriver.Chrome(
    executable_path="C:/Ariel/Course/DevOps/11_14_2021/DevOps1411/05_12_2021/chromedriver.exe")
# firefox_driver = webdriver.Firefox(
#     executable_path="C:/Ariel/Course/DevOps/11_14_2021/DevOps1411/05_12_2021/geckodriver.exe")
# chrome_driver.get("http://www.google.co.il")
# firefox_driver.get("http://www.google.co.il")

# website_title = chrome_driver.title
# chrome_driver.refresh()
# if website_title == chrome_driver.title:
#     print("equal")


# test1 = chrome_driver.find_element_by_id("hplogo")
# test2 = firefox_driver.find_element_by_id("hplogo")

# print(test1)
# print(test2)


# chrome_driver.get("https://translate.google.com/")
# chrome_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("אריאל איטח")
# chrome_driver.find_element_by_class_name('er8xn').send_keys("אריאל איטח")
# chrome_driver.find_element_by_tag_name('textarea').send_keys("אריאל איטח")

# chrome_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
# chrome_driver.find_element_by_class_name('er8xn')
# chrome_driver.find_element_by_tag_name('textarea')

chrome_driver.get("https://www.youtube.com/")
chrome_driver.find_element_by_xpath('//input[@id="search"]').send_keys("good music")
chrome_driver.find_element_by_id("search-icon-legacy").click()




# chrome_driver.get("https://www.facebook.com/")
# chrome_driver.find_element_by_id("email").send_keys("ariel_itach.com")
# chrome_driver.find_element_by_id("pass").send_keys("P@ssw0rd")
# chrome_driver.find_element_by_tag_name('button').click()


# chrome_driver.get("https://www.facebook.com/")
# print(f"before delete: {chrome_driver.get_cookies()}")
#
# chrome_driver.delete_all_cookies()
# print(f"after delete: {chrome_driver.get_cookies()}")


# chrome_driver.get("https://www.github.com/")
# chrome_driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]').send_keys("Selenium")
# chrome_driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]').send_keys(u'\ue007')


# executable_path="C:/Ariel/Course/DevOps/11_14_2021/DevOps1411/05_12_2021/chromedriver.exe"
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
# chrome_driver.get("https://www.github.com/")
