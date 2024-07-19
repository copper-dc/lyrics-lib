import yt_dlp
from lyrics import get_lyrics

def get_video_info(url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    video_info = get_video_info(video_url)

    print("Title:", video_info.get('title', 'N/A'))
    print("Uploader:", video_info.get('uploader', 'N/A'))
    print(get_lyrics(video_info.get('uploader', 'N/A'), video_info.get('title', 'N/A')))
    