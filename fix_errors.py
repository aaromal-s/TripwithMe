import glob
import re

def fix_errors():
    # 1. Fix script.js
    with open('d:/Projects/TripwithMe/script.js', 'r', encoding='utf-8', errors='ignore') as f:
        js_content = f.read()
    
    # Fix corrupted star characters
    js_content = re.sub(r"const stars = '.*?'\.repeat\(rating\) \+ '.*?'\.repeat\(5 - rating\);", 
                        "const stars = '★'.repeat(rating) + '☆'.repeat(5 - rating);", 
                        js_content)
    
    # Fix copyright symbol
    js_content = js_content.replace("attribution: 'Ac OpenStreetMap contributors'", 
                                    "attribution: '&copy; OpenStreetMap contributors'")
    
    with open('d:/Projects/TripwithMe/script.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    # 2. Fix HTML files
    html_files = glob.glob('d:/Projects/TripwithMe/*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Fix missing heart in footer
        content = re.sub(r'<span style="color: var\(--primary-accent\)">\s*</span> for travelers.', 
                         '<span style="color: var(--primary-accent)">&hearts;</span> for travelers.', 
                         content)
                         
        content = re.sub(r'<span style="color: var\(--primary-accent\)">.*?</span> for travelers.', 
                         '<span style="color: var(--primary-accent)">&hearts;</span> for travelers.', 
                         content)
        
        # In packages.html, ensure Compare button closes properly if it was missing something
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Fixed JS encoding and HTML footer hearts!")

fix_errors()
