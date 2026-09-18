document.addEventListener("DOMContentLoaded", () => {
  // 1. Theme/Dark Mode Toggle
  const themeToggle = document.getElementById("theme-toggle");
  if (themeToggle) {
    // Check local storage for theme
    const currentTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", currentTheme);
    themeToggle.checked = currentTheme === "dark";

    themeToggle.addEventListener("change", (e) => {
      const newTheme = e.target.checked ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme);
    });
  }

  // 2. Sticky Header Effect
  const header = document.querySelector(".header");
  if (header) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 50) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }
    });
  }

  // 3. Currency Converter Logic
  const currencySelect = document.getElementById("currency-select");
  const priceElements = document.querySelectorAll(".pkg-price, .price-tag");

  // Base prices are in INR. Rates for demo purposes.
  const rates = {
    INR: { symbol: "₹", rate: 1 },
    USD: { symbol: "$", rate: 0.012 },
    EUR: { symbol: "€", rate: 0.011 },
  };

  if (currencySelect) {
    currencySelect.addEventListener("change", (e) => {
      const currency = e.target.value;
      const { symbol, rate } = rates[currency];

      priceElements.forEach((el) => {
        const basePrice = parseInt(el.getAttribute("data-base-price"));
        if (basePrice) {
          const converted = Math.round(basePrice * rate).toLocaleString(
            "en-IN",
          );
          if (el.classList.contains("price-tag")) {
            el.innerHTML = `${symbol}${converted} <span>/ person</span>`;
          } else {
            el.textContent = `${symbol}${converted}`;
          }
        }
      });
    });
  }

  // 4. "Surprise Me" Logic
  const surpriseBtn = document.getElementById("surprise-btn");
  const destinations = ["trip-details.html", "packages.html"]; // could expand with more trips
  if (surpriseBtn) {
    surpriseBtn.addEventListener("click", () => {
      surpriseBtn.classList.add("spin-anim");
      setTimeout(() => {
        const randomDest =
          destinations[Math.floor(Math.random() * destinations.length)];
        window.location.href = randomDest;
      }, 500);
    });
  }

  // 5. Live Sidebar Filtering (Packages Page)
  const filterCheckboxes = document.querySelectorAll(
    '.sidebar input[type="checkbox"]',
  );
  const packageCards = document.querySelectorAll(".package-grid .pkg-card");

  if (filterCheckboxes.length > 0 && packageCards.length > 0) {
    filterCheckboxes.forEach((cb) => {
      cb.addEventListener("change", () => {
        const checkedRegions = Array.from(
          document.querySelectorAll(".filter-group:nth-child(1) input:checked"),
        ).map((cb) => cb.value);
        const checkedStyles = Array.from(
          document.querySelectorAll(".filter-group:nth-child(2) input:checked"),
        ).map((cb) => cb.value);

        packageCards.forEach((card) => {
          const region = card.getAttribute("data-region");
          const style = card.getAttribute("data-style");

          const regionMatch =
            checkedRegions.length === 0 || checkedRegions.includes(region);
          const styleMatch =
            checkedStyles.length === 0 || checkedStyles.includes(style);

          if (regionMatch && styleMatch) {
            card.style.display = "block";
          } else {
            card.style.display = "none";
          }
        });
      });
    });
  }

  // 6. Compare Packages Bar (Packages Page)
  const compareCheckboxes = document.querySelectorAll(".compare-checkbox");
  const compareBar = document.getElementById("compare-bar");
  const compareCount = document.getElementById("compare-count");
  let selectedForCompare = [];

  if (compareCheckboxes.length > 0 && compareBar) {
    compareCheckboxes.forEach((cb) => {
      cb.addEventListener("change", (e) => {
        const pkgTitle = e.target.getAttribute("data-title");
        if (e.target.checked) {
          if (selectedForCompare.length < 3) {
            selectedForCompare.push(pkgTitle);
          } else {
            e.target.checked = false;
            alert("You can only compare up to 3 packages.");
          }
        } else {
          selectedForCompare = selectedForCompare.filter((t) => t !== pkgTitle);
        }

        if (selectedForCompare.length > 0) {
          compareBar.classList.add("visible");
          compareCount.textContent = selectedForCompare.length;
        } else {
          compareBar.classList.remove("visible");
        }
      });
    });
  }

  // 7. Multi-Step Booking Wizard & Dynamic Price (Trip Details)
  let currentStep = 1;
  const nextBtns = document.querySelectorAll(".next-step");
  const prevBtns = document.querySelectorAll(".prev-step");
  const steps = document.querySelectorAll(".wizard-step");
  const guestSelect = document.getElementById("guests");
  const basePriceEl = document.getElementById("total-price");

  if (steps.length > 0) {
    const updateSteps = () => {
      steps.forEach((step, index) => {
        if (index + 1 === currentStep) {
          step.classList.add("active");
        } else {
          step.classList.remove("active");
        }
      });
    };

    nextBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        // simple validation simulation
        if (currentStep < steps.length) {
          currentStep++;
          updateSteps();
        }
      });
    });

    prevBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        if (currentStep > 1) {
          currentStep--;
          updateSteps();
        }
      });
    });
  }

  if (guestSelect && basePriceEl) {
    const baseCost = parseInt(basePriceEl.getAttribute("data-base-price"));
    guestSelect.addEventListener("change", (e) => {
      const count = parseInt(e.target.value);
      const total = count * baseCost;

      // Reapply currency if needed, assuming INR for simplicity here unless extended
      basePriceEl.textContent = "₹" + total.toLocaleString("en-IN");
    });
  }

  // 11. Authentication Page Logic (Login/Register Split Screen)
  const authSlider = document.querySelectorAll(".slider-slide");
  if (authSlider.length > 0) {
    let currentSlide = 0;
    setInterval(() => {
      authSlider[currentSlide].classList.remove("active");
      currentSlide = (currentSlide + 1) % authSlider.length;
      authSlider[currentSlide].classList.add("active");
    }, 5000); // Change image every 5 seconds
  }

  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");
  const showRegisterBtn = document.getElementById("show-register");
  const showLoginBtn = document.getElementById("show-login");

  if (loginForm && registerForm && showRegisterBtn && showLoginBtn) {
    showRegisterBtn.addEventListener("click", (e) => {
      e.preventDefault();
      loginForm.classList.remove("active");
      registerForm.classList.add("active");
    });

    showLoginBtn.addEventListener("click", (e) => {
      e.preventDefault();
      registerForm.classList.remove("active");
      loginForm.classList.add("active");
    });
  }
});

