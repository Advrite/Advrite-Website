import glob
import os

html_files = glob.glob('*.html')
old_email = 'hello@advrite.com'
new_email = 'hello.advrite@gmail.com'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_email in content:
        new_content = content.replace(old_email, new_email)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
