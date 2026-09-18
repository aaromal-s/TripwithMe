ABOUT_HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About Us - TripwithMe</title>
    <meta name="description" content="Learn about TripwithMe's mission to provide unforgettable Indian travel experiences." />
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <!-- Preloader -->
    <div id="preloader" class="preloader">
      <svg class="loader-plane" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="60" height="60">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
      </svg>
    </div>

    <!-- Header -->
    <header class="header glassmorphism">
      <div class="nav-container">
        <a href="index.html" class="logo">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="var(--primary-accent)" width="32" height="32" class="logo-icon">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418" />
          </svg>
          Tripwith<span>Me</span>
        </a>

        <input type="checkbox" id="menu-toggle" />
        <label for="menu-toggle" class="menu-btn">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" width="28" height="28">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        </label>

        <ul class="nav-links">
          <li><a href="index.html" class="nav-link">Home</a></li>
          <li><a href="packages.html" class="nav-link">Destinations</a></li>
          <li><a href="about.html" class="nav-link active">About Us</a></li>
          <li><a href="contact.html" class="nav-link">Contact</a></li>
        </ul>

        <div class="header-controls">
          <select id="currency-select" aria-label="Currency" class="glass-select">
            <option value="INR">INR ₹</option>
            <option value="USD">USD $</option>
            <option value="EUR">EUR €</option>
          </select>
          <label style="display: flex; align-items: center; cursor: pointer" title="Toggle Dark Mode" class="theme-toggle-label">
            <input type="checkbox" id="theme-toggle" style="display: none" />
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="20" height="20" class="theme-icon">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
            </svg>
          </label>
          <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
        </div>
      </div>
    </header>

    <!-- Page Banner -->
    <div class="page-header parallax-bg" style="background-image: url('images/hero-bg.jpg');">
      <h1>About Us</h1>
    </div>

    <!-- Main Content -->
    <main class="container" style="margin-top: 4rem; margin-bottom: 4rem;">
      <!-- Our Story -->
      <section class="glassmorphism" style="padding: 3rem; margin-bottom: 4rem; border-radius: var(--border-radius);">
        <div style="text-align: center; max-width: 800px; margin: 0 auto;">
          <h2 style="color: var(--primary-base); margin-bottom: 1.5rem; font-size: 2.5rem;">Our Mission</h2>
          <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-dark);">
            At TripwithMe, we believe travel is more than just visiting places; it's about experiencing the soul of a destination. Founded by passionate explorers, our mission is to curate authentic, premium, and unforgettable journeys across the incredible landscapes of India. From the snow-capped peaks of the Himalayas to the tranquil backwaters of Kerala, we connect you with the heart of every culture.
          </p>
        </div>
      </section>

      <!-- Why Choose Us -->
      <section style="margin-bottom: 4rem;">
        <h2 style="text-align: center; color: var(--primary-base); margin-bottom: 3rem; font-size: 2.2rem;">Why Choose Us</h2>
        <div class="grid-3">
          <div class="glassmorphism" style="padding: 2.5rem; text-align: center; border-radius: var(--border-radius);">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="var(--primary-accent)" width="48" height="48" style="margin-bottom: 1.5rem;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 0 1 1.04 0l2.125 5.111a.563.563 0 0 0 .475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 0 0-.182.557l1.285 5.385a.562.562 0 0 1-.84.61l-4.725-2.885a.562.562 0 0 0-.586 0L6.982 20.54a.562.562 0 0 1-.84-.61l1.285-5.386a.562.562 0 0 0-.182-.557l-4.204-3.602a.562.562 0 0 1 .321-.988l5.518-.442a.563.563 0 0 0 .475-.345L11.48 3.5Z" />
            </svg>
            <h3 style="margin-bottom: 1rem; color: var(--text-dark);">Curated Experiences</h3>
            <p style="color: var(--text-light);">We handpick every hotel, guide, and activity to ensure you get nothing but the absolute best quality.</p>
          </div>
          <div class="glassmorphism" style="padding: 2.5rem; text-align: center; border-radius: var(--border-radius);">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="var(--primary-accent)" width="48" height="48" style="margin-bottom: 1.5rem;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
              <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
            </svg>
            <h3 style="margin-bottom: 1rem; color: var(--text-dark);">Local Experts</h3>
            <p style="color: var(--text-light);">Travel with confidence knowing our guides are passionate locals who know the hidden gems.</p>
          </div>
          <div class="glassmorphism" style="padding: 2.5rem; text-align: center; border-radius: var(--border-radius);">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="var(--primary-accent)" width="48" height="48" style="margin-bottom: 1.5rem;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-2.896-1.596-5.48-4.18-7.076-7.076l1.293-.97c.362-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
            </svg>
            <h3 style="margin-bottom: 1rem; color: var(--text-dark);">24/7 Support</h3>
            <p style="color: var(--text-light);">From the moment you book until you return home, our support team is always just a call away.</p>
          </div>
        </div>
      </section>

      <!-- Our Team -->
      <section>
        <h2 style="text-align: center; color: var(--primary-base); margin-bottom: 3rem; font-size: 2.2rem;">Meet The Team</h2>
        <div class="team-grid">
          <div class="team-card glassmorphism">
            <div class="team-avatar">JD</div>
            <h3>Jane Doe</h3>
            <p class="team-role">Founder & CEO</p>
          </div>
          <div class="team-card glassmorphism">
            <div class="team-avatar" style="background: var(--primary-accent);">MR</div>
            <h3>Mark Ruffalo</h3>
            <p class="team-role">Head of Experiences</p>
          </div>
          <div class="team-card glassmorphism">
            <div class="team-avatar" style="background: #10b981;">SK</div>
            <h3>Sarah Khan</h3>
            <p class="team-role">Lead Guide</p>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-bottom">
        <p>&copy; 2026 TripwithMe. Crafted with <span style="color: var(--primary-accent)">♥</span> for travelers.</p>
      </div>
    </footer>
  </body>
</html>
"""

with open('d:/Projects/TripwithMe/about.html', 'w', encoding='utf-8') as f:
    f.write(ABOUT_HTML)
print("about.html created!")
