import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui
import selenium.webdriver.support.expected_conditions as EC
import os
from os import walk,path,makedirs
import time


class Link:
    filename = None
    fileType = None
    src = None
    quality = None


class Video:
    __url = 'https://en.savefrom.net'
    __youtubeUrl = 'http://youtube.com'
    
    links = []
    quality = ''
    filename = ''
    link = ''
    downloaded = False
    def __init__(self, title, src , duration = None,default = True,separate_short_videos=True,directory = "E:/Documentary/Unseen/"):
        self.title = title
        self.duration = duration
        self.src = src
        self.default = default  
        self.directory = directory
    
        if separate_short_videos: 
            self.directory + '/short_videos/'

    def getLinks(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        browser = webdriver.Chrome(options=options)
        
        self.__url += '?url=' + self.__youtubeUrl + self.src
        browser.get(self.__url)
        try:
            time.sleep(15)
            if self.default :
                href = browser.find_element_by_css_selector('.def-btn-box>a')
                link = Link() 
                self.filename = href.get_attribute("download") if href.get_attribute("download") else None
                self.link = href.get_attribute("href")
                self.fileType = href.get_attribute("data-type")
                self.quality = href.get_attribute("data-quality")
            
            hrefs = browser.find_elements_by_css_selector('.link-group>a')
            links = []
            for href in hrefs:
                link = Link() 
                link.filename = href.get_attribute("download") if href.get_attribute("download") else None
                link.src = href.get_attribute("href")
                link.fileType = href.get_attribute("data-type")
                link.quality = href.get_attribute("data-quality")

                if link.filename and not self.filename:
                    self.filename = link.filename 
                # print(link.__dict__)
                if 'dash' in link.fileType:
                    continue
                links.append(link)            

            self.best_quality = max(link.quality for link in links)

            for link in links:
                if link.filename:
                    self.filename = link.filename  
                    break
                
            self.links = [link.__dict__ for link in links]
            browser.quit()
            return True
        except: 
            print("Video:" + self.title + " failed to get data")
            browser.quit()
            return False
        finally:
            browser.quit()

    def download(self):
        if not self.getLinks():
            return False

        try:
            if not path.isdir(self.directory):
                makedirs(self.directory)
                print("Directory created!")

            urllib.request.urlretrieve(self.link, self.directory +'/' + self.filename)
            self.downloaded = True
            print("Video: " + self.title + " downloaded")
            return self.downloaded
        except :
            self.downloaded = False
            print("Video:" + self.title + " failed during downloading")
            return self.downloaded
