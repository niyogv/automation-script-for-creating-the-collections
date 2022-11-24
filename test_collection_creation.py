# This is an automation script of python
# Application name : devmarket.moiverse.io
# Author : Niyog V
# Test scenario : Creating collection with different scenario
# date : 01-04-2022

import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from utlities.utlis import Home

class Test_qamarket_create_collection_public:

# This is a function which reads data of test1 from excel sheet
    @pytest.fixture(params=Home.readDataCollection('test1')) # the name of the test which is mentioned under the xl sheet
    def getdata(self,request):
        return request.param

# This is a function which reads data of test2 from excel sheet
    @pytest.fixture(params=Home.readDataCollection('test2')) # the name of the test which is mentioned under the xl sheet
    def getdata1(self,request):
        return request.param

# This is a function which reads data of test3 from excel sheet
    @pytest.fixture(params=Home.readDataCollection('test3')) # the name of the test which is mentioned under the xl sheet
    def getdata2(self,request):
        return request.param

# This is a pre-defined function which runs before entering into collection creation
    @pytest.fixture
    def test_Invoke(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        wait=WebDriverWait(self.driver,10)
        self.driver.get('https://devmarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        user=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys('')
        password=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys('')
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(10)

# This is a main function which reads data of test1 from excel sheet, uploads image from HDD and creates collection
    def test_1(self,test_Invoke,getdata):
        self.driver.find_element_by_xpath("//div[@class='styles_account__3MgT6 styles_menuLink__17kgw']").click()
        self.driver.find_element_by_xpath("//ul[@class='MuiList-root MuiMenu-list styles_menuList__33Jfh MuiList-padding']/div[2]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys('/Users/aicumen-dev/Downloads/')
        self.driver.find_element_by_xpath("//input[@placeholder='Collection Name']").send_keys(getdata['name'])
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/textarea').send_keys(getdata['description'])
        self.driver.find_element_by_xpath("//input[@placeholder='Collection Royalty']").send_keys(getdata['royality'])
        self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div[1]/div[2]/div[4]/div').click()
        time.sleep(30)
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert True
            else:
                assert False
        finally:
            self.driver.quit()

# This is a main function which reads data of test2 from excel sheet and repeats the same data as in test1 and checks
# whether the collection is created or not (It should show the error message as "Collection name already exist")
    def test_2(self,test_Invoke,getdata1):
        self.driver.find_element_by_xpath("//div[@class='styles_account__3MgT6 styles_menuLink__17kgw']").click()
        self.driver.find_element_by_xpath("//ul[@class='MuiList-root MuiMenu-list styles_menuList__33Jfh MuiList-padding']/div[2]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys('/Users/aicumen-dev/Downloads/')
        self.driver.find_element_by_xpath("//input[@placeholder='Collection Name']").send_keys(getdata1['name'])
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/textarea').send_keys(getdata1['description'])
        self.driver.find_element_by_xpath("//input[@placeholder='Collection Royalty']").send_keys(getdata1['royality'])
        self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div[1]/div[2]/div[4]/div').click()
        time.sleep(10)
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert False,'Collection name already exist'
            else:
                assert True
        finally:
            self.driver.quit()

# This is a main function which reads data of test3 from excel sheet and repeats the different data and same image as in test1 and checks
# whether the collection is created or not (It should show the error message as "Collection name already exist")
    def test_3(self,test_Invoke,getdata2):
        self.driver.find_element_by_xpath("//div[@class='styles_account__3MgT6 styles_menuLink__17kgw']").click()
        self.driver.find_element_by_xpath("//ul[@class='MuiList-root MuiMenu-list styles_menuList__33Jfh MuiList-padding']/div[2]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys('/Users/aicumen-dev/Downloads/')
        self.driver.find_element_by_xpath("//input[@placeholder='Collection Name']").send_keys(getdata2['name'])
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/textarea').send_keys(getdata2['description'])
        self.driver.find_element_by_xpath("//input[@placeholder='Collection Royalty']").send_keys(getdata2['royality'])
        self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div[1]/div[2]/div[4]/div').click()
        time.sleep(10)
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert False,'Collection name already exist'
            else:
                assert True
        finally:
            self.driver.quit()



