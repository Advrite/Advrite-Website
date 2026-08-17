import os
import re

files = ["index.html", "about.html", "services.html", "portfolio.html", "contact.html"]

nav_template = '''    <nav id="main-nav" class="fixed top-0 w-full bg-gradient-to-b from-black/80 via-black/40 to-transparent z-50 transition-all duration-300">
        <div class="container mx-auto px-6 max-w-7xl h-[90px] flex justify-between items-center relative">
            <!-- Logo -->
            <a href="index.html" class="flex-shrink-0 z-10 lg:-ml-[5%]">
                <img src="assets/logo-white.svg" alt="Advrite Logo" class="h-[61px]" />
            </a>
            
            <!-- Center Nav Links -->
            <div class="hidden md:flex absolute left-1/2 -translate-x-1/2 items-center gap-10 font-medium text-[15px]">
                <a href="index.html" class="{class_home} hover:text-white transition-colors duration-300">Home</a>
                <a href="about.html" class="{class_about} hover:text-white transition-colors duration-300">About</a>
                <a href="services.html" class="{class_services} hover:text-white transition-colors duration-300">Services</a>
                <a href="portfolio.html" class="{class_portfolio} hover:text-white transition-colors duration-300">Portfolio</a>
                <a href="contact.html" class="{class_contact} hover:text-white transition-colors duration-300">Contact</a>
            </div>
            
            <!-- CTA Right -->
            <div class="hidden md:block flex-shrink-0 z-10">
                <a href="contact.html" class="bg-brand-primary text-white px-7 py-2.5 rounded-full hover:bg-brand-hover transition-colors duration-300 font-medium text-[15px]">
                    Get a Quote
                </a>
            </div>

            <!-- Mobile Menu Toggle -->
            <div class="md:hidden flex items-center z-10">
                <button id="mobile-menu-btn" class="text-white hover:text-brand-primary p-2" aria-label="Open menu">
                    <i class="ph ph-list text-3xl"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu Overlay -->
        <div id="mobile-menu" class="fixed inset-0 bg-white/95 backdrop-blur-md z-40 hidden flex-col items-center justify-center pt-20 pb-8 px-6 overflow-y-auto h-screen">
            <button id="mobile-menu-close" class="absolute top-6 right-6 text-ui-textPrimary hover:text-brand-primary p-2" aria-label="Close menu">
                <i class="ph ph-x text-3xl"></i>
            </button>
            <div class="flex flex-col items-center gap-6 text-xl w-full max-w-sm mt-8">
                <a href="index.html" class="mobile-link {m_class_home} hover:text-brand-primary transition-colors py-2">Home</a>
                <a href="about.html" class="mobile-link {m_class_about} hover:text-brand-primary transition-colors py-2">About</a>
                <a href="services.html" class="mobile-link {m_class_services} hover:text-brand-primary transition-colors py-2">Services</a>
                <a href="portfolio.html" class="mobile-link {m_class_portfolio} hover:text-brand-primary transition-colors py-2">Portfolio</a>
                <a href="contact.html" class="mobile-link {m_class_contact} hover:text-brand-primary transition-colors py-2">Contact</a>
                <a href="contact.html" class="mobile-link bg-brand-primary text-white px-8 py-4 rounded-full hover:bg-brand-hover hover:text-white transition-colors w-full text-center mt-6 font-medium">
                    Get a Quote
                </a>
            </div>
        </div>
    </nav>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Generate the nav tailored to this file
    kwargs = {
        'class_home': 'text-brand-primary' if f == 'index.html' else 'text-white/80',
        'class_about': 'text-brand-primary' if f == 'about.html' else 'text-white/80',
        'class_services': 'text-brand-primary' if f == 'services.html' else 'text-white/80',
        'class_portfolio': 'text-brand-primary' if f == 'portfolio.html' else 'text-white/80',
        'class_contact': 'text-brand-primary' if f == 'contact.html' else 'text-white/80',
        
        'm_class_home': 'text-brand-primary' if f == 'index.html' else 'text-ui-textSec',
        'm_class_about': 'text-brand-primary' if f == 'about.html' else 'text-ui-textSec',
        'm_class_services': 'text-brand-primary' if f == 'services.html' else 'text-ui-textSec',
        'm_class_portfolio': 'text-brand-primary' if f == 'portfolio.html' else 'text-ui-textSec',
        'm_class_contact': 'text-brand-primary' if f == 'contact.html' else 'text-ui-textSec',
    }
    
    new_nav = nav_template.format(**kwargs)
    
    # Regex to find <nav id="main-nav" ...> ... </nav>
    # Note: re.DOTALL allows . to match newlines
    pattern = re.compile(r'<nav id="main-nav".*?</nav>', re.DOTALL)
    new_content = pattern.sub(new_nav, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("Navbar updated across all pages.")
