NEW_PACKAGES = """
        <!-- Card 11 -->
        <div class="pkg-card flip-card-wrapper" data-region="East India" data-style="Adventure">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input type="checkbox" class="compare-checkbox" data-title="Mystical Sikkim" title="Compare" />
              </div>
              <img src="images/sikkim.jpg" alt="Sikkim" class="pkg-img" />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Sikkim
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    7 Days
                  </span>
                </div>
                <h3 class="pkg-title">Mystical Sikkim</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">Rugged mountain passes and stunning lakes.</p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="26000">₹26,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Nathula Pass Visit</li>
                <li>✓ Tsomgo Lake</li>
                <li>✓ Rumtek Monastery</li>
                <li>✓ Teesta River Rafting</li>
                <li>✓ Gangtok Ropeway</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>

        <!-- Card 12 -->
        <div class="pkg-card flip-card-wrapper" data-region="South India" data-style="Heritage & Culture">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <div class="compare-checkbox-container">
                <input type="checkbox" class="compare-checkbox" data-title="Heritage of Hampi" title="Compare" />
              </div>
              <img src="images/hampi.jpg" alt="Hampi" class="pkg-img" />
              <div class="pkg-content">
                <div class="pkg-meta">
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    Karnataka
                  </span>
                  <span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="16" height="16">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    4 Days
                  </span>
                </div>
                <h3 class="pkg-title">Heritage of Hampi</h3>
                <p style="color: var(--text-light); font-size: 0.9rem">Explore the magnificent ruins of Vijayanagara.</p>
                <div class="pkg-footer">
                  <span class="pkg-price" data-base-price="15000">₹15,000</span>
                  <a href="login.html" class="btn btn-primary cta-btn">Book Now</a>
                </div>
              </div>
            </div>
            <div class="flip-card-back">
              <h3>Highlights</h3>
              <ul style="margin: 1rem 0; text-align: left; list-style-type: none">
                <li>✓ Virupaksha Temple</li>
                <li>✓ Vittala Temple Complex</li>
                <li>✓ Matanga Hill Trek</li>
                <li>✓ Coracle Ride</li>
                <li>✓ Elephant Stables</li>
              </ul>
              <a href="trip-details.html" class="btn btn-primary">Full Itinerary</a>
            </div>
          </div>
        </div>
"""

with open('d:/Projects/TripwithMe/packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

if "Mystical Sikkim" not in content:
    new_content = content.replace("      </section>", NEW_PACKAGES + "\n      </section>")
    with open('d:/Projects/TripwithMe/packages.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Added 2 new packages successfully!")
else:
    print("Packages already added.")
