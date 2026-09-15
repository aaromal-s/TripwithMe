import os
import re
import urllib.request

# Define mapping of base photo IDs/URLs to local filenames
asset_mapping = {
    "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-beautiful-beach-and-the-sea-1258-large.mp4": "hero-video.mp4",
    "photo-1524492412937-b28074a5d7da": "hero-bg.jpg",
    "photo-1598228723793-52759bba239c": "kerala.jpg",
    "photo-1477587458883-47145ed94245": "rajasthan.jpg",
    "photo-1626621341517-bbf3d9990a23": "himachal.jpg",
    "photo-1512343879784-a960bf40e7f2": "goa.jpg",
    "photo-1571536802807-3cab8d9d40b9": "uttarakhand.jpg",
    "photo-1588095147817-48f5728a05db": "meghalaya.jpg",
    "photo-1599661559684-6338525b642e": "kerala-details.jpg",
    "photo-1593693397690-362cb9666fc2": "contact-bg.jpg"
}

os.makedirs('images', exist_ok=True)

files_to_update = ['index.html', 'packages.html', 'trip-details.html', 'style.css']

# Download logic + Replace logic
for filename in files_to_update:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all Unsplash URLs and Mixkit Video
    urls = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+\?[^\s"\'\)]+', content)
    urls += re.findall(r'https://assets\.mixkit\.co/[^\s"\'\)]+', content)
    
    # We want to remove &quot; from the end if it was caught
    cleaned_urls = [url.replace('&quot;', '') for url in urls]

    for url in set(cleaned_urls):
        # determine local filename
        local_name = "unknown.jpg"
        for key, name in asset_mapping.items():
            if key in url:
                local_name = name
                break
        
        local_path = f"images/{local_name}"
        
        # Download if not exists
        if not os.path.exists(local_path):
            print(f"Downloading {local_name} from {url}")
            try:
                # Add headers because sometimes unsplash blocks python urllib
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Failed to download {url}: {e}")
        
        # Replace in content (handling exact strings)
        content = content.replace(url, local_path)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished processing assets.")
