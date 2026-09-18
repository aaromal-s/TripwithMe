import glob
import re

SEARCH_HTML = """
          <!-- Global Search -->
          <div class="search-container" style="position: relative; margin-right: 1rem;">
            <input type="text" id="global-search" class="glass-input" placeholder="Search destinations..." style="padding: 0.5rem 1rem; border-radius: 20px; width: 200px;">
            <div id="search-results" class="search-results glassmorphism" style="position: absolute; top: 110%; left: 0; width: 100%; border-radius: 8px; display: none; flex-direction: column; z-index: 1000; max-height: 300px; overflow-y: auto;"></div>
          </div>
"""

# 1. Inject Search into ALL headers
html_files = glob.glob('d:/Projects/TripwithMe/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert right after <div class="header-controls">
    if 'id="global-search"' not in content and '<div class="header-controls">' in content:
        content = content.replace('<div class="header-controls">', '<div class="header-controls">' + SEARCH_HTML)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. Inject Favorite Heart Button into package cards in index and packages
FAVORITE_HTML = """
            <button class="favorite-btn" style="position: absolute; top: 10px; right: 10px; background: rgba(255,255,255,0.7); border: none; border-radius: 50%; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10; transition: all 0.3s ease;">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="#ff4757" width="20" height="20" class="heart-icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
              </svg>
            </button>
"""

for file in ['d:/Projects/TripwithMe/index.html', 'd:/Projects/TripwithMe/packages.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # The package image is usually `<img src="images/...`
    # Let's insert the button right before the <img class="pkg-img"> inside <div class="flip-card-front">
    if 'favorite-btn' not in content:
        content = content.replace('<div class="flip-card-front">', '<div class="flip-card-front">' + FAVORITE_HTML)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Search bar and Favorite buttons injected!")
