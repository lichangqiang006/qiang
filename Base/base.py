from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver=driver
    # 封装查找元素的方法 真正目的是给以下方法使用  点击、输入
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 封装点击方法
    def base_click_element(self,loc):
        self.base_find_element(loc).click()
    # 封装输入方法
    def base_input_text(self,loc,text):
        self.base_find_element(loc).send_keys(text)
    # 封装截图方法
    def base_get_img(self,imagePath):
        self.driver.get_screenshot_as_file(imagePath)