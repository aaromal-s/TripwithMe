CSS_ADDITIONS = """
/* About Us Styles */
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  padding: 0 2rem;
}

.team-card {
  padding: 2.5rem 1.5rem;
  text-align: center;
  border-radius: var(--border-radius);
  transition: transform 0.3s ease;
}

.team-card:hover {
  transform: translateY(-5px);
}

.team-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: var(--primary-base);
  color: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  font-weight: bold;
  margin: 0 auto 1.5rem auto;
  box-shadow: var(--shadow-sm);
}

.team-role {
  color: var(--primary-accent);
  font-weight: bold;
  margin-top: 0.5rem;
}

/* Contact Styles */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}

@media (max-width: 768px) {
  .contact-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open('d:/Projects/TripwithMe/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + CSS_ADDITIONS)
print("CSS for About and Contact appended!")
