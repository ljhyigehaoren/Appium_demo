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
    'appPackage': 'com.android.settings',
    # apk的launcherActivity
    'appActivity': '.Settings',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
     'resetKeyboard':True,# 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来

}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

time.sleep(3)

######################## 启动短信的应用程序（跳转其他应用）########################
# app_package:要跳转的应用程序名
# app_activity:要跳转的页面名
# driver.start_activity("com.android.contacts",".activities.PeopleActivity")
#
######################### 获取当前的程序的包名和界面名 ########################
# page_name = driver.current_package
# activity_name = driver.current_activity
# print(page_name,activity_name)

#########################退出当前App回到主界面（com.vphone.launcher）########################
# driver.close_app()
# print(driver.current_package)

#########################判断抖音App是否已经安装，安装则卸载，未安装则安装########################
# com.ss.android.ugc.aweme
# isinstall = driver.is_app_installed("com.ss.android.ugc.aweme")
# if (isinstall):
#     print("程序已安装，卸载程序")
#     driver.remove_app("com.ss.android.ugc.aweme")
# else:
#     print("程序未安装，安装程序")
#     driver.install_app(
#         "C:/Users/Administrator/Desktop/Downloads/aweme_aweGW_v11.2.0_97887f5.apk"
#         )

#########################该方法往往用来测试程序的热启动，进入后台后，等待一段时间，自动回到前台########################
#seconds：单位秒
# driver.background_app(10)

# 进入抖音首页
driver.start_activity("com.ss.android.ugc.aweme",".splash.SplashActivity")

#########################by_id获取抖音页面搜索按钮，并点击########################
# driver.find_element_by_id("com.ss.android.ugc.aweme:id/c3k").click()

########################## 显示等待 #########################
# 在5秒内，每一秒钟找一次id为："com.ss.android.ugc.aweme:id/c3k" 得元素
# button = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/c3k"))
# button.click()

########################## 隐式等待 #########################
driver.implicitly_wait(3)

########################### 获取输入框元素，并输入内容 ##########################
# driver.find_element_by_class_name("android.widget.EditText").send_keys("本田190")

########################### 获取页面某id相同的元素，并获取文本内容 ##########################
# results = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/glh")
# for element in results:
#     print(element.text)
#     print(element.a)
#
########################### 获取取消按钮，并返回 ##########################
# # driver.find_element_by_link_text("取消").click()
# driver.find_element_by_id("com.ss.android.ugc.aweme:id/gis").click()



############################ swpe 滑动屏幕 ###########################
# 设置滑动初始坐标和滑动距离
start_x = 300
start_y = 1400
distance = 1200
"""
Args:
    start_x:(起始位置x坐标) x-coordinate at which to start
    start_y:(起始位置Y坐标)  y-coordinate at which to start
    end_x:(结束位置x坐标) x-coordinate at which to stop
    end_y:(结束位置y坐标) y-coordinate at which to stop
    duration: （滑动持续的时间，单位毫秒）time to take the swipe, in ms.

Usage:
    driver.swipe(100, 100, 100, 400)
"""
driver.tap([(500, 1200)], 500)  #appium中模拟手指点击方法，叫tap，有两个参数，元素位置和点击持续时间ms
for num in range(1,20):
    print("第几次滑动",num)
    driver.swipe(start_x,start_y,start_x,start_y-distance,800) #注意：当start_y 小于 end_y 表示向上拉
    time.sleep(2)

end_element = driver.find_element_by_id("android.widget.ImageView")
start_element = driver.find_element_by_class_name("android.widget.LinearLayout")


########################### scroll滚动   ##########################
"""
Args:
    origin_el: 滑动的起始元素
    destination_el: 滑动的结束元素
    duration: 持续时间单位秒.
Usage:
    driver.scroll(el1, el2)
"""
# driver.scroll(start_element,end_element)


########################## drag_and_drop 拖拽 ##########################
"""
Args:
    origin_el: 起始元素
    destination_el: 目标元素
"""
# driver.drag_and_drop(origin_el,origin_el)


########################## 轻敲 ##########################
"""
element: 要轻敲的元素
x : 相对于元素的左上角，x坐标点击
y : y坐标。如果使用y，也必须设置x。
"""
# # 根据元素完成轻敲
# tap_element = driver.find_element_by_id("com.ss.android.ugc.aweme:id/emz")
# TouchAction(driver).tap(element=tap_element).perform()
# time.sleep(1)
# # 根据坐标完成轻敲
# TouchAction(driver).tap(x=70,y=100).perform()
# time.sleep(2)


########################## 按下 ##########################
press_element = driver.find_element_by_id("com.ss.android.ugc.aweme:id/emz")
# 按下或者抬起
"""
el: the element to press
x: x coordiate to press. If y is used, x must also be set
y: y coordiate to press. If x is used, y must also be set
pressure: 仅仅iOS端使用
"""
# #根据元素长按
# TouchAction(driver).press(el=press_element).perform()
# #根据坐标长按
# TouchAction(driver).press(x=70,y=100).perform()


########################## press按下 release抬起 ##########################
"""
el: the element to press(要按的元素对象)
x: x坐标，x存在，则y必须存在
y: y坐标，y存在，则x必须存在
duration: 长按持续时间(毫秒)
"""
#根据元素长按，并抬起
# TouchAction(driver).press(el=press_element).release().perform()

########################## long_press 长按 release抬起 ##########################
#根据元素长按持续时间为1秒，并抬起
# TouchAction(driver).long_press(el=press_element,duration=1000).release().perform()


########################## wait等待 ##########################
#按下等待一秒然后抬起
"""
wait method
    Args:
        ms: 暂停，持续时间
"""
# TouchAction(driver).press(el=press_element).wait(1000).release().perform()


#退出当前应用
# driver.close_app()
#直接关闭驱动对象
driver.quit()


# print(driver) #driver对象存在，
# print(driver.current_package) #当执行到这行代码时，异常（A session is either terminated or not started）


