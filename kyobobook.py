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
import re

def makeDetailUrl(href):
    #str = "javascript:makeDetailUrl('KOR','15','9791161951164','0 ', 'N' )"
    regex = r"(?P<ejkGb>\'\w+\')+,(?P<linkClass>\'\d+\')+,(?P<barcode>\'\d+\')+,(\'\d+\s\')"

    matches = re.finditer(regex, href, re.MULTILINE)
    
    for matchNum, match in enumerate(matches, start=1):
        
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    
        ejkGb = match.group("ejkGb").replace("'","")
        linkClass = match.group("linkClass").replace("'","")
        barcode = match.group("barcode").replace("'","")
        #print(ejkGb,linkClass,barcode)
    
    domain = 'http://www.kyobobook.co.kr'
    tempBarcode = barcode[:2]
    linkUrl = ""
    sUrl = ""

    if(tempBarcode == "14"):
        linkUrl = "http://pod.kyobobook.co.kr/soldOutPODBookList/soldOutPODBookDetailView.ink?orderClick="
    elif(tempBarcode == "29"):
        linkUrl = domain+"/product/detailViewPackage.laf?mallGb=PKG"            
    elif(ejkGb == 'KOR'):
        linkUrl = domain+"/product/detailViewKor.laf?mallGb=KOR"
    else:
        print('error')
        
    sUrl = linkUrl + "&ejkGb=" + ejkGb + "&linkClass=" + linkClass + "&barcode=" + barcode

    return sUrl

try:    # 정상 처리
    chromedriver = 'D:/app/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    options.add_argument('disable-gpu')    # GPU 사용 안함
    options.add_argument('lang=ko_KR')    # 언어 설정
    driver = webdriver.Chrome(chromedriver, options=options)
    #driver = webdriver.Chrome(chromedriver)
    
    #자기계발서
    print('##### 자기계발서 #####')
    url= 'http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb=KOR&linkClass=15&menuCode=002'
    driver.get(url)    # 크롤링할 사이트 호출
    #titleList = driver.find_elements_by_class_name('copy') 
    
    for i in range(1,21):
        titleData = driver.find_element_by_xpath('//*[@id="prd_list_type1"]/li['+str(-1+i*2)+']/div/div[1]/div[2]/div[1]/a')
        #titleData = driver.find_element_by_xpath('//*[@id="bestList"]/ol/li['+str(i)+']/p[1]/a')
        print(str(i)+'위 '+ titleData.text)
        print(makeDetailUrl(titleData.get_property('href')))


    #경영경제
    print('##### 경제/경영 #####')
    url= 'http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb=KOR&linkClass=13&menuCode=002'
    driver.get(url)    # 크롤링할 사이트 호출
    
    for i in range(1,21):
        titleData = driver.find_element_by_xpath('//*[@id="prd_list_type1"]/li['+str(-1+i*2)+']/div/div[1]/div[2]/div[1]/a')
        #titleData = driver.find_element_by_xpath('//*[@id="bestList"]/ol/li['+str(i)+']/p[1]/a')
        print(str(i)+'위 '+ titleData.text)
        print(makeDetailUrl(titleData.get_property('href')))        



except TimeoutException:    # 예외 처리
    print('해당 페이지에 연극 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()
    

