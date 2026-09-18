CSS_ADDITIONS = """
/* Compare Modal Styles */
.compare-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(10, 10, 10, 0.8);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.compare-modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

.compare-modal {
  background: var(--bg-light);
  width: 90%;
  max-width: 1000px;
  border-radius: var(--border-radius);
  padding: 3rem;
  position: relative;
  max-height: 90vh;
  overflow-y: auto;
  transform: translateY(20px);
  transition: transform 0.3s ease;
}

.compare-modal-overlay.active .compare-modal {
  transform: translateY(0);
}

.compare-close-btn {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: none;
  border: none;
  color: var(--text-dark);
  cursor: pointer;
  transition: color 0.3s ease;
}

.compare-close-btn:hover {
  color: var(--primary-accent);
}

.compare-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.compare-col {
  padding: 1.5rem;
  border-radius: var(--border-radius);
  text-align: center;
}

/* Dashboard Styles */
.dashboard-container {
  max-width: 1200px;
  margin: 8rem auto 4rem auto;
  padding: 0 2rem;
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 3rem;
}

.dashboard-sidebar {
  background: var(--white);
  padding: 2rem;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-sm);
  height: fit-content;
}

.user-profile-widget {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid var(--bg-light);
}

.user-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: var(--primary-base);
  color: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: bold;
  margin: 0 auto 1rem auto;
}

.dashboard-nav {
  list-style-type: none;
  padding: 0;
}

.dashboard-nav li {
  margin-bottom: 1rem;
}

.dashboard-nav a {
  display: flex;
  align-items: center;
  gap: 1rem;
  color: var(--text-dark);
  text-decoration: none;
  padding: 0.8rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.dashboard-nav a:hover, .dashboard-nav a.active {
  background: var(--primary-base);
  color: var(--white);
}

.dashboard-content h2 {
  margin-bottom: 2rem;
  color: var(--primary-base);
}

.dashboard-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: var(--white);
  padding: 2rem;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-sm);
  text-align: center;
}

.stat-card h3 {
  font-size: 2.5rem;
  color: var(--primary-accent);
  margin-bottom: 0.5rem;
}

@media (max-width: 768px) {
  .dashboard-container {
    grid-template-columns: 1fr;
  }
  .dashboard-stats {
    grid-template-columns: 1fr;
  }
}
"""

with open('d:/Projects/TripwithMe/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + CSS_ADDITIONS)
print("CSS appended!")
