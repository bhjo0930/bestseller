# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:27:03 2020

@author: bhjo0
"""



from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time
import pandas as pd

try:    # 정상 처리
    chromedriver = 'D:/app/chromedriver_72.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    options.add_argument('disable-gpu')    # GPU 사용 안함
    options.add_argument('lang=ko_KR')    # 언어 설정
    driver = webdriver.Chrome(chromedriver, options=options)
    #driver = webdriver.Chrome(chromedriver)
    
    #Best
    url = 'http://www.yes24.com/24/Category/BestSeller'
    #Search
#    url = 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query=%C3%A5+%C0%D0%BE%EE%B5%E5%B8%B3%B4%CF%B4%D9'
    driver.get(url)    # 크롤링할 사이트 호출
    #titleList = driver.find_elements_by_class_name('copy') 
    
    for i in range(1,21):
        #Best
        titleData = driver.find_element_by_xpath('//*[@id="bestList"]/ol/li['+str(i)+']/p[1]/a')
        #Search
 #       titleData = driver.find_element_by_xpath('//*[@id="schMid_wrap"]/div[3]/div[2]/table/tbody/tr['+str(i*2-1)+']/td[2]/p[1]')

        print(str(i)+'위 '+ titleData.text)
        print(titleData.get_property('href'))

except TimeoutException:    # 예외 처리
    print('해당 페이지에 연극 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()
    
    
    