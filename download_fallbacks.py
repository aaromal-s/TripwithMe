import os
import urllib.request

fallbacks = {
    "images/meghalaya.jpg": "https://picsum.photos/800/600?random=1",
    "images/uttarakhand.jpg": "https://picsum.photos/800/600?random=2",
    "images/kerala-details.jpg": "https://picsum.photos/1920/1080?random=3"
}

for local_path, fallback_url in fallbacks.items():
    if not os.path.exists(local_path):
        print(f"Downloading fallback for {local_path} from {fallback_url}")
        try:
            req = urllib.request.Request(fallback_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                final_url = response.geturl() # follow redirect
                
            req2 = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req2) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {fallback_url}: {e}")

# Try to download the video using a different header or a sample video
video_path = "images/hero-video.mp4"
if not os.path.exists(video_path):
    print("Downloading fallback video...")
    try:
        # A known working sample video
        video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/720/Big_Buck_Bunny_720_10s_1MB.mp4"
        req = urllib.request.Request(video_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(video_path, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Failed to download video: {e}")