// --- Preloader ---
window.addEventListener("load", () => {
  const preloader = document.getElementById("preloader");
  if (preloader) {
    setTimeout(() => {
      preloader.classList.add("hidden");
    }, 800);
  }
});

// --- Custom Cursor ---
const cursor = document.createElement("div");
cursor.className = "custom-cursor";
const follower = document.createElement("div");
follower.className = "cursor-follower";
document.body.appendChild(cursor);
document.body.appendChild(follower);

let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;
let followerX = mouseX;
let followerY = mouseY;

document.addEventListener("mousemove", (e) => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  cursor.style.left = mouseX + "px";
  cursor.style.top = mouseY + "px";
});

// Smooth follower animation
function animateFollower() {
  followerX += (mouseX - followerX) * 0.15;
  followerY += (mouseY - followerY) * 0.15;
  follower.style.left = followerX + "px";
  follower.style.top = followerY + "px";
  requestAnimationFrame(animateFollower);
}
animateFollower();

// Cursor Hover Effects
const interactiveElements = document.querySelectorAll(
  "a, button, input, select, .map-pin, .state-card, .pkg-card",
);
interactiveElements.forEach((el) => {
  el.addEventListener("mouseenter", () =>
    document.body.classList.add("cursor-hover"),
  );
  el.addEventListener("mouseleave", () =>
    document.body.classList.remove("cursor-hover"),
  );
});

// --- Scroll-Triggered Animations (AOS) ---
const observerOptions = {
  root: null,
  rootMargin: "0px",
  threshold: 0.15,
};

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll(".fade-in").forEach((el) => observer.observe(el));

// --- Typewriter Effect ---
const typewriterText = document.querySelector(".typewriter-text");
if (typewriterText) {
  const words = ["Kerala", "Rajasthan", "Goa", "Himachal", "India"];
  let wordIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typeSpeed = 150;

  function type() {
    const currentWord = words[wordIndex];

    if (isDeleting) {
      typewriterText.textContent = currentWord.substring(0, charIndex - 1);
      charIndex--;
      typeSpeed = 50;
    } else {
      typewriterText.textContent = currentWord.substring(0, charIndex + 1);
      charIndex++;
      typeSpeed = 150;
    }

    if (!isDeleting && charIndex === currentWord.length) {
      typeSpeed = 2000; // Pause at end
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      typeSpeed = 500; // Pause before new word
    }

    setTimeout(type, typeSpeed);
  }

  // Start typing
  setTimeout(type, 1000);
}


