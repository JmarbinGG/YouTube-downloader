from pytube import YouTube
print("Youtube Downloader By Jmarbin!")
url = input("Enter Youtube Video Link: ") 
print("loading...")
YouTube(url).streams.get_highest_resolution().download()

print("downloaded to the project folder!")
