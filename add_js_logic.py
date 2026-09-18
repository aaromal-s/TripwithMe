SCRIPT_ADDITIONS = """
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
"""

with open('d:/Projects/TripwithMe/script.js', 'a', encoding='utf-8') as f:
    f.write("\n" + SCRIPT_ADDITIONS)
print("JS logic appended!")
