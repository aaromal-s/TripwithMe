import re

NEW_PACKAGES = """
        <!-- Card 5 -->
        <div
          class="pkg-card flip-card-wrapper"
          data-region="North India"
          data-style="Nature & Wildlife"
        >
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input
                  type="checkbox"
                  class="compare-checkbox"
                  data-title="Spiritual Uttarakhand"
                  title="Compare"
                />
              </div>
              <img
                src="images/uttarakhand.jpg"
                alt="Uttarakhand"
                class="pkg-img"
              />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Uttarakhand
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    5 Days
                  </span>
                </div>
                <h3 class="pkg-title">Spiritual Uttarakhand</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">
                  Himalayan treks and peaceful spiritual retreats.
                </p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="22000">₹22,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Kedarnath Trek</li>
                <li>✓ Ganges Aarti</li>
                <li>✓ Yoga Retreat</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>

        <!-- Card 6 -->
        <div
          class="pkg-card flip-card-wrapper"
          data-region="North East India"
          data-style="Nature & Wildlife"
        >
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input
                  type="checkbox"
                  class="compare-checkbox"
                  data-title="Magical Meghalaya"
                  title="Compare"
                />
              </div>
              <img
                src="images/meghalaya.jpg"
                alt="Meghalaya"
                class="pkg-img"
              />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Meghalaya
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    6 Days
                  </span>
                </div>
                <h3 class="pkg-title">Magical Meghalaya</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">
                  Abode of clouds with living root bridges.
                </p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="31000">₹31,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Living Root Bridges</li>
                <li>✓ Dawki River</li>
                <li>✓ Waterfalls</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>
"""

with open('packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Append right before the closing tag of the section with class package-grid
new_content = content.replace("      </section>", NEW_PACKAGES + "\n      </section>")

with open('packages.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
