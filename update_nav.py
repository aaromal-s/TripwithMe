import glob

for filename in glob.glob('d:/Projects/TripwithMe/*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Some might have class="nav-link", some might not (like in the footer or mobile menu)
    # The header links typically look like: <li><a href="#" class="nav-link">About Us</a></li>
    content = content.replace('href="#" class="nav-link">About Us', 'href="about.html" class="nav-link">About Us')
    content = content.replace('href="#" class="nav-link">Contact', 'href="contact.html" class="nav-link">Contact')
    
    # Also handle the ones in the mobile menu or footer if they don't have the class
    content = content.replace('href="#">About Us', 'href="about.html">About Us')
    content = content.replace('href="#">Contact', 'href="contact.html">Contact')
    
    # Just in case for Contact Support
    content = content.replace('href="#">Contact Support', 'href="contact.html">Contact Support')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav links updated across all HTML files.")
