import re
import glob

# Ensure print to stdout works in cp1252 (PowerShell) without crashing
import sys
sys.stdout.reconfigure(encoding='utf-8')

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Fix checkmarks in highlights
    # The corrupted checkmark might look like 'o" ', '? ', or just garbage before a word.
    # The structure is exactly <li> followed by the corruption, followed by a space, then the word.
    # Let's replace any non-alphanumeric between <li> and the first word with '✓ '
    content = re.sub(r'<li>[^A-Za-z0-9<]+([A-Z])', r'<li>✓ \1', content)

    # Fix price symbols
    # <span class="pkg-price" data-base-price="28500">,128,500</span> -> ₹28,500
    content = re.sub(r'(class="pkg-price"[^>]*>)[^0-9]+([0-9])', r'\1₹\2', content)

    # Fix footer heart
    content = re.sub(r'with <span style="color:var\(--primary-accent\)">[^<]+</span> for travelers',
                     r'with <span style="color:var(--primary-accent)">♥</span> for travelers', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("All encoding errors in HTML files have been fixed!")
