COMPARE_MODAL_HTML = """
    <!-- Compare Modal -->
    <div class="compare-modal-overlay" id="compare-modal-overlay">
      <div class="compare-modal">
        <button class="compare-close-btn" id="compare-close-btn">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" width="24" height="24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
          </svg>
        </button>
        <h2>Compare Packages</h2>
        <div class="compare-grid" id="compare-grid">
          <!-- Dynamically populated -->
        </div>
      </div>
    </div>
"""

with open('d:/Projects/TripwithMe/packages.html', 'r', encoding='utf-8') as f:
    content = f.read()

if "compare-modal-overlay" not in content:
    new_content = content.replace("    </main>", "    </main>\n" + COMPARE_MODAL_HTML)
    with open('d:/Projects/TripwithMe/packages.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Compare modal HTML added!")
else:
    print("Compare modal HTML already exists.")
