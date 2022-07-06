import pytube

#Ask for video url
url = input('Enter video url: ')

#Specify the storage path of video
path = 'D:\Mitch\Repos\clcoding'

#magic line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)