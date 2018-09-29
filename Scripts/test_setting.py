import sys,os
sys.path.append(os.getcwd())
from Page.page_setting import PageSetting
from Base.get_driver import get_driver
class TestSetting():
    def setup(self):
        # 获取driver
        self.driver=get_driver()
        # 实例化setting页面对象
        self.setting = PageSetting(self.driver)
    def teardown(self):
        # 关闭driver驱动对象
        self.driver.quit()
    # 执行测试方法
    def test_setting(self):
        # 点击搜索按钮
        self.setting.page_click_search_btn()
        # 输入搜索内容
        self.setting.page_input_text("wlan")
        # 点击返回按钮
        self.setting.page_click_back_btn()