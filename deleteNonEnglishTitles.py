from langdetect import detect
from os import walk,remove,startfile

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

collection = []
for(dirpath, dirnames, filenames) in walk('E:/Documentary/'):
    if filenames:
        collection.append({dirpath:filenames})

for data in collection:
    for path,filenames in data.items():
        print("PATH:" + path)
        for filename in filenames:
            print("FILENAME:" + filename)
            if not isEnglish(filename.split('.')[0]): 
                print("NOT ENGLISH:" + filename)
                response = 'm'
                while response =='m':
                    print("Delete " + filename + "?")
                    response = input()
                    if response == 'y':
                        remove(path + '/' + filename)
                        print(filename + " DETELED!!!")
                    elif response == 'm':
                        startfile(path + '/' + filename)
                    elif response =='n':
                        print("SKIPPED!!!")

