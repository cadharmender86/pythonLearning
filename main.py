# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


driver=webdriver.Chrome(ChromeDriverManager().install())
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("https://connectcloud.appypie.com")
loginId=driver.find_element_by_xpath("//input[@id='email']")
# loginId.click()
loginId.send_keys("kumardharmendra@appypiellp.com")
password=driver.find_element_by_xpath("//input[@id='password']")
login=driver.find_element_by_xpath("//button[contains(text(),'Login')]")
password.send_keys("Dharmendra@101121")
# wait.until(expected_conditions.visibility_of(login))
driver.execute_script("arguments[0].click();", login)
# login.click()

