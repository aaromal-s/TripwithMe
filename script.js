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
  const authSlider = document.querySelectorAll('.slider-slide');
  if (authSlider.length > 0) {
    let currentSlide = 0;
    setInterval(() => {
      authSlider[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % authSlider.length;
      authSlider[currentSlide].classList.add('active');
    }, 5000); // Change image every 5 seconds
  }

  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const showRegisterBtn = document.getElementById('show-register');
  const showLoginBtn = document.getElementById('show-login');

  if (loginForm && registerForm && showRegisterBtn && showLoginBtn) {
    showRegisterBtn.addEventListener('click', (e) => {
      e.preventDefault();
      loginForm.classList.remove('active');
      registerForm.classList.add('active');
    });

    showLoginBtn.addEventListener('click', (e) => {
      e.preventDefault();
      registerForm.classList.remove('active');
      loginForm.classList.add('active');
    });
  }
});
