import os

from pymediainfo import MediaInfo

os.environ['PATH'] = os.path.dirname('C:/Program Files/MediaInfo/Mediainfo.dll') + ';' + os.environ['PATH']

media_info = MediaInfo.parse('D:/Downloads/Video/Ghost_hunt_07.mp4')
for track in media_info.tracks:
    print(track.track_type)