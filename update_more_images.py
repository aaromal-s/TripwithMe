import os
import urllib.request

# URLs for real photos
images = {
    "images/kerala.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Alleppey.jpg",
    "images/kerala-details.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/04/Kerala_backwaters%2C_Vembanad_Lake%2C_India.jpg",
    "images/meghalaya.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/83/Living_Root_Bridge%2C_Meghalaya%2C_India.jpg",
    "images/uttarakhand.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/64/Kedarnath_Temple.jpg"
}

# Fallbacks in case the first one 404s
fallbacks = {
    "images/uttarakhand.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/18/Kedarnath_Temple_Uttarakhand.jpg"
}

for local_path, url in images.items():
    print(f"Downloading {local_path} from {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(local_path, 'wb') as f:
                f.write(response.read())
        print("Success.")
    except Exception as e:
        print(f"Failed: {e}")
        if local_path in fallbacks:
            alt_url = fallbacks[local_path]
            print(f"Trying fallback {alt_url}")
            try:
                req = urllib.request.Request(alt_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    with open(local_path, 'wb') as f:
                        f.write(response.read())
                print("Fallback success.")
            except Exception as e2:
                print(f"Fallback failed: {e2}")

