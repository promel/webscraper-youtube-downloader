from database import Database
from os import walk
database = Database()
data = database.find({"title": "Seeing the Beginning of Time 4K - New Universe Documentary 2019"})

default = data[0]
if not default.get('directory'):
    for(dirpath, dirnames, filenames) in walk('E:/'):
        if default['filename'] in filenames: 
            print(dirpath)
            default.__setitem__('directory',dirpath.replace('\\','/'))          

    time = [element.replace("',)",'') for element in default['duration']]
    default['duration'] = time
    database.update({'_id':default['_id']},default)

print(default)