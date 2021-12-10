from selenium import webdriver
from time import sleep


my_driver = webdriver.Chrome(executable_path="C:/Ariel/Course/DevOps/11_14_2021/DevOps1411/05_12_2021/chromedriver.exe")
# my_driver.get("https://github.com")
# sleep(3)
# my_driver.close()
my_driver.get("C:/Ariel/Course/DevOps/11_14_2021/DevOps1411/05_12_2021/tip_calc/index.html")
# my_driver.back()
# my_driver.refresh()
billamt = my_driver.find_element_by_id("billamt")
billamt.send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element_by_id("peopleamt").send_keys("4")
my_driver.find_element_by_id("musicScore").send_keys("2")
my_driver.find_element_by_id("calculate").click()
actual = my_driver.find_element_by_id("tip").text
expected = "5.75"
my_driver.close()

# if actual == expected:
#     print("test finished successfully - tip is ok")
# else:
#     print("test failed - tip is not ok")

assert expected == actual


