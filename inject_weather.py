import glob
import re

WEATHER_HTML = """
          <!-- Live Weather Widget -->
          <div id="weather-widget" class="weather-widget glassmorphism" style="margin-top: 1rem; padding: 1rem; display: inline-flex; align-items: center; gap: 1rem; border-radius: 20px;">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#f59e0b" width="30" height="30">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
            </svg>
            <div>
              <span style="font-size: 0.9rem; color: var(--text-light); display: block;">Live Weather</span>
              <span id="weather-temp" style="font-weight: bold; color: var(--primary-accent); font-size: 1.2rem;">Loading...</span>
            </div>
          </div>
"""

trip_files = glob.glob('d:/Projects/TripwithMe/trip-details*.html')
for file in trip_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where to inject weather. Below the trip-meta div is good.
    if 'id="weather-widget"' not in content:
        # Trip details header usually looks like:
        # </div>
        # </div>
        # </header>
        # Let's just put it in the header banner or right after the title.
        # `<div class="trip-meta">` is a good spot.
        content = re.sub(r'(<div class="trip-meta">.*?</div>)', r'\1\n' + WEATHER_HTML, content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Weather widget injected!")
