from database import Database
from scraper import scrap
from video import Video

database = Database()
database.db = 'failed'
data = database.find()
videos:Video = []

for item in data:
    video = Video(None,None)
    for key,value in item.items():
        if key == '_id':
            continue
        video.__dict__[key] = value       

    print(video.__dict__)
    videos.append(video)

# scrap(videos)    