// -------------------------------------------------------------
// Packages Filtering Logic
// -------------------------------------------------------------
const filterCheckboxes = document.querySelectorAll('.sidebar input[type="checkbox"]');
const packageCards = document.querySelectorAll('.pkg-card');

if (filterCheckboxes.length > 0 && packageCards.length > 0) {
  filterCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', filterPackages);
  });
}

function filterPackages() {
  // Get active region filters
  const regionFilters = Array.from(document.querySelectorAll('.filter-group:nth-child(1) input:checked')).map(cb => cb.value);
  // Get active style filters
  const styleFilters = Array.from(document.querySelectorAll('.filter-group:nth-child(2) input:checked')).map(cb => cb.value);

  packageCards.forEach(card => {
    const cardRegion = card.getAttribute('data-region');
    const cardStyle = card.getAttribute('data-style');

    const matchesRegion = regionFilters.length === 0 || regionFilters.includes(cardRegion);
    const matchesStyle = styleFilters.length === 0 || styleFilters.includes(cardStyle);

    if (matchesRegion && matchesStyle) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

// -------------------------------------------------------------
// Compare Logic
// -------------------------------------------------------------
const compareCheckboxes = document.querySelectorAll('.compare-checkbox');
const compareBar = document.getElementById('compare-bar');
const compareCountSpan = document.getElementById('compare-count');
const compareBtn = compareBar ? compareBar.querySelector('button') : null;
const compareModalOverlay = document.getElementById('compare-modal-overlay');
const compareCloseBtn = document.getElementById('compare-close-btn');
const compareGrid = document.getElementById('compare-grid');

let selectedForCompare = [];

if (compareCheckboxes.length > 0) {
  compareCheckboxes.forEach(cb => {
    cb.addEventListener('change', (e) => {
      const card = e.target.closest('.pkg-card');
      const title = card.querySelector('.pkg-title').innerText;
      const price = card.querySelector('.pkg-price').innerText;
      const img = card.querySelector('.pkg-img').src;
      const highlights = Array.from(card.querySelectorAll('.flip-card-back li')).map(li => li.innerText);

      if (e.target.checked) {
        if (selectedForCompare.length >= 3) {
          alert('You can only compare up to 3 packages at a time.');
          e.target.checked = false;
          return;
        }
        selectedForCompare.push({ title, price, img, highlights });
      } else {
        selectedForCompare = selectedForCompare.filter(item => item.title !== title);
      }

      updateCompareBar();
    });
  });
}

function updateCompareBar() {
  if (!compareBar) return;
  compareCountSpan.innerText = selectedForCompare.length;
  if (selectedForCompare.length > 0) {
    compareBar.classList.add('visible');
  } else {
    compareBar.classList.remove('visible');
  }
}

if (compareBtn && compareModalOverlay) {
  compareBtn.addEventListener('click', () => {
    populateCompareModal();
    compareModalOverlay.classList.add('active');
  });
}

if (compareCloseBtn && compareModalOverlay) {
  compareCloseBtn.addEventListener('click', () => {
    compareModalOverlay.classList.remove('active');
  });
  compareModalOverlay.addEventListener('click', (e) => {
    if (e.target === compareModalOverlay) {
      compareModalOverlay.classList.remove('active');
    }
  });
}

function populateCompareModal() {
  if (!compareGrid) return;
  compareGrid.innerHTML = '';
  
  selectedForCompare.forEach(pkg => {
    const col = document.createElement('div');
    col.className = 'compare-col glassmorphism';
    col.innerHTML = `
      <img src="${pkg.img}" alt="${pkg.title}" style="width:100%; border-radius: 8px; margin-bottom: 1rem;" />
      <h3 style="color:var(--primary-accent); margin-bottom: 0.5rem;">${pkg.title}</h3>
      <div style="font-size: 1.2rem; font-weight: bold; margin-bottom: 1rem;">${pkg.price}</div>
      <ul style="list-style-type:none; padding:0; text-align:left;">
        ${pkg.highlights.map(h => `<li style="margin-bottom:0.5rem; font-size:0.9rem;">${h}</li>`).join('')}
      </ul>
    `;
    compareGrid.appendChild(col);
  });
}


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
