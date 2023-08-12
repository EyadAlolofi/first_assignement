import pytube

print("Download videos from YouTube using URL")
url = input("Enter the video URL: ")

yt = pytube.YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download('Desktop')

print("Download completed!")