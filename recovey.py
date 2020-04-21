from database import Database
from scraper import scrap
from video import Video
from os import walk

database = Database()
directory = 'E:/Music Videos/Kanye West'
data = database.find({'directory': directory})
# data = database.find()

if directory:
    for(dirpath, dirnames, filenames) in walk(directory):
        filenames
for item in data:
    time = [item.replace("',)",'') for item in item['duration']]
    item['duration'] = time
    database.update({'_id':item['_id']},item)
    data = database.find({'_id':item['_id']})

    if item['filename'] not in filenames:
        if Video(item['title'],item['src']).download():
            item['downloaded'] = True
            database.update({'_id':item['_id']},item)
        else:
            item['downloaded'] = False
            database.update({'_id':item['_id']},item)



   