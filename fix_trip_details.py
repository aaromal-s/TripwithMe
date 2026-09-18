import glob

LEAFLET_CSS = '    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />\n'
LEAFLET_JS = '    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>\n'

SECTIONS_HTML = """
        <!-- Interactive Itinerary Map -->
        <section>
          <h2 style="color:var(--primary-base); margin-bottom: 1rem;">Route Map</h2>
          <div id="itinerary-map" style="width: 100%; height: 400px; border-radius: var(--border-radius); box-shadow: var(--shadow-sm); z-index: 1;"></div>
        </section>

        <!-- Reviews Section -->
        <section id="reviews-section">
          <h2 style="color:var(--primary-base); margin-bottom: 1rem; margin-top: 2rem;">Customer Reviews</h2>
          
          <div id="reviews-list" style="display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 2rem;">
            <!-- Review 1 -->
            <div class="review-card glassmorphism" style="padding: 1.5rem; display: flex; gap: 1rem; align-items: flex-start;">
              <div class="user-avatar" style="width: 50px; height: 50px; font-size: 1.2rem; flex-shrink: 0;">SA</div>
              <div>
                <h4 style="margin-bottom: 0.2rem;">Sarah Anderson</h4>
                <div style="color: #f59e0b; font-size: 1.2rem; margin-bottom: 0.5rem;">★★★★★</div>
                <p style="color: var(--text-dark);">Absolutely magical experience! The heritage hotels were breathtaking and the guide was extremely knowledgeable. Highly recommend this tour.</p>
              </div>
            </div>
          </div>

          <div class="glassmorphism" style="padding: 2rem;">
            <h3 style="margin-bottom: 1rem; color:var(--text-dark);">Write a Review</h3>
            <form id="review-form" style="display: flex; flex-direction: column; gap: 1rem;">
              <input type="text" id="reviewer-name" class="glass-input" placeholder="Your Name" required />
              <select id="review-rating" class="glass-select" required>
                <option value="5">5 Stars - Excellent</option>
                <option value="4">4 Stars - Very Good</option>
                <option value="3">3 Stars - Average</option>
                <option value="2">2 Stars - Poor</option>
                <option value="1">1 Star - Terrible</option>
              </select>
              <textarea id="review-text" class="glass-input" placeholder="Tell us about your experience..." rows="4" required style="resize: vertical;"></textarea>
              <button type="submit" class="btn btn-primary" style="align-self: flex-start;">Submit Review</button>
            </form>
          </div>
        </section>
"""

trip_files = glob.glob('d:/Projects/TripwithMe/trip-details-*.html')
for file in trip_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "itinerary-map" not in content:
        content = content.replace('</title>', '</title>\n' + LEAFLET_CSS + LEAFLET_JS)
        # Find where to inject sections. Usually right before </div>\n      <!-- Right Column: Sticky Booking Form
        # Let's just replace the closing tag of the trip-details-content div.
        content = content.replace('        </section>\n      </div>\n\n      <!-- Right Column', '        </section>\n' + SECTIONS_HTML + '      </div>\n\n      <!-- Right Column')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected into {file}")
