CSS_ADDITIONS = """
/* Reviews & Maps Styles */
.review-card {
  transition: transform 0.3s ease;
}

.review-card:hover {
  transform: translateY(-2px);
}

.leaflet-container {
  font-family: inherit;
  z-index: 1;
}
"""

JS_ADDITIONS = """
// -------------------------------------------------------------
// Interactive Map (Leaflet.js)
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  const mapContainer = document.getElementById('itinerary-map');
  // Check if map container exists and Leaflet is loaded
  if (mapContainer && typeof L !== 'undefined') {
    // Initialize map centered roughly around Rajasthan (Jaipur)
    const map = L.map('itinerary-map').setView([26.9124, 75.7873], 7);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add markers for the itinerary
    const locations = [
      { name: "Jaipur", coords: [26.9124, 75.7873] },
      { name: "Jodhpur", coords: [26.2389, 73.0243] },
      { name: "Udaipur", coords: [24.5854, 73.7125] }
    ];

    const latlngs = [];
    locations.forEach(loc => {
      const marker = L.marker(loc.coords).addTo(map);
      marker.bindPopup(`<b>${loc.name}</b>`).openPopup();
      latlngs.push(loc.coords);
    });

    // Draw a line connecting the locations
    const polyline = L.polyline(latlngs, { color: 'var(--primary-base)', weight: 4 }).addTo(map);
    map.fitBounds(polyline.getBounds(), { padding: [50, 50] });
  }

  // -------------------------------------------------------------
  // Reviews Submission Logic
  // -------------------------------------------------------------
  const reviewForm = document.getElementById('review-form');
  const reviewsList = document.getElementById('reviews-list');

  if (reviewForm && reviewsList) {
    reviewForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('reviewer-name').value;
      const rating = parseInt(document.getElementById('review-rating').value);
      const text = document.getElementById('review-text').value;
      
      const initials = name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
      const stars = '★'.repeat(rating) + '☆'.repeat(5 - rating);

      const newReview = document.createElement('div');
      newReview.className = 'review-card glassmorphism';
      newReview.style.padding = '1.5rem';
      newReview.style.display = 'flex';
      newReview.style.gap = '1rem';
      newReview.style.alignItems = 'flex-start';

      newReview.innerHTML = `
        <div class="user-avatar" style="width: 50px; height: 50px; font-size: 1.2rem; flex-shrink: 0;">${initials}</div>
        <div>
          <h4 style="margin-bottom: 0.2rem;">${name}</h4>
          <div style="color: #f59e0b; font-size: 1.2rem; margin-bottom: 0.5rem;">${stars}</div>
          <p style="color: var(--text-dark);">${text}</p>
        </div>
      `;

      // Insert at the top
      reviewsList.insertBefore(newReview, reviewsList.firstChild);
      reviewForm.reset();
    });
  }
});
"""

with open('d:/Projects/TripwithMe/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + CSS_ADDITIONS)

with open('d:/Projects/TripwithMe/script.js', 'a', encoding='utf-8') as f:
    f.write("\n" + JS_ADDITIONS)

print("JS and CSS for Map/Reviews appended!")
