import glob

for filepath in glob.glob('e:/Advrite-Website-main/*.html'):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace About Us with About Advrite
    content = content.replace('<span>About Us</span>', '<span>About Advrite</span>')
    content = content.replace('<span>Our Services</span>', '<span>Services</span>')
    content = content.replace('<span>Our Portfolio</span>', '<span>Portfolio</span>')
    content = content.replace('<span>Contact Us</span>', '<span>Contact</span>')
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print('Footer anchor text updated')
