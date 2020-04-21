from os import walk,path,makedirs
# from pydub import AudioSegment
import json
from database import Database
from audio import Audio
from converter import convert

db = Database("ConvertedAudio","audios")
source_directory = 'E:/Music Videos/'
destination_directory = 'E:/Music/Converted/'

for (dirpath, dirnames, videos) in walk(source_directory):
    for video in videos:
        parts = video.split('.mp4')
        filename = ''
        title  = ''
        file_format = '.mp3'
        
        if len(parts)>1:
            title = parts[0]
            filename =  title + file_format
        else:
            continue
            
        db = Database('audioCollection','audios')
        if db.find_one({'title':title}):
            print('title {} SKIPPED!!!'.format(title))
            continue

        directory = dirpath.split('/')[-1]
        full_destination_directory = destination_directory + directory 
        if not path.isdir(full_destination_directory):
            makedirs(full_destination_directory)

        convert(dirpath + '/' + video,full_destination_directory + '/' + filename)
        audio = Audio(title,directory,length = '?',size = '?',file_format = file_format )
        db.insert(audio.__dict__)




