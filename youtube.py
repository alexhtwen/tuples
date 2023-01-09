def download_youtube_video(url):

  # Import the modules needed to download the video
  from pytube import YouTube
  import os

  # Get the video from the provided URL
  yt = YouTube(url)

  # Get the video title
  title = yt.title

  # Set the directory for the downloads
  dir_path = os.path.join(os.getcwd(), "youtube_downloads")

  # Check if the directory exists and create it if it doesn't
  if not os.path.exists(dir_path):
    os.mkdir(dir_path)

  # Get the video and download it in the specified directory
  yt.streams.get_highest_resolution().download(dir_path, filename=title)

  # Return the title of the downloaded video
  return title


download_youtube_video('https://www.youtube.com/watch?v=sm2zar9v-so')