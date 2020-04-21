import requests
from bs4 import BeautifulSoup

class Link:
    title = None
    duration = None
    src = None



class Links:
    url = 'https://www.youtube.com/results'
    payload = {'search_query':'science'}
    filename = "youtube_results.html"
    links = []
    # <div id="progress" class="style-scope ytd-thumbnail-overlay-resume-playback-renderer" style="width: 67%;"></div>
    def __init__(self,search):
        self.getPage(search)
        return 

    def getPage(self,search):
        self.payload['search_query'] = search
        request = requests.get(self.url, params=self.payload)
        with open(self.filename, "wb") as f:
            f.write(request.content)
        self.getData()

    def getData(self):
        soup = BeautifulSoup(open(self.filename),features="lxml")
        headers = soup.select('h3')
        for header in headers: 
            headerClasses = header.get('class')
            if headerClasses:
                if 'yt-lockup-title' in headerClasses:
                    soup = BeautifulSoup(str(header), 'html.parser')
                    spans = soup.find_all('span')
                    if spans[0].string:
                        link = Link
                        link.title = spans[0].string
                        link.duration = spans[1].string
                        link.src = soup.a.get('href')
                        self.links.append(link)       


    # print(headers)
    # videos = []
    # repeats = []
    # filenamesCollection = []
    # for(dirpath, dirnames, filenames) in walk('E:/Documentary'):
    #     filenamesCollection += filenames

    # for item in data:
    #     if item:
    #         if item['title']:
    #             if item['title'] in filenamesCollection:
    #                 repeats.append(item)  
    #             else:
    #                 videos.append(Video(item['title'],item['duration'],item['src']))


    # mylist = [video.__dict__ for video in videos]

    # print(mylist)
    # database = Database()

    # database.insert(mylist) 