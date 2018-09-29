from selenium.webdriver.common.by import By
from Base.base import Base
"""
    以下定位数据，我们临时先放到这里
"""
# 搜索按钮id
search_btn = By.ID, "com.android.settings:id/search"
input_search=By.ID,"android:id/search_src_text"
back_btn=By.CLASS_NAME,"android.widget.ImageButton"

class PageSetting(Base):
    # 点击搜索按钮 方法封装
    def page_click_search_btn(self):
        # 调用base类点击元素方法
        self.base_click_element(search_btn)
    # 输入 方法封装
    def page_input_text(self,text):
        self.base_input_text(input_search,text)
    # 点击搜索框返回按钮
    def page_click_back_btn(self):
        self.base_click_element(back_btn)