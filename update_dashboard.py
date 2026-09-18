import re

# 1. Update dashboard.html to add a container for Wishlist and logic
with open('d:/Projects/TripwithMe/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

WISHLIST_HTML = """
        <h3 style="margin-top:4rem; margin-bottom:1.5rem; color:var(--text-dark);">Your Wishlist</h3>
        <div id="dashboard-wishlist" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 2rem;">
          <!-- Populated by JS -->
        </div>

        <script>
          document.addEventListener('DOMContentLoaded', () => {
            const wishlistContainer = document.getElementById('dashboard-wishlist');
            if (wishlistContainer) {
              const wishlist = JSON.parse(localStorage.getItem('tripwithme_wishlist')) || [];
              if (wishlist.length === 0) {
                wishlistContainer.innerHTML = '<p style="color:var(--text-light);">Your wishlist is empty. Explore our destinations to add some!</p>';
              } else {
                wishlist.forEach(item => {
                  const card = document.createElement('div');
                  card.className = 'glassmorphism';
                  card.style.padding = '1.5rem';
                  card.style.borderRadius = 'var(--border-radius)';
                  card.innerHTML = `
                    <img src="${item.img}" alt="${item.title}" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;" />
                    <h4 style="color:var(--text-dark); margin-bottom: 0.5rem;">${item.title}</h4>
                    <div style="color:var(--primary-accent); font-weight: bold; margin-bottom: 1rem;">${item.price}</div>
                    <button class="btn btn-outline" style="width: 100%;" onclick="alert('Removed from wishlist'); location.reload(); localStorage.setItem('tripwithme_wishlist', JSON.stringify(JSON.parse(localStorage.getItem('tripwithme_wishlist')).filter(w => w.title !== '${item.title}')))">Remove</button>
                  `;
                  wishlistContainer.appendChild(card);
                });
              }
            }
          });
        </script>
"""

if 'dashboard-wishlist' not in content:
    content = content.replace('      </section>', WISHLIST_HTML + '\n      </section>')
    with open('d:/Projects/TripwithMe/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Add Lightbox hover class to CSS
CSS_ADDITIONS = """
/* Lightbox Image Hover */
.gallery-grid img {
  transition: transform 0.3s ease;
}
.gallery-grid img:hover {
  transform: scale(1.02);
  box-shadow: var(--shadow-md);
}
"""

with open('d:/Projects/TripwithMe/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + CSS_ADDITIONS)

# 3. Ensure gallery images in trip-details have the correct class if missing (they already have .gallery-grid img selector in JS)

print("Dashboard Wishlist and CSS updated!")
