import glob
import re

def check_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    
    # Check for empty hrefs that should be fixed (we just fixed #, but let's check)
    if 'href=""' in content:
        errors.append("Empty href found")
        
    # Count tags to find mismatched pairs roughly
    tags_to_check = ['div', 'section', 'main', 'header', 'footer', 'form', 'ul', 'li', 'span', 'p', 'h1', 'h2', 'h3']
    for tag in tags_to_check:
        open_count = len(re.findall(rf'<{tag}\b[^>]*>', content))
        close_count = len(re.findall(rf'</{tag}>', content))
        if open_count != close_count:
            errors.append(f"Mismatched <{tag}>: {open_count} open, {close_count} close")
            
    return errors

html_files = glob.glob('d:/Projects/TripwithMe/*.html')
for file in html_files:
    errors = check_html(file)
    if errors:
        print(f"Errors in {file}:")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"No obvious tag mismatch in {file}")
