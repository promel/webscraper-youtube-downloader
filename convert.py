from os import unlink
from subprocess import check_output, STDOUT, CalledProcessError

def convert(source,destination):
    args = ['ffmpeg', '-i', source , destination]
    try:
        txt = check_output(args, stderr=STDOUT)
        print(txt)
    except CalledProcessError as e:
        print ("conversion failed", e)
    else:
        print (source, ' converted to ',destination)