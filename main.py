import requests
from bs4 import BeautifulSoup
from video import Video
from os import walk
from database import Database
from scraper import scrap

def getData(header,directory):
    spans = header.find_all('span')
    if len(spans)>0:
        duration = spans[0].string,
        duration = str(duration[0]).split(': ')[-1].replace('.','').split(':')
        
        return Video (
            title = header.a.string,
            duration = duration,
            src = header.a.get('href'),
            directory = directory
        )

    return None

def get_next_page(next_page,page_number,search = 'Science documantaries',directory = 'E:/Documentary/',VIDEO_LIMIT = None):
    path = './html/youtube_results.html'
    page = 'results?search_query=' + search

    if next_page:
        page = next_page
    url = 'https://www.youtube.com/' + page
    request = requests.get(url)

    with open(path, "wb") as f:
        f.write(request.content)

    soup = BeautifulSoup(open(path,encoding="utf8"),features="html.parser")
    headers = soup.select('.yt-lockup-title')
    # print(headers)
    videos = [getData(header,directory + search) for header in headers]
    scrap(videos)
    hrefs = soup.select('.branded-page-box > a')
    return [href.get('href') for href in hrefs if href.get_text().isdigit() and int(href.get_text()) == page_number][0]

next_page = None
page_number = 2
search = 'Science documantaries'
PAGE_LIMIT = 20

VIDEO_LIMIT = 20
counter = 0
directory = 'E:/Documentary/'

next_page = get_next_page(next_page,page_number,search,directory = directory)
while next_page:
    page_number += 1
    counter +=1
    print("PAGE NUMBERS: {} PAGE_LIMIT {}  CURRENT PAGE: {} \nLINK:{}".format(counter,PAGE_LIMIT,page_number,next_page))
    next_page = get_next_page(next_page,page_number,search,directory = directory)
    if(PAGE_LIMIT and counter>PAGE_LIMIT):
        break