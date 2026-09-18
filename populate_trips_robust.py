import re
import os

destinations = {
    'goa': {
        'subtitle': '<p>4 Days / 3 Nights &bull; North & South Goa</p>',
        'description': '<p>\n            Experience the ultimate tropical getaway with pristine beaches, vibrant nightlife, and Portuguese heritage. This 4-day Goa retreat is perfect for relaxation and thrill-seekers alike.\n          </p>',
        'image': 'images/goa.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Arrival & North Goa</div>
                <div class="timeline-content">
                  <h4>Beaches & Nightlife</h4>
                  <p>Check into your beachfront resort. Spend the evening relaxing at Baga Beach and enjoying the local seafood shacks.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2: Old Goa & Culture</div>
                <div class="timeline-content">
                  <h4>Portuguese Heritage</h4>
                  <p>Visit the Basilica of Bom Jesus, Se Cathedral, and explore the Latin Quarter of Fontainhas.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 3: South Goa & Water Sports</div>
                <div class="timeline-content">
                  <h4>Thrill & Serenity</h4>
                  <p>Enjoy water sports like parasailing and jet skiing. Evening sunset cruise on the Mandovi River.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4: Departure</div>
                <div class="timeline-content">
                  <h4>Farewell Goa</h4>
                  <p>Enjoy a final morning by the pool before heading to the airport for your onward journey.</p>
                </div>
              </div>
            </div>'''
    },
    'kerala': {
        'subtitle': '<p>6 Days / 5 Nights &bull; Munnar, Alleppey, Kochi</p>',
        'description': '<p>\n            Journey through "God\'s Own Country" exploring lush tea plantations, serene backwaters, and pristine beaches in this unforgettable 6-day Kerala experience.\n          </p>',
        'image': 'images/kerala.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Arrival in Kochi</div>
                <div class="timeline-content">
                  <h4>Historic Port City</h4>
                  <p>Explore Fort Kochi, the Chinese Fishing Nets, and enjoy an evening Kathakali dance performance.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2-3: Munnar</div>
                <div class="timeline-content">
                  <h4>Tea Plantations & Waterfalls</h4>
                  <p>Drive to Munnar. Visit the Eravikulam National Park, Mattupetty Dam, and sprawling tea estates.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4: Alleppey Houseboat</div>
                <div class="timeline-content">
                  <h4>Serene Backwaters</h4>
                  <p>Board a traditional Kettuvallam houseboat. Cruise through the palm-fringed canals while enjoying authentic Kerala cuisine.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 5-6: Departure</div>
                <div class="timeline-content">
                  <h4>Farewell Kerala</h4>
                  <p>Disembark the houseboat and transfer to Cochin airport with beautiful memories.</p>
                </div>
              </div>
            </div>'''
    },
    'himachal': {
        'subtitle': '<p>6 Days / 5 Nights &bull; Shimla, Manali</p>',
        'description': '<p>\n            Escape to the majestic Himalayas. Experience snow-capped peaks, pine forests, and thrilling adventure sports in this beautiful Himachal Pradesh tour.\n          </p>',
        'image': 'images/himachal.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1-2: Shimla</div>
                <div class="timeline-content">
                  <h4>The Queen of Hills</h4>
                  <p>Stroll along the Ridge and Mall Road. Visit Jakhoo Temple and enjoy panoramic views of the valley.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 3: Journey to Manali</div>
                <div class="timeline-content">
                  <h4>Scenic Drive</h4>
                  <p>Drive through Kullu Valley. Stop by the Beas River and visit shawl weaving factories.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4-5: Manali & Rohtang Pass</div>
                <div class="timeline-content">
                  <h4>Snow & Adventure</h4>
                  <p>Full day excursion to Solang Valley or Rohtang Pass (subject to weather). Enjoy snow activities and stunning vistas.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 6: Departure</div>
                <div class="timeline-content">
                  <h4>Homeward Bound</h4>
                  <p>Depart from Manali with breathtaking mountain memories.</p>
                </div>
              </div>
            </div>'''
    },
    'kashmir': {
        'subtitle': '<p>5 Days / 4 Nights &bull; Srinagar, Gulmarg, Pahalgam</p>',
        'description': '<p>\n            Experience "Paradise on Earth." Stay on a romantic Shikara on Dal Lake, ride the Gulmarg Gondola, and witness the stunning valleys of Kashmir.\n          </p>',
        'image': 'images/kashmir.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Srinagar Arrival</div>
                <div class="timeline-content">
                  <h4>Houseboat & Shikara</h4>
                  <p>Check into a premium houseboat. Enjoy a sunset Shikara ride on the serene Dal Lake.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2: Gulmarg Excursion</div>
                <div class="timeline-content">
                  <h4>The Meadow of Flowers</h4>
                  <p>Take the famous Gondola ride to Phase 2 for breathtaking views of the Apharwat Peak.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 3-4: Pahalgam & Gardens</div>
                <div class="timeline-content">
                  <h4>Valleys & Saffron</h4>
                  <p>Visit the lush Betaab Valley, Aru Valley, and the historic Mughal Gardens in Srinagar.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 5: Departure</div>
                <div class="timeline-content">
                  <h4>Farewell Kashmir</h4>
                  <p>Transfer to Srinagar Airport to conclude your heavenly journey.</p>
                </div>
              </div>
            </div>'''
    },
    'spiti': {
        'subtitle': '<p>8 Days / 7 Nights &bull; Manali, Kaza, Chandratal</p>',
        'description': '<p>\n            An expedition to the rugged, cold desert mountains of Spiti Valley. Discover ancient monasteries, high-altitude lakes, and starry night skies.\n          </p>',
        'image': 'images/spiti.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Manali Arrival</div>
                <div class="timeline-content">
                  <h4>Acclimatization</h4>
                  <p>Rest and prepare for the high-altitude journey ahead in Manali.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2-3: Drive to Kaza</div>
                <div class="timeline-content">
                  <h4>Rohtang & Kunzum Pass</h4>
                  <p>A thrilling off-road drive via Rohtang and Kunzum pass. Enter the Spiti Valley.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4-5: Exploring Kaza</div>
                <div class="timeline-content">
                  <h4>Key Monastery & Kibber</h4>
                  <p>Visit the iconic Key Monastery, the high village of Kibber, and send a postcard from Hikkim (highest post office).</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 6-8: Chandratal & Return</div>
                <div class="timeline-content">
                  <h4>The Moon Lake</h4>
                  <p>Camp near the stunning Chandratal Lake before making the rugged journey back to Manali.</p>
                </div>
              </div>
            </div>'''
    },
    'northeast': {
        'subtitle': '<p>6 Days / 5 Nights &bull; Shillong, Cherrapunji</p>',
        'description': '<p>\n            Explore the abode of clouds in Meghalaya. Witness living root bridges, majestic waterfalls, and crystal clear rivers in India\'s Northeast.\n          </p>',
        'image': 'images/meghalaya.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Guwahati to Shillong</div>
                <div class="timeline-content">
                  <h4>The Scotland of the East</h4>
                  <p>Arrive in Guwahati and drive to Shillong. En route, visit the serene Umiam Lake.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2-3: Cherrapunji</div>
                <div class="timeline-content">
                  <h4>Waterfalls & Caves</h4>
                  <p>Witness Nohkalikai Falls, explore Mawsmai Caves, and experience the wettest place on earth.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4: Living Root Bridge</div>
                <div class="timeline-content">
                  <h4>Nature's Marvel</h4>
                  <p>Embark on an adventurous trek to the Double Decker Living Root Bridge in Nongriat.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 5-6: Dawki & Departure</div>
                <div class="timeline-content">
                  <h4>Crystal River</h4>
                  <p>Boat on the transparent Umngot River in Dawki. Visit Mawlynnong before departing via Guwahati.</p>
                </div>
              </div>
            </div>'''
    },
    'darjeeling': {
        'subtitle': '<p>5 Days / 4 Nights &bull; Darjeeling, Tiger Hill</p>',
        'description': '<p>\n            A charming retreat into the Eastern Himalayas. Enjoy world-famous tea gardens, the heritage Toy Train, and sweeping views of Mt. Kanchenjunga.\n          </p>',
        'image': 'images/darjeeling.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Arrival in Darjeeling</div>
                <div class="timeline-content">
                  <h4>Hill Station Charm</h4>
                  <p>Check into your hotel. Spend the evening strolling around the famous Mall Road.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2: Tiger Hill Sunrise</div>
                <div class="timeline-content">
                  <h4>Majestic Peaks</h4>
                  <p>Early morning drive to Tiger Hill to witness the sunrise over Mt. Kanchenjunga. Visit Ghoom Monastery.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 3: Tea & Toy Train</div>
                <div class="timeline-content">
                  <h4>Heritage & Culture</h4>
                  <p>Take a joyride on the Himalayan Railway Toy Train. Afternoon tour of a working tea estate.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4-5: Sightseeing & Departure</div>
                <div class="timeline-content">
                  <h4>Peace Pagoda</h4>
                  <p>Visit the Japanese Peace Pagoda and Padmaja Naidu Zoo before departing for Bagdogra Airport.</p>
                </div>
              </div>
            </div>'''
    },
    'hampi': {
        'subtitle': '<p>4 Days / 3 Nights &bull; Hampi Ruins & Temples</p>',
        'description': '<p>\n            Step back in time to the Vijayanagara Empire. Explore ancient boulder-strewn landscapes, majestic temples, and a deep, captivating history.\n          </p>',
        'image': 'images/hampi.jpg',
        'timeline': '''<div class="timeline">
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 1: Arrival & Virupaksha</div>
                <div class="timeline-content">
                  <h4>Sacred Center</h4>
                  <p>Arrive in Hampi. Visit the grand Virupaksha Temple and watch the sunset from Hemakuta Hill.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 2: Vittala Temple & Chariot</div>
                <div class="timeline-content">
                  <h4>Architectural Marvels</h4>
                  <p>Explore the Vittala Temple complex, marvel at the Stone Chariot, and see the Royal Enclosure.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 3: Coracles & Hippie Island</div>
                <div class="timeline-content">
                  <h4>River & Boulders</h4>
                  <p>Take a Coracle ride on the Tungabhadra River. Explore the relaxed vibe of Sanapur Lake.</p>
                </div>
              </div>
              <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-day">Day 4: Departure</div>
                <div class="timeline-content">
                  <h4>Farewell Hampi</h4>
                  <p>Early morning trek up Matanga Hill for sunrise before concluding your historical journey.</p>
                </div>
              </div>
            </div>'''
    }
}

for dest, data in destinations.items():
    filepath = f"d:/Projects/TripwithMe/trip-details-{dest}.html"
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace Hero Images (Both night and day)
    content = re.sub(r"url\('images/hero-bg\.jpg'\)", f"url('{data['image']}')", content)
    
    # 2. Replace Subtitle (handles bullet points, html entities or spaces)
    content = re.sub(r'<p>7 Days / 6 Nights.*?Udaipur</p>', data['subtitle'], content, flags=re.DOTALL)
    
    # 3. Replace Description
    content = re.sub(r'<h2 style="color: var\(--primary-base\); margin-bottom: 1rem">\s*About the Trip\s*</h2>\s*<p>.*?</p>', 
                     f'<h2 style="color: var(--primary-base); margin-bottom: 1rem">\n            About the Trip\n          </h2>\n          {data["description"]}', 
                     content, flags=re.DOTALL)
                     
    # 4. Replace Timeline (The original Rajasthan timeline goes up to Day 7: Departure and ends before Animated SVG map)
    # The start is <div class="timeline"> and the end is </div> </div> <!-- Animated SVG Map -->
    # We will match <div class="timeline"> up to <!-- Animated SVG Map -->
    content = re.sub(r'<div class="timeline">.*?</div>\s*</div>\s*<!-- Animated SVG Map -->', 
                     f'{data["timeline"]}\n          </div>\n\n          <!-- Animated SVG Map -->', 
                     content, flags=re.DOTALL)
                     
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all 8 destination files with perfect regex!")
