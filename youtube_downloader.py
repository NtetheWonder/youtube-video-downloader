from pytube import YouTube

def display_streams(yt):
    print("Available video streams:")
    for stream in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution'):
        print(f"{stream.resolution}: {stream.filesize / (1024*1024):.2f} MB")

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        display_streams(yt)
        choice = input("Enter the resolution you want to download (e.g., 720p): ")
        stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=choice).first()
        if stream:
            print(f"Downloading {stream.resolution} video...")
            stream.download(output_path=save_path)
            print("Download completed successfully!")
        else:
            print("Invalid resolution choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path where you want to save the video: ")

    download_video(video_url, save_path)
