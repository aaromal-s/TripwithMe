JS_ADDITIONS = """
// -------------------------------------------------------------
// Advanced Feature: Global Search Autocomplete
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('global-search');
  const searchResults = document.getElementById('search-results');
  
  if (searchInput && searchResults) {
    const packages = [
      { title: "Royal Rajasthan Tour", link: "trip-details.html" },
      { title: "Kerala Backwaters", link: "trip-details-kerala.html" },
      { title: "Himalayan Escape", link: "trip-details-himachal.html" },
      { title: "Goa Beach Retreat", link: "trip-details-goa.html" },
      { title: "Spiritual Uttarakhand", link: "trip-details-spiti.html" },
      { title: "Magical Meghalaya", link: "trip-details-northeast.html" },
      { title: "Andaman Islands", link: "trip-details-goa.html" },
      { title: "Kashmir Paradise", link: "trip-details-kashmir.html" },
      { title: "Spiti Valley Expedition", link: "trip-details-spiti.html" },
      { title: "Darjeeling Tea Trails", link: "trip-details-darjeeling.html" },
      { title: "Mystical Sikkim", link: "trip-details-northeast.html" },
      { title: "Heritage of Hampi", link: "trip-details-hampi.html" }
    ];

    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      searchResults.innerHTML = '';
      
      if (query.length < 2) {
        searchResults.style.display = 'none';
        return;
      }
      
      const filtered = packages.filter(p => p.title.toLowerCase().includes(query));
      
      if (filtered.length > 0) {
        searchResults.style.display = 'flex';
        filtered.forEach(p => {
          const item = document.createElement('a');
          item.href = p.link;
          item.textContent = p.title;
          item.style.padding = '0.8rem 1rem';
          item.style.color = 'var(--text-dark)';
          item.style.textDecoration = 'none';
          item.style.borderBottom = '1px solid var(--bg-light)';
          item.onmouseover = () => item.style.background = 'var(--primary-light)';
          item.onmouseout = () => item.style.background = 'transparent';
          searchResults.appendChild(item);
        });
      } else {
        searchResults.style.display = 'none';
      }
    });

    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
        searchResults.style.display = 'none';
      }
    });
  }
});

// -------------------------------------------------------------
// Advanced Feature: Favorites / Wishlist
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  const favoriteBtns = document.querySelectorAll('.favorite-btn');
  
  if (favoriteBtns.length > 0) {
    let wishlist = JSON.parse(localStorage.getItem('tripwithme_wishlist')) || [];
    
    favoriteBtns.forEach(btn => {
      const card = btn.closest('.pkg-card');
      const title = card.querySelector('.pkg-title').innerText;
      
      // Init state
      if (wishlist.some(item => item.title === title)) {
        btn.querySelector('svg').setAttribute('fill', '#ff4757');
      }
      
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const price = card.querySelector('.pkg-price').innerText;
        const img = card.querySelector('.pkg-img').src;
        
        const index = wishlist.findIndex(item => item.title === title);
        
        if (index > -1) {
          // Remove from wishlist
          wishlist.splice(index, 1);
          btn.querySelector('svg').setAttribute('fill', 'none');
        } else {
          // Add to wishlist
          wishlist.push({ title, price, img });
          btn.querySelector('svg').setAttribute('fill', '#ff4757');
        }
        
        localStorage.setItem('tripwithme_wishlist', JSON.stringify(wishlist));
      });
    });
  }
});

// -------------------------------------------------------------
// Advanced Feature: Live Weather API
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  const weatherTemp = document.getElementById('weather-temp');
  if (weatherTemp) {
    // We'll use a generic central India coord for demo if not specified
    const lat = 20.5937;
    const lng = 78.9629;
    
    fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lng}&current_weather=true`)
      .then(res => res.json())
      .then(data => {
        if (data && data.current_weather) {
          weatherTemp.innerText = `${data.current_weather.temperature}°C`;
        } else {
          weatherTemp.innerText = 'N/A';
        }
      })
      .catch(err => {
        console.error("Weather API error", err);
        weatherTemp.innerText = 'Unavailable';
      });
  }
});

// -------------------------------------------------------------
// Advanced Feature: Interactive Image Lightbox
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  const images = document.querySelectorAll('.gallery-grid img');
  if (images.length > 0) {
    // Create Lightbox DOM
    const lightbox = document.createElement('div');
    lightbox.id = 'lightbox-overlay';
    lightbox.style.position = 'fixed';
    lightbox.style.top = '0';
    lightbox.style.left = '0';
    lightbox.style.width = '100vw';
    lightbox.style.height = '100vh';
    lightbox.style.background = 'rgba(0,0,0,0.9)';
    lightbox.style.zIndex = '9999';
    lightbox.style.display = 'none';
    lightbox.style.alignItems = 'center';
    lightbox.style.justifyContent = 'center';
    lightbox.style.cursor = 'zoom-out';
    
    const lightboxImg = document.createElement('img');
    lightboxImg.style.maxWidth = '90%';
    lightboxImg.style.maxHeight = '90%';
    lightboxImg.style.borderRadius = '8px';
    lightboxImg.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
    lightboxImg.style.cursor = 'default';
    
    lightbox.appendChild(lightboxImg);
    document.body.appendChild(lightbox);
    
    images.forEach(img => {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', () => {
        lightboxImg.src = img.src;
        lightbox.style.display = 'flex';
      });
    });
    
    lightbox.addEventListener('click', (e) => {
      if (e.target !== lightboxImg) {
        lightbox.style.display = 'none';
      }
    });
  }
});
"""

with open('d:/Projects/TripwithMe/script.js', 'a', encoding='utf-8') as f:
    f.write("\n" + JS_ADDITIONS)
print("Advanced JS Logic appended!")
