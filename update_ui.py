import re
import os

NEW_HEADER = """    <header class="header glassmorphism">
      <div class="nav-container">
        <a href="index.html" class="logo">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="var(--primary-accent)"
            width="32"
            height="32"
            class="logo-icon"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"
            />
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
          <li><a href="#" class="nav-link">About Us</a></li>
          <li><a href="#" class="nav-link">Contact</a></li>
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
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z"/>
            </svg>
          </label>
          <button type="button" class="btn btn-primary cta-btn">Book Now</button>
        </div>
      </div>
    </header>"""

NEW_FOOTER = """    <footer class="footer creative-footer">
      <div class="footer-grid">
        <div class="footer-col brand-col">
          <a href="index.html" class="logo footer-logo">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="var(--primary-accent)" width="32" height="32">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"/>
            </svg>
            Tripwith<span>Me</span>
          </a>
          <p class="footer-tagline">Your trusted partner for discovering the incredible diversity and beauty of India.</p>
          <div class="social-links">
            <a href="#" aria-label="Facebook"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
            <a href="#" aria-label="Instagram"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
            <a href="#" aria-label="Twitter"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path></svg></a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul class="footer-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="packages.html">All Packages</a></li>
            <li><a href="#">Travel Guides</a></li>
            <li><a href="#">Contact Support</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Top Destinations</h4>
          <ul class="footer-links">
            <li><a href="trip-details.html">Rajasthan Royals</a></li>
            <li><a href="trip-details.html">Kerala Backwaters</a></li>
            <li><a href="#">Spiti Valley</a></li>
            <li><a href="#">Andaman Islands</a></li>
          </ul>
        </div>
        <div class="footer-col newsletter-col">
          <h4>Newsletter</h4>
          <p>Subscribe for travel tips and exclusive offers.</p>
          <form class="newsletter-form">
            <div class="input-group">
              <input type="email" placeholder="Your email address" required />
              <button type="submit" class="btn btn-primary">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
              </button>
            </div>
          </form>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 TripwithMe. Crafted with <span style="color:var(--primary-accent)">♥</span> for travelers.</p>
      </div>
    </footer>"""

CSS_ADDITIONS = """
/* --- Creative Header & Footer Enhancements --- */

/* Glassmorphism Header */
.header.glassmorphism {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  transition: all 0.4s ease;
}

:root[data-theme="dark"] .header.glassmorphism {
  background: rgba(18, 18, 18, 0.85);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.logo-icon {
  transition: transform 0.3s ease;
}
.logo:hover .logo-icon {
  transform: rotate(20deg);
}

/* Nav Links Underline Effect */
.nav-links {
  align-items: center;
}
.nav-link {
  position: relative;
  padding: 0.5rem 0;
}
.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: var(--primary-accent);
  transition: width 0.3s ease;
}
.nav-link:hover::after {
  width: 100%;
}

/* Header Controls */
.header-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.glass-select {
  background: transparent;
  border: 1px solid rgba(0,0,0,0.1);
  padding: 0.4rem;
  border-radius: 6px;
  color: var(--text-dark);
  cursor: pointer;
}
:root[data-theme="dark"] .glass-select {
  border-color: rgba(255,255,255,0.2);
}
.glass-select:focus {
  outline: none;
  border-color: var(--primary-accent);
}

.theme-toggle-label {
  padding: 0.4rem;
  border-radius: 50%;
  background: rgba(0,0,0,0.05);
  transition: background 0.3s ease;
}
:root[data-theme="dark"] .theme-toggle-label {
  background: rgba(255,255,255,0.1);
}
.theme-toggle-label:hover {
  background: rgba(0,0,0,0.1);
}
:root[data-theme="dark"] .theme-toggle-label:hover {
  background: rgba(255,255,255,0.2);
}

.cta-btn {
  padding: 0.6rem 1.5rem;
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Creative Footer */
.creative-footer {
  background: linear-gradient(135deg, var(--primary-base) 0%, #044a3f 100%);
  color: #e0e6ed;
  padding: 5rem 2rem 2rem;
  margin-top: 5rem;
  position: relative;
}

:root[data-theme="dark"] .creative-footer {
  background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
  border-top: 1px solid #333;
}

.footer-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

@media (max-width: 992px) {
  .footer-grid {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 576px) {
  .footer-grid {
    grid-template-columns: 1fr;
  }
}

.footer-logo {
  color: var(--white) !important;
  margin-bottom: 1.5rem;
}

.footer-tagline {
  line-height: 1.8;
  margin-bottom: 2rem;
  opacity: 0.85;
}

.social-links {
  display: flex;
  gap: 1rem;
}
.social-links a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  color: var(--white);
  transition: all 0.3s ease;
}
.social-links a:hover {
  background: var(--primary-accent);
  transform: translateY(-3px);
}

.footer-col h4 {
  color: var(--white);
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  position: relative;
  padding-bottom: 0.5rem;
}
.footer-col h4::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 40px;
  height: 2px;
  background: var(--primary-accent);
}

.footer-links li {
  margin-bottom: 0.8rem;
}
.footer-links a {
  color: #e0e6ed;
  opacity: 0.8;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
}
.footer-links a::before {
  content: '›';
  margin-right: 8px;
  color: var(--primary-accent);
  font-size: 1.2rem;
  opacity: 0;
  transform: translateX(-10px);
  transition: all 0.3s ease;
}
.footer-links a:hover {
  opacity: 1;
  color: var(--white);
  padding-left: 5px;
}
.footer-links a:hover::before {
  opacity: 1;
  transform: translateX(0);
}

.newsletter-col p {
  margin-bottom: 1.5rem;
  opacity: 0.85;
}

.input-group {
  display: flex;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 30px;
  padding: 0.3rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.input-group input {
  background: transparent;
  border: none;
  padding: 0.8rem 1.2rem;
  color: var(--white);
  width: 100%;
  outline: none;
}
.input-group input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}
.input-group button {
  border-radius: 50%;
  width: 45px;
  height: 45px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
  padding-top: 2rem;
  opacity: 0.7;
  font-size: 0.9rem;
}
"""

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match the entire header
    header_pattern = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
    if header_pattern.search(content):
        content = header_pattern.sub(NEW_HEADER, content)
    
    # Regex to match the entire footer
    footer_pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(NEW_FOOTER, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in ['index.html', 'packages.html', 'trip-details.html']:
    if os.path.exists(html_file):
        replace_in_file(html_file)

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'Creative Header & Footer Enhancements' not in css_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(CSS_ADDITIONS)
