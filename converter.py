from os import walk, path, makedirs, unlink
from subprocess import check_output, STDOUT, CalledProcessError
from database import Database
from audio import Audio

# source_directory = 'C:/Users/Joseph More/Videos/Stash'
# destination_directory = 'C:/Users/Joseph More/Videos/Converted'

source_directory = 'E:/Music Videos/'
destination_directory = 'E:/Music/Converted/'

extensions = ['webm', 'gif', 'mp4']
file_format = '.mp3'
db = Database('audioCollection', 'audios')

for (dirpath, dirnames, videos) in walk(source_directory):
    for video in videos:
        parts = [video.split('.' + extension)
                 for extension in extensions if extension in video]
        # print(parts)
        filename = ''
        title = ''

        if parts:
            title = parts[0][0]
            filename = title + file_format
        else:
            continue

        if db.find_one({'title': title}):
            print('title {} SKIPPED!!!'.format(title))
            continue

        directory = dirpath.split('/')[-1]
        print()
        full_destination_directory = destination_directory + directory
        if not path.isdir(full_destination_directory):
            makedirs(full_destination_directory)

        args = ['ffmpeg', '-i', source_directory + directory + '/' +
                video,  full_destination_directory + '/' + filename]
        try:
            txt = check_output(args, stderr=STDOUT)
        except CalledProcessError as e:
            print("conversion failed", e)
        else:
            # unlink(source_directory + '/' + video)
            print(video, 'converted to', filename)
            audio = Audio(title, destination_directory, length='?',
                          size='?', file_format=file_format)
            db.insert(audio.__dict__)
