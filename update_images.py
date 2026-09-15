import os
import urllib.request
import urllib.parse

# Real photo URLs from Wikimedia Commons
new_images = {
    "images/kashmir.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Dal_Lake%2C_Kashmir.jpg",
    "images/spiti.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Key_Monastery_Spiti.jpg",
    "images/darjeeling.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/51/Darjeeling%2C_India%2C_Tea_plantations.jpg",
    "images/andaman.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/87/Havelock_Island_Beach_No_7.jpg" # A known Wikipedia image
}

for local_path, url in new_images.items():
    print(f"Downloading real photo for {local_path}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully downloaded {local_path}")
    except Exception as e:
        print(f"Failed to download {local_path}: {e}")
        # Try another Andaman link if it fails
        if 'andaman' in local_path:
            alt_url = "https://upload.wikimedia.org/wikipedia/commons/1/1d/Radhanagar_Beach_Havelock_Island_Andaman.jpg"
            print(f"Trying alternative URL for {local_path}...")
            try:
                req = urllib.request.Request(alt_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    with open(local_path, 'wb') as out_file:
                        out_file.write(response.read())
                print(f"Successfully downloaded {local_path}")
            except Exception as e2:
                print(f"Alternative failed: {e2}")

