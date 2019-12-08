# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
auto_setup(__file__)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)


driver.get("https://crmhybridapp.autohome.com.cn/webapp/firstPage/chargeIndex")
driver.set_window_size(500,950)
driver.find_element_by_xpath("//input[@placeholder='请输入OA账号']").click()
driver.find_element_by_xpath("//input[@placeholder='请输入OA账号']").send_keys("wangjian1102")
driver.find_element_by_xpath("//input[@placeholder='请输入OA密码']").click()
driver.find_element_by_xpath("//input[@placeholder='请输入OA密码']").send_keys("Auto5678")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/a/div").click()

driver.airtest_touch(Template(r"tpl1575735320020.png", record_pos=(16.77, 8.99), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1575735408604.png", record_pos=(13.075, 1.8), resolution=(100, 100)), "汪剑登录成")




