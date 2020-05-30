# .ChooseLockPattern

from appium import webdriver
import time

##########################这里为功能示范代码，并没有按照面向对象思想，需要可自行修改和封装#################
##########################初始化#################

# desired_caps = dict()
# 设备的系统
# desired_caps["platformName"] = "Android"
# 系统的版本
# desired_caps["platformVersion"] = "5.1.1"
# 设备的名称（都需要有，安卓可以随意填写，但是iOS 只能是iphone 6s）
# desired_caps["deviceName"] = "127.0.0.1:62001"
# 要打开的应用程序
# desired_caps["appPackage"] = "com.android.settings"
# 要打开的页面名
# desired_caps["appActivity"] = ".settings"
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    #设备系统
    'platformName': 'Android',
    #设备名称
    'deviceName': '127.0.0.1:62001',
    #安卓版本
    'platformVersion': '5.1.1',
    # apk包名
    'appPackage': 'com.ss.android.ugc.aweme',
    # apk的launcherActivity
    'appActivity': '.splash.SplashActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
    'resetKeyboard':True,# 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来

}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)


##########################模拟移动###################
"""
Move the pointer from the previous point to the element or point specified
从一个点移动到另一个点（或元素）
Args:
    el: 要移动到的元素（element）
    x: 要移动到的位置的x坐标，x存在，则y必须存在
    y: 要移动到的位置的y坐标，y存在，则x必须存在
"""
# TouchAction(driver).press(x=146,y=523).move_to(x=449,y=523).move_to(x=750,y=523).move_to(x=447,y=822).move_to(x=150,y=1125).move_to(x=445,y=1125).move_to(x=750,y=1125).release().perform()

##########################获取屏幕尺寸#################
print(driver.get_window_size())

##########################保存截图操作#################
driver.get_screenshot_as_file("C:/Users/Administrator/Desktop/screenshot.png")

##########################获取网络状态#################
print(driver.network_connection)

#########################设置网络状态#################
import appium.webdriver.connectiontype
"""
Args:
    connection_type: int 类型 appium.webdriver.ConnectionType 的枚举类型

class ConnectionType:
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6

"""
# 例如设置当前网络类型为NO_CONNECTION
result = driver.set_network_connection(0)
print(result)


#########################判断网络状态#################
print(driver.network_connection)
from appium.webdriver.connectiontype import ConnectionType
if driver.network_connection == ConnectionType.WIFI_ONLY:
    print("WIFI_ONLY,只开启了WIFI")
elif driver.network_connection == ConnectionType.NO_CONNECTION:
    print("没有网络")
elif driver.network_connection == ConnectionType.NO_CONNECTION:
    print("飞行模式")
elif driver.network_connection == ConnectionType.DATA_ONLY:
    print("使用流量")
else:
    print("流量和WIFI均已开启")



###########################发送键操作#####################
"""
Args:
    keycode: the keycode to be sent to the device
    metastate: meta information about the keycode being sent
"""
# driver.press_keycode(24)
# driver.press_keycode(24)
# driver.press_keycode(24)
# driver.press_keycode(4)


##################################通知栏操作#################
driver.open_notifications()
time.sleep(2)
driver.press_keycode(4)
time.sleep(1)


####################################退出关闭当前会话#############
driver.quit()