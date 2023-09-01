import time
from selenium import webdriver
# 如果要操作Windows元素，则使用库uiautomation, 如果要处理移动端，appium

# 第一步：先实例化webdriver对象，用于初始化浏览器操作
# 默认情况下，建议将chromedriver.exe等放在PATH环境变量的某个目录中，否则需要在参数executable_path中指定
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path="C:/Tools/chromedriver.exe")
# driver = webdriver.Firefox()
driver.maximize_window()
# 访问目标网站的页面地址
driver.get('http://192.168.112.188:8080/woniusales/')
time.sleep(2)
print(driver.title)
print(driver.page_source)
# driver.refresh()
# driver.back()
# driver.forward()
# driver.get_cookies()

# 第二步：利用DOM的识别机制，去识别和操作界面元素
driver.find_element_by_id('username').send_keys('admin')
time.sleep(1)
driver.find_element_by_id('password').send_keys('admin123')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='verifycode']").send_keys('0000')
time.sleep(1)
# driver.find_element_by_xpath("/html/body/div[4]/div/form/div[6]/button").click()
driver.find_element_by_css_selector("body > div.container > div > form > div:nth-child(6) > button").click()
time.sleep(3)

try:
    driver.find_element_by_id('barcode').send_keys('1234567890')
    print("登录成功")
except:
    print("登录失败")

if '请扫描商品条码' in driver.page_source:
    print("登录成功")
else:
    print("登录失败")

driver.close()




# UIAutomation识别Windows元素
import uiautomation

time.sleep(2)
calc = uiautomation.WindowControl(Name='计算器')
calc.ButtonControl(AutomationId='num1Button').Click()
calc.ButtonControl(AutomationId='plusButton').Click()
calc.ButtonControl(Name='五').Click()
calc.ButtonControl(AutomationId='equalButton').Click()

