CSS_ADDITIONS = """
/* -------------------------------------------
   Creative Form Elements (Glassmorphism)
------------------------------------------- */
.glass-input, .glass-select {
  width: 100%;
  padding: 1.2rem 1.5rem;
  background: rgba(255, 255, 255, 0.6);
  border: 2px solid transparent;
  border-radius: var(--border-radius);
  color: var(--text-dark);
  font-family: inherit;
  font-size: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(10px);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
}

.dark-mode .glass-input, .dark-mode .glass-select {
  background: rgba(30, 41, 59, 0.5);
  border: 2px solid rgba(255, 255, 255, 0.05);
  color: var(--white);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
}

.glass-input:focus, .glass-select:focus {
  outline: none;
  border-color: var(--primary-accent);
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 0 20px rgba(245, 158, 11, 0.15), inset 0 2px 4px rgba(0,0,0,0.05);
  transform: translateY(-2px);
}

.dark-mode .glass-input:focus, .dark-mode .glass-select:focus {
  background: rgba(30, 41, 59, 0.8);
  border-color: var(--primary-accent);
  box-shadow: 0 0 20px rgba(245, 158, 11, 0.2), inset 0 2px 4px rgba(0,0,0,0.2);
}

.glass-input::placeholder {
  color: rgba(100, 116, 139, 0.7);
  transition: opacity 0.3s ease;
}

.dark-mode .glass-input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.glass-input:focus::placeholder {
  opacity: 0.5;
}

/* Button pulse animation for creative touch */
.btn-pulse {
  position: relative;
  overflow: hidden;
}

.btn-pulse::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 150%;
  height: 150%;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform 0.6s ease-out, opacity 0.6s ease-out;
}

.btn-pulse:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: 0s;
}
"""

with open('d:/Projects/TripwithMe/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + CSS_ADDITIONS)
print("Added creative glass-input styles!")
