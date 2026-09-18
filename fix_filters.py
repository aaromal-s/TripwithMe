import re

with open('d:/Projects/TripwithMe/packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add missing regions
region_html = """          <label class="checkbox-label">
            <input type="checkbox" value="West India" /> West India
          </label>
          <label class="checkbox-label">
            <input type="checkbox" value="East India" /> East India
          </label>
          <label class="checkbox-label">
            <input type="checkbox" value="North East India" /> North East India
          </label>"""

content = re.sub(r'          <label class="checkbox-label">\s*<input type="checkbox" value="West India" /> West India\s*</label>', region_html, content)

# Add missing styles
style_html = """          <label class="checkbox-label">
            <input type="checkbox" value="Relaxation" /> Relaxation
          </label>
          <label class="checkbox-label">
            <input type="checkbox" value="Adventure" /> Adventure
          </label>"""

content = re.sub(r'          <label class="checkbox-label">\s*<input type="checkbox" value="Relaxation" /> Relaxation\s*</label>', style_html, content)

with open('d:/Projects/TripwithMe/packages.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed packages.html filters!")
