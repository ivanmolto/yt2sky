import siaskynet
import pyinputplus as pyip
from pytube import YouTube
import webbrowser
import os

blurb_prompt = 'Please enter the YouTube video link: '
blurb_saved_locally = 'Your high resolution mp4 YouTube video has been saved locally as:  '
blurb_current_directory = 'You will find it at the current directory: '
blurb_uploading_snapshot = 'Now uploading your video to Skynet...'
blurb_description = 'This is the Skylink that you can share with anyone to retrieve your video on any Skynet Webportal:'
blurb_url = 'Please check at the follow link: '
blurb_host = 'https://siasky.net/'

video_file_name = ''

video_link = pyip.inputStr(prompt=blurb_prompt)
print()

yt = YouTube(video_link)
try:
    video_download = yt.streams.filter(
        subtype='mp4').get_highest_resolution().download()
except:
    print('Failed to Download the video ')
    exit()

for root, dirs, files in os.walk("."):
    for filename in files:
        if "mp4" in filename:
            video_download_name = filename

print(blurb_saved_locally + video_download_name)
print()
path_to_video = os.getcwd()
print(blurb_current_directory + str(path_to_video))
print()

skylink = siaskynet.upload_file(video_download_name)
print(blurb_description)
print(skylink)
print()
url_link = blurb_host + skylink[6:]
print(blurb_url + url_link)
webbrowser.open_new(url_link)
