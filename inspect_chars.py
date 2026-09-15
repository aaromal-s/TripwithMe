import re
import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        
    matches = re.findall(r'<li>([^A-Za-z0-9<]+)[A-Z]', content)
    unique_matches = set(matches)
    if unique_matches:
        print(f"{filename} list item prefixes: {unique_matches}")

    price_matches = re.findall(r'class="pkg-price"[^>]*>([^0-9]+)[0-9]', content)
    unique_prices = set(price_matches)
    if unique_prices:
        print(f"{filename} price prefixes: {unique_prices}")
        
    footer_matches = re.findall(r'with <span[^>]*>(.+?)</span> for travelers', content)
    unique_footer = set(footer_matches)
    if unique_footer:
        print(f"{filename} footer symbols: {unique_footer}")
