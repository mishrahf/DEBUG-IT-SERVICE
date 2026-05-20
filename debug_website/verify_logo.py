#!/usr/bin/env python
"""
Logo Setup Verification Script
Checks if logo is properly placed and provides diagnostic info
"""

import os
import sys
from pathlib import Path

# Get the project root
project_root = Path(__file__).parent
static_dir = project_root / 'static' / 'images'
logo_path = static_dir / 'logo.png'

print("=" * 60)
print("DEBUG IT SERVICE - Logo Setup Verification")
print("=" * 60)

# Check if directory exists
if static_dir.exists():
    print(f"✓ Images directory exists: {static_dir}")
else:
    print(f"✗ Images directory NOT found: {static_dir}")
    print(f"  Creating directory...")
    static_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Directory created successfully")

# Check if logo exists
if logo_path.exists():
    file_size = logo_path.stat().st_size
    file_size_mb = file_size / (1024 * 1024)
    print(f"✓ Logo file found: {logo_path}")
    print(f"  File size: {file_size_mb:.2f} MB")
    print(f"\n✓ Logo is properly set up! Your website will display it perfectly.")
else:
    print(f"✗ Logo file NOT found: {logo_path}")
    print(f"\nTo fix this:")
    print(f"1. Save your logo image as: logo.png")
    print(f"2. Place it in: {static_dir}")
    print(f"3. Restart the Django server")
    print(f"4. Refresh your browser")

# Check template files
print(f"\n{'=' * 60}")
print("Template Status:")
print("=" * 60)

template_files = {
    'base.html': project_root / 'templates' / 'base.html',
    'index.html': project_root / 'templates' / 'home' / 'index.html',
}

for name, path in template_files.items():
    if path.exists():
        with open(path, 'r') as f:
            content = f.read()
            if 'logo.png' in content or 'navbar-logo' in content:
                print(f"✓ {name} - Logo references found")
            else:
                print(f"✗ {name} - No logo references found")
    else:
        print(f"✗ {name} - File not found")

# Check CSS
print(f"\n{'=' * 60}")
print("CSS Status:")
print("=" * 60)

css_path = project_root / 'static' / 'css' / 'style.css'
if css_path.exists():
    with open(css_path, 'r') as f:
        content = f.read()
        if '.navbar-logo' in content:
            print(f"✓ CSS includes navbar-logo styles")
        if '.hero-logo' in content:
            print(f"✓ CSS includes hero-logo styles with animation")
        if '.footer-logo' in content:
            print(f"✓ CSS includes footer-logo styles")
else:
    print(f"✗ CSS file not found: {css_path}")

print(f"\n{'=' * 60}")
print("INSTRUCTIONS:")
print("=" * 60)
print(f"""
1. Save your DEBUG IT SERVICE logo as:
   {logo_path}

2. Make sure the file has:
   - Filename: logo.png
   - Format: PNG (preferably with transparency)
   - Location: {static_dir}

3. Refresh your browser at:
   http://localhost:8000

4. You should see the logo in:
   - Navigation bar (60px height)
   - Hero section (animated)
   - Footer (80px height)

If you still don't see the logo:
- Check browser cache (Ctrl+Shift+Delete)
- Ensure the file path is exactly: {logo_path}
- Restart the Django server
""")

print("=" * 60)
