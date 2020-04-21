from video import Video
from os import walk
from database import Database

def scrap(videos,directory = None):

    filenamesCollection = []
    if directory:
        for(dirpath, dirnames, filenames) in walk(directory):
            filenamesCollection += filenames

    filenames = [item.split('.')[0] for item in filenamesCollection]
    print(filenames)
    database = Database()
    for video in videos:
        # separate_short_videos = True
        # if VIDEO_LIMIT
        database.db = 'videos'

        if video:
            title = video.title
            # duration = video.duration
            if not title or 'hindi' in title.lower() or 'bollywood' in title.lower():
                continue
            # if len(item['duration'])<2 and int(item['duration'][0]) < lenght_limit and reject_short_videos :
            #     rejects.append(item)
            #     continue
            # if len(item['duration'])<2 and int(item['duration'][0]) < lenght_limit and separate_short_videos :
            #     separate_short_videos = False
            if database.find_one({'title': title}):
                print("IN DB: " + title + " SKIPPED!")
                continue

            if filenames and title in filenames:
                database.insert(video)
                print("REPEAT:" + title + " SKIPPED!")
                continue

            print(video.__dict__)
            video.download()

            if video.downloaded:
                database.insert(video.__dict__)
            else:
                database.db = 'failed'
                database.insert(video.__dict__)
