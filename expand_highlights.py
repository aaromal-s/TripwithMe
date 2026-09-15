# -*- coding: utf-8 -*-
with open('d:/Projects/TripwithMe/packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "<li>✓ Heritage Hotel Stay</li>": "<li>✓ Heritage Hotel Stay</li>\n                <li>✓ Local Cultural Shows</li>\n                <li>✓ Authentic Rajasthani Cuisine</li>",
    "<li>✓ Ayurvedic Spa</li>": "<li>✓ Ayurvedic Spa</li>\n                <li>✓ Kathakali Performance</li>\n                <li>✓ Spice Plantation Walk</li>",
    "<li>✓ Pine Forest Trek</li>": "<li>✓ Pine Forest Trek</li>\n                <li>✓ Solang Valley Tour</li>\n                <li>✓ Bonfire Nights</li>",
    "<li>✓ Fort Aguada</li>": "<li>✓ Fort Aguada</li>\n                <li>✓ Dudhsagar Waterfalls</li>\n                <li>✓ Portuguese Heritage Walk</li>",
    "<li>✓ Yoga Retreat</li>": "<li>✓ Yoga Retreat</li>\n                <li>✓ Valley of Flowers</li>\n                <li>✓ White Water Rafting</li>",
    "<li>✓ Waterfalls</li>": "<li>✓ Waterfalls</li>\n                <li>✓ Mawsmai Cave Exploration</li>\n                <li>✓ Cleanest Village Tour</li>",
    "<li>✓ Cellular Jail</li>": "<li>✓ Cellular Jail</li>\n                <li>✓ Glass Bottom Boat Ride</li>\n                <li>✓ Snorkeling at Elephant Beach</li>",
    "<li>✓ Pahalgam Views</li>": "<li>✓ Pahalgam Views</li>\n                <li>✓ Mughal Gardens Visit</li>\n                <li>✓ Saffron Fields Tour</li>",
    "<li>✓ High Altitude Roads</li>": "<li>✓ High Altitude Roads</li>\n                <li>✓ Pin Valley National Park</li>\n                <li>✓ Stargazing in Kibber</li>",
    "<li>✓ Tiger Hill Sunrise</li>": "<li>✓ Tiger Hill Sunrise</li>\n                <li>✓ Peace Pagoda Visit</li>\n                <li>✓ Batasia Loop Exploration</li>"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('d:/Projects/TripwithMe/packages.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Highlights successfully expanded!")
