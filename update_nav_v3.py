import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The exact new template we want to inject
nav_template = '''    <nav id="main-nav" class="fixed top-0 w-full z-50 transition-all duration-300 pointer-events-none">
        <div class="container mx-auto px-6 max-w-7xl h-[90px] flex justify-between items-center relative pointer-events-auto">
            <!-- Logo -->
            <a href="index.html" class="flex-shrink-0 z-10 lg:-ml-[5%]">
                <img src="assets/logo-white.svg" alt="Advrite Logo" class="h-[61px]" />
            </a>
            
            <!-- Center Nav Links -->
            <div class="hidden md:flex absolute left-1/2 -translate-x-1/2 items-center gap-12 font-medium text-[15px]">
                <a href="index.html" class="text-white hover:text-brand-primary transition-colors duration-300">Home</a>
                <a href="about.html" class="text-white hover:text-brand-primary transition-colors duration-300">About</a>
                <a href="services.html" class="text-white hover:text-brand-primary transition-colors duration-300">Services</a>
                <a href="portfolio.html" class="text-white hover:text-brand-primary transition-colors duration-300">Portfolio</a>
                <a href="contact.html" class="text-white hover:text-brand-primary transition-colors duration-300">Contact</a>
            </div>
            
            <!-- CTA Right -->
            <div class="hidden md:block flex-shrink-0 z-10">
                <a href="contact.html" class="bg-brand-primary text-white px-7 py-2.5 rounded-full hover:bg-brand-hover transition-colors duration-300 font-medium text-[15px]">
                    Get a Quote
                </a>
            </div>

            <!-- Mobile Menu Toggle -->
            <div class="md:hidden flex items-center z-10">
                <button id="mobile-menu-btn" class="text-white hover:text-brand-primary p-2 transition-colors duration-300" aria-label="Open menu">
                    <i class="ph ph-list text-3xl"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Overlay -->
        <div id="mobile-menu" class="fixed inset-0 bg-black/95 backdrop-blur-lg z-40 hidden flex-col items-center justify-center pt-20 pb-8 px-6 overflow-y-auto h-screen pointer-events-auto">
            <button id="mobile-menu-close" class="absolute top-6 right-6 text-white hover:text-brand-primary p-2 transition-colors duration-300" aria-label="Close menu">
                <i class="ph ph-x text-4xl"></i>
            </button>
            <div class="flex flex-col items-center justify-center space-y-8 w-full">
                <a href="index.html" class="mobile-link text-3xl font-medium text-white hover:text-brand-primary transition-colors">Home</a>
                <a href="about.html" class="mobile-link text-3xl font-medium text-white hover:text-brand-primary transition-colors">About</a>
                <a href="services.html" class="mobile-link text-3xl font-medium text-white hover:text-brand-primary transition-colors">Services</a>
                <a href="portfolio.html" class="mobile-link text-3xl font-medium text-white hover:text-brand-primary transition-colors">Portfolio</a>
                <a href="contact.html" class="mobile-link text-3xl font-medium text-white hover:text-brand-primary transition-colors">Contact</a>
                <a href="contact.html" class="mobile-link mt-4 bg-brand-primary text-white px-10 py-4 rounded-full font-bold text-xl hover:bg-brand-hover transition-colors w-full text-center max-w-[280px]">
                    Get a Quote
                </a>
            </div>
        </div>
    </nav>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match the entire <nav id="main-nav"> block
    nav_pattern = re.compile(r'<nav id="main-nav"[\s\S]*?</nav>', re.MULTILINE)

    if nav_pattern.search(content):
        # Determine the active page
        page_name = os.path.basename(file)
        
        # We need to make the active link purple.
        # Let's modify the template for this specific page.
        page_template = nav_template
        if page_name == 'index.html':
            page_template = page_template.replace('href="index.html" class="text-white hover:text-brand-primary', 'href="index.html" class="text-brand-primary hover:text-white')
        elif page_name == 'about.html':
            page_template = page_template.replace('href="about.html" class="text-white hover:text-brand-primary', 'href="about.html" class="text-brand-primary hover:text-white')
        elif page_name == 'services.html':
            page_template = page_template.replace('href="services.html" class="text-white hover:text-brand-primary', 'href="services.html" class="text-brand-primary hover:text-white')
        elif page_name == 'portfolio.html':
            page_template = page_template.replace('href="portfolio.html" class="text-white hover:text-brand-primary', 'href="portfolio.html" class="text-brand-primary hover:text-white')
        elif page_name == 'contact.html':
            page_template = page_template.replace('href="contact.html" class="text-white hover:text-brand-primary', 'href="contact.html" class="text-brand-primary hover:text-white')

        new_content = nav_pattern.sub(page_template, content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Could not find nav block in {file}")
