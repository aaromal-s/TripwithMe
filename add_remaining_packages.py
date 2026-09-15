import os
import urllib.request
import re

# 1. Download images for the new packages
new_images = {
    "images/andaman.jpg": "https://picsum.photos/800/600?random=11",
    "images/kashmir.jpg": "https://picsum.photos/800/600?random=12",
    "images/spiti.jpg": "https://picsum.photos/800/600?random=13",
    "images/darjeeling.jpg": "https://picsum.photos/800/600?random=14"
}

os.makedirs('images', exist_ok=True)
for local_path, url in new_images.items():
    if not os.path.exists(local_path):
        print(f"Downloading {local_path}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                final_url = response.geturl()
            req2 = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req2) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {local_path}: {e}")

# 2. HTML content for 4 new packages
NEW_PACKAGES = """
        <!-- Card 7 -->
        <div class="pkg-card flip-card-wrapper" data-region="South India" data-style="Relaxation">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input type="checkbox" class="compare-checkbox" data-title="Andaman Islands" title="Compare" />
              </div>
              <img src="images/andaman.jpg" alt="Andaman" class="pkg-img" />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Andaman
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    7 Days
                  </span>
                </div>
                <h3 class="pkg-title">Andaman Islands</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">Pristine beaches and vibrant coral reefs.</p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="45000">₹45,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Scuba Diving</li>
                <li>✓ Radhanagar Beach</li>
                <li>✓ Cellular Jail</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>

        <!-- Card 8 -->
        <div class="pkg-card flip-card-wrapper" data-region="North India" data-style="Adventure">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input type="checkbox" class="compare-checkbox" data-title="Kashmir Paradise" title="Compare" />
              </div>
              <img src="images/kashmir.jpg" alt="Kashmir" class="pkg-img" />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Kashmir
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    6 Days
                  </span>
                </div>
                <h3 class="pkg-title">Kashmir Paradise</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">Experience heaven on earth in the valleys.</p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="38000">₹38,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Dal Lake Shikara</li>
                <li>✓ Gulmarg Gondola</li>
                <li>✓ Pahalgam Views</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>

        <!-- Card 9 -->
        <div class="pkg-card flip-card-wrapper" data-region="North India" data-style="Adventure">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input type="checkbox" class="compare-checkbox" data-title="Spiti Valley Expedition" title="Compare" />
              </div>
              <img src="images/spiti.jpg" alt="Spiti Valley" class="pkg-img" />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Spiti Valley
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    8 Days
                  </span>
                </div>
                <h3 class="pkg-title">Spiti Valley Expedition</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">Rugged mountain terrains and ancient monasteries.</p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="35000">₹35,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Key Monastery</li>
                <li>✓ Chandratal Lake</li>
                <li>✓ High Altitude Roads</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>

        <!-- Card 10 -->
        <div class="pkg-card flip-card-wrapper" data-region="East India" data-style="Nature & Wildlife">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input type="checkbox" class="compare-checkbox" data-title="Darjeeling Tea Trails" title="Compare" />
              </div>
              <img src="images/darjeeling.jpg" alt="Darjeeling" class="pkg-img" />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Darjeeling
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    4 Days
                  </span>
                </div>
                <h3 class="pkg-title">Darjeeling Tea Trails</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">Rolling hills and the iconic toy train experience.</p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="18000">₹18,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Tea Garden Tour</li>
                <li>✓ Toy Train Ride</li>
                <li>✓ Tiger Hill Sunrise</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>
"""

with open('packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we don't duplicate if script is run twice
if "Darjeeling Tea Trails" not in content:
    new_content = content.replace("      </section>", NEW_PACKAGES + "\n      </section>")
    with open('packages.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Added 4 new packages to packages.html")
else:
    print("Packages already exist.")
