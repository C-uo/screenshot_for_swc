import os
import time
from selenium import webdriver

URL = 'https://supercweather.com'
PIC_PATH = os.path.join(os.path.expanduser('~'), 'Pictures/python/screenshot')
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
PIC_NAME = now + '.png'
LOG_NAME = 'log.log'


def w_log(msg, path=PIC_PATH, name=LOG_NAME):
    log_path = os.path.join(path, name)
    with open(log_path, 'a') as log:
        msg = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) + '\t' + msg
        log.writelines(msg)


def screenshot_web(url=URL, path=PIC_PATH, name=PIC_NAME):
    if not os.path.exists(path):
        os.makedirs(path)
    browser = webdriver.PhantomJS()
    browser.set_window_size(1200, 800)
    browser.get(url)
    browser.execute_script('map.setView([35.2939372, 136.255413]);')
    browser.find_element_by_class_name("button04").click()
    browser.find_element_by_class_name('rssel').click()
    browser.find_element_by_xpath('//option[@value="0"]').click()
    time.sleep(10)
    pic_path = os.path.join(os.path.join(path, name))
    print(pic_path)
    if browser.save_screenshot(pic_path):
        w_log('成功!')
    else:
        w_log('スクリーンショット取れない')
    browser.close()


if __name__ == '__main__':
    while True:
        try:
            screenshot_web()
        except BaseException as e:
            w_log(repr(e))
