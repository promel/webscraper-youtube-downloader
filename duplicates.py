from database import Database
from os import walk

database = Database()
data = database.find()
print(data.count())
for item in data:
    print(item)
    if not item.get('title'):
        print('No title deleted:',item)
        database.delete({'_id':item['_id']})
        continue
    innerData = database.find({'title':item['title']})
    default = {}
    duplicates = []
    if innerData.count() == 1:
        continue 
      
    for innerItem in innerData:
        if not default and innerItem.get('title') and innerItem.get('directory'):
            default = innerItem 
            continue
        print('deleted:',innerItem.get('title'))
        database.delete({'_id':innerItem['_id']})
        del innerItem['_id'] 
        duplicates.append(innerItem)

    if not default:
        default = item
        database.insert(item)
        print('inserted:',item)

    if not default.get('directory'):
        for(dirpath, dirnames, filenames) in walk('E:/'):
            if default.get('filename') and default['filename'] in filenames: 
               default.__setitem__('directory',dirpath)          

    time = [element.replace("',)",'') for element in default['duration']]
    default['duration'] = time
    database.update({'_id':default['_id']},default)

    print('Number of duplicates: ',len(duplicates))
  

