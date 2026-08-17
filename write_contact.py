import os

html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- SEO Master Tags -->
    <title>Contact Us | Let's Build Something Iconic | Advrite</title>
    <meta name="description" content="Ready to scale your brand? Contact Advrite to discuss Brand Identity, UI/UX, or Web Development. Book a discovery call today.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://advrite.com/contact" />
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://advrite.com/contact">
    <meta property="og:title" content="Contact Us | Advrite">
    <meta property="og:description" content="Ready to scale your brand? Contact Advrite to discuss Brand Identity, UI/UX, or Web Development. Book a discovery call today.">
    <meta property="og:image" content="https://advrite.com/assets/og-image.jpg">
    <meta property="og:site_name" content="Advrite">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Contact Us | Advrite">
    <meta name="twitter:description" content="Book a discovery call today and scale your brand.">
    <meta name="twitter:image" content="https://advrite.com/assets/og-image.jpg">

    <!-- Schema.org -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "ContactPage",
          "@id": "https://advrite.com/contact/#webpage",
          "url": "https://advrite.com/contact",
          "name": "Contact Advrite",
          "isPartOf": {
            "@id": "https://advrite.com/#website"
          }
        },
        {
          "@type": "LocalBusiness",
          "name": "Advrite Studio",
          "image": "https://advrite.com/assets/logo.svg",
          "@id": "https://advrite.com",
          "url": "https://advrite.com",
          "telephone": "+917012008225",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Cyber Park Road",
            "addressLocality": "Kozhikode",
            "addressRegion": "KL",
            "postalCode": "673016",
            "addressCountry": "IN"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": 11.255869,
            "longitude": 75.719875
          }
        }
      ]
    }
    </script>
    
    <!-- Preloads & Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web" defer></script>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            primary: '#FF7B67',
                            hover: '#F56A55',
                            accent: '#FF7B67',
                            light: '#FFF5F3',
                        },
                        ui: {
                            bg: '#FFFFFF',
                            bgSec: '#F8F9FA',
                            textPrimary: '#0B0F14',
                            textSec: '#4B5563',
                            border: '#E5E7EB',
                            muted: '#9CA3AF',
                            dark: '#171C24',
                        }
                    },
                    fontFamily: {
                        poppins: ['Poppins', 'sans-serif'],
                        inter: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body class="antialiased selection:bg-[#48A9E8] selection:text-white overflow-x-hidden pt-24 bg-white">

    <!-- Navigation -->
    <nav class="fixed top-0 w-full bg-white/95 backdrop-blur-md z-50">
        <div class="container mx-auto px-6 h-24 flex justify-between items-center">
            <a href="index.html" class="flex items-center gap-2">
                <img src="assets/logo.svg" alt="Advrite Logo" class="h-16" />
            </a>
            <div class="hidden md:flex items-center gap-8 text-ui-textSec">
                <a href="index.html" class="hover:text-[#48A9E8] transition-colors duration-300">Home</a>
                <a href="about.html" class="hover:text-[#48A9E8] transition-colors duration-300">About</a>
                <a href="services.html" class="hover:text-[#48A9E8] transition-colors duration-300">Services</a>
                <a href="portfolio.html" class="hover:text-[#48A9E8] transition-colors duration-300">Portfolio</a>
                <a href="contact.html" class="text-[#48A9E8] font-medium transition-colors duration-300">Contact</a>
            </div>
            <div class="hidden md:block">
                <a href="contact.html" class="bg-[#48A9E8] text-white px-6 py-2.5 rounded-[20px] btn-text hover:bg-[#171719] transition-colors duration-300 inline-block">
                    Start a Project
                </a>
            </div>
            <div class="md:hidden flex items-center">
                <button id="mobile-menu-btn" class="text-ui-textPrimary hover:text-[#48A9E8] p-2" aria-label="Open menu">
                    <i class="ph ph-list text-3xl"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="fixed inset-0 bg-white z-40 hidden flex-col transition-opacity duration-300 opacity-0 pt-24 pb-8 px-6 overflow-y-auto">
            <button id="mobile-menu-close" class="absolute top-8 right-6 text-ui-textPrimary p-2" aria-label="Close menu">
                <i class="ph ph-x text-3xl"></i>
            </button>
            <div class="flex flex-col gap-6 text-2xl font-bold text-ui-textPrimary mt-8">
                <a href="index.html" class="mobile-link hover:text-[#48A9E8] transition-colors py-2">Home</a>
                <a href="about.html" class="mobile-link hover:text-[#48A9E8] transition-colors py-2">About</a>
                <a href="services.html" class="mobile-link hover:text-[#48A9E8] transition-colors py-2">Services</a>
                <a href="portfolio.html" class="mobile-link hover:text-[#48A9E8] transition-colors py-2">Portfolio</a>
                <a href="contact.html" class="mobile-link text-[#48A9E8] transition-colors py-2">Contact</a>
                <a href="contact.html" class="mobile-link bg-[#48A9E8] text-white px-8 py-4 rounded-[20px] btn-text hover:bg-[#171719] hover:text-white transition-colors w-full text-center mt-6">
                    Start a Project
                </a>
            </div>
        </div>
    </nav>

    <main>
        <!-- Contact Hero -->
        <section class="relative pt-32 pb-16 lg:pt-40 lg:pb-24 bg-white overflow-hidden">
            <div class="absolute right-0 top-0 w-[600px] h-[600px] bg-[#F3F4F4] rounded-full blur-[100px] opacity-70 pointer-events-none -z-10 transform translate-x-1/3 -translate-y-1/3"></div>
            
            <div class="container mx-auto px-6 max-w-7xl text-center relative z-10 animate-fade-in-up stagger-1">
                <h4 class="text-sm font-bold tracking-widest uppercase text-[#48A9E8] mb-6">Let's Work Together</h4>
                <h1 class="text-5xl md:text-7xl font-bold text-ui-textPrimary mb-6 leading-[1.1] font-poppins">
                    Have a project in <span class="relative inline-block">mind<span class="absolute -bottom-2 left-0 w-full h-1 bg-[#FFD814]"></span></span>?
                </h1>
                
                <p class="text-xl text-ui-textSec leading-relaxed max-w-2xl mx-auto font-medium mb-10">
                    Tell us what you're building, and let's create something meaningful together.
                </p>
            </div>
        </section>

        <!-- Project Enquiry & Form -->
        <section class="py-16 bg-white">
            <div class="container mx-auto px-6 max-w-7xl">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-24">
                    
                    <!-- Left: Form Info -->
                    <div class="lg:col-span-5 flex flex-col gap-8 animate-fade-in-up stagger-2">
                        <div>
                            <h4 class="text-sm font-bold tracking-widest uppercase text-[#48A9E8] mb-4">Start a Project</h4>
                            <h2 class="text-4xl md:text-5xl font-bold text-ui-textPrimary mb-6 font-poppins">Tell us about your project.</h2>
                            <p class="text-lg text-ui-textSec leading-relaxed">Fill out the form with your details, and our strategy team will review your requirements and reach out shortly.</p>
                        </div>
                        <div class="bg-[#F3F4F4] p-8 rounded-[20px] border border-[#D2CFF2]/50">
                            <h4 class="font-bold text-ui-textPrimary mb-4">What happens next?</h4>
                            <ul class="text-ui-textSec text-sm space-y-4">
                                <li class="flex items-start gap-3"><i class="ph-bold ph-check text-[#48A9E8] mt-0.5 text-lg"></i> We review your details within 24 hours.</li>
                                <li class="flex items-start gap-3"><i class="ph-bold ph-check text-[#48A9E8] mt-0.5 text-lg"></i> We schedule a discovery call to align on goals.</li>
                                <li class="flex items-start gap-3"><i class="ph-bold ph-check text-[#48A9E8] mt-0.5 text-lg"></i> We present a customized proposal and timeline.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Right: Form -->
                    <div class="lg:col-span-7 bg-white border border-[#D2CFF2] shadow-[0_8px_30px_rgb(0,0,0,0.04)] p-8 md:p-12 rounded-[20px] relative overflow-hidden animate-fade-in-up stagger-3">
                        <!-- Success State -->
                        <div id="success-state" class="absolute inset-0 bg-white z-20 hidden flex-col items-center justify-center text-center p-8">
                            <svg class="w-24 h-24 mb-6" viewBox="0 0 100 100">
                                <circle class="success-circle" cx="50" cy="50" r="45" fill="none" stroke="#48A9E8" stroke-width="5"/>
                                <path class="success-check" d="M30 50 L45 65 L70 35" fill="none" stroke="#48A9E8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            <h3 class="text-3xl font-bold text-ui-textPrimary mb-3 font-poppins">Inquiry Received</h3>
                            <p class="text-ui-textSec mb-8 font-medium">Thank you! We've received your project details and will reach out shortly.</p>
                            <button onclick="resetForm()" class="text-[#48A9E8] font-bold hover:text-[#171719] transition-colors">Send another inquiry</button>
                        </div>

                        <div id="form-container">
                            <form id="contact-form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="space-y-6">
                                <input type="hidden" name="form-name" value="contact" />
                                <p class="hidden">
                                    <label>Donâ€™t fill this out if you're human: <input name="bot-field" /></label>
                                </p>

                                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                    <div>
                                        <label for="name" class="block text-sm font-bold text-ui-textPrimary mb-2">Full Name <span class="text-[#48A9E8]">*</span></label>
                                        <input type="text" id="name" name="name" required class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary" placeholder="John Doe">
                                    </div>
                                    <div>
                                        <label for="email" class="block text-sm font-bold text-ui-textPrimary mb-2">Email Address <span class="text-[#48A9E8]">*</span></label>
                                        <input type="email" id="email" name="email" required class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary" placeholder="john@company.com">
                                    </div>
                                </div>
                                
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                    <div>
                                        <label for="phone" class="block text-sm font-bold text-ui-textPrimary mb-2">Phone / WhatsApp</label>
                                        <input type="tel" id="phone" name="phone" class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary" placeholder="+91 98765 43210">
                                    </div>
                                    <div>
                                        <label for="company" class="block text-sm font-bold text-ui-textPrimary mb-2">Company / Brand</label>
                                        <input type="text" id="company" name="company" class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary" placeholder="Your Brand Name">
                                    </div>
                                </div>
                                
                                <div>
                                    <label for="service" class="block text-sm font-bold text-ui-textPrimary mb-2">Service Needed</label>
                                    <div class="relative">
                                        <select id="service" name="service" class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary appearance-none cursor-pointer font-medium">
                                            <option value="branding">Branding</option>
                                            <option value="graphic_design">Graphic Design</option>
                                            <option value="website_design">Website Design</option>
                                            <option value="video_editing">Video Editing</option>
                                            <option value="motion_graphics">Motion Graphics</option>
                                            <option value="digital_marketing">Digital Marketing</option>
                                            <option value="photography_videography">Photography & Videography</option>
                                            <option value="other">Other</option>
                                        </select>
                                        <i class="ph-bold ph-caret-down absolute right-5 top-1/2 transform -translate-y-1/2 text-ui-textSec pointer-events-none"></i>
                                    </div>
                                </div>

                                <div>
                                    <label for="budget" class="block text-sm font-bold text-ui-textPrimary mb-2">Budget Range (INR)</label>
                                    <div class="relative">
                                        <select id="budget" name="budget" class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary appearance-none cursor-pointer font-medium">
                                            <option value="under_50k">Under â‚¹50,000</option>
                                            <option value="50k_150k">â‚¹50,000 - â‚¹1,50,000</option>
                                            <option value="150k_500k">â‚¹1,50,000 - â‚¹5,00,000</option>
                                            <option value="over_500k">â‚¹5,00,000+</option>
                                        </select>
                                        <i class="ph-bold ph-caret-down absolute right-5 top-1/2 transform -translate-y-1/2 text-ui-textSec pointer-events-none"></i>
                                    </div>
                                </div>

                                <div>
                                    <label for="message" class="block text-sm font-bold text-ui-textPrimary mb-2">Project Details <span class="text-[#48A9E8]">*</span></label>
                                    <textarea id="message" name="message" required rows="4" class="w-full px-5 py-4 rounded-[16px] bg-[#F3F4F4] border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary resize-none" placeholder="Tell us about your company, current challenges, and goals..."></textarea>
                                </div>
                                
                                <div class="pt-4">
                                    <button type="submit" id="submit-btn" class="w-full bg-[#48A9E8] text-white px-8 py-4 rounded-[20px] font-bold text-lg hover:bg-[#171719] transition-all duration-300 flex items-center justify-center gap-2">
                                        <span>Submit Project Inquiry</span>
                                        <i class="ph-bold ph-paper-plane-right"></i>
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Information -->
        <section class="py-16 md:py-24 bg-[#F3F4F4] border-y border-[#D2CFF2]/50">
            <div class="container mx-auto px-6 max-w-7xl">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <!-- Email -->
                    <div class="bg-white p-8 rounded-[20px] shadow-sm animate-fade-in-up stagger-1 border border-transparent hover:border-[#48A9E8]/30 transition-all duration-300">
                        <div class="w-12 h-12 rounded-full bg-[#F3F4F4] flex items-center justify-center text-[#48A9E8] mb-6">
                            <i class="ph-fill ph-envelope-simple text-2xl"></i>
                        </div>
                        <h4 class="text-lg font-bold text-ui-textPrimary mb-1">Email Us</h4>
                        <a href="mailto:hello@advrite.com" class="text-ui-textSec font-medium hover:text-[#48A9E8] transition-colors">hello@advrite.com</a>
                    </div>
                    
                    <!-- Phone -->
                    <div class="bg-white p-8 rounded-[20px] shadow-sm animate-fade-in-up stagger-2 border border-transparent hover:border-[#48A9E8]/30 transition-all duration-300">
                        <div class="w-12 h-12 rounded-full bg-[#F3F4F4] flex items-center justify-center text-[#48A9E8] mb-6">
                            <i class="ph-fill ph-phone text-2xl"></i>
                        </div>
                        <h4 class="text-lg font-bold text-ui-textPrimary mb-1">Call Us</h4>
                        <div class="flex flex-col text-ui-textSec font-medium">
                            <a href="tel:+917012008225" class="hover:text-[#48A9E8] transition-colors">+91 70120 08225</a>
                            <a href="tel:+918590008225" class="hover:text-[#48A9E8] transition-colors">+91 85900 08225</a>
                        </div>
                    </div>

                    <!-- WhatsApp -->
                    <div class="bg-white p-8 rounded-[20px] shadow-sm animate-fade-in-up stagger-3 border border-transparent hover:border-[#48A9E8]/30 transition-all duration-300">
                        <div class="w-12 h-12 rounded-full bg-[#F3F4F4] flex items-center justify-center text-[#48A9E8] mb-6">
                            <i class="ph-fill ph-whatsapp-logo text-2xl"></i>
                        </div>
                        <h4 class="text-lg font-bold text-ui-textPrimary mb-1">WhatsApp</h4>
                        <a href="https://wa.me/917012008225" target="_blank" rel="noopener noreferrer" class="text-ui-textSec font-medium hover:text-[#48A9E8] transition-colors">Chat instantly.</a>
                    </div>

                    <!-- Business Hours -->
                    <div class="bg-white p-8 rounded-[20px] shadow-sm animate-fade-in-up stagger-4 border border-transparent hover:border-[#48A9E8]/30 transition-all duration-300">
                        <div class="w-12 h-12 rounded-full bg-[#F3F4F4] flex items-center justify-center text-[#48A9E8] mb-6">
                            <i class="ph-fill ph-clock text-2xl"></i>
                        </div>
                        <h4 class="text-lg font-bold text-ui-textPrimary mb-1">Business Hours</h4>
                        <p class="text-ui-textSec font-medium">Mon-Fri: 9am - 6pm IST</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="pt-16 pb-8 bg-white text-ui-textPrimary border-t border-gray-100">
        <div class="container mx-auto px-6 max-w-7xl">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-8">
                <!-- Left: Brand -->
                <div class="flex flex-col items-start">
                    <a href="index.html" class="inline-block mb-6">
                        <img src="assets/logo.svg" alt="Advrite Logo" loading="lazy" decoding="async" class="h-10 w-auto" />
                    </a>
                    <p class="text-lg font-bold text-ui-textPrimary mb-8">Creative &bull; Branding &bull; Digital</p>
                    
                    <div class="flex gap-6 text-2xl text-ui-textSec">
                        <a href="#" class="hover:text-[#48A9E8] hover:-translate-y-1 transition-all duration-300" aria-label="Instagram">
                            <i class="ph ph-instagram-logo"></i>
                        </a>
                        <a href="#" class="hover:text-[#48A9E8] hover:-translate-y-1 transition-all duration-300" aria-label="Behance">
                            <i class="ph ph-behance-logo"></i>
                        </a>
                        <a href="#" class="hover:text-[#48A9E8] hover:-translate-y-1 transition-all duration-300" aria-label="LinkedIn">
                            <i class="ph ph-linkedin-logo"></i>
                        </a>
                    </div>
                </div>
                
                <!-- Middle: Quick Links -->
                <div class="flex flex-col items-start md:mx-auto">
                    <h4 class="text-sm font-bold tracking-widest uppercase text-ui-textPrimary mb-6">QUICK LINKS</h4>
                    <div class="flex flex-col gap-4 text-base font-medium text-ui-textSec">
                        <a href="about.html" class="hover:text-[#48A9E8] transition-colors duration-300">About Us</a>
                        <a href="services.html" class="hover:text-[#48A9E8] transition-colors duration-300">Services</a>
                        <a href="portfolio.html" class="hover:text-[#48A9E8] transition-colors duration-300">Portfolio</a>
                        <a href="contact.html" class="hover:text-[#48A9E8] transition-colors duration-300">Contact</a>
                    </div>
                </div>

                <!-- Right: Contact -->
                <div class="flex flex-col items-start md:ml-auto">
                    <h4 class="text-sm font-bold tracking-widest uppercase text-ui-textPrimary mb-6">CONTACT</h4>
                    <div class="flex flex-col gap-4 text-base font-medium text-ui-textSec mb-6">
                        <a href="mailto:hello@advrite.com" class="flex items-center gap-3 hover:text-[#48A9E8] transition-colors duration-300">
                            <i class="ph ph-envelope-simple text-xl"></i> hello@advrite.com
                        </a>
                        <a href="tel:+917012008225" class="flex items-center gap-3 hover:text-[#48A9E8] transition-colors duration-300">
                            <i class="ph ph-phone text-xl"></i> +91 70120 08225
                        </a>
                        <a href="tel:+918590008225" class="flex items-center gap-3 hover:text-[#48A9E8] transition-colors duration-300">
                            <i class="ph ph-whatsapp-logo text-xl"></i> +91 85900 08225
                        </a>
                    </div>
                    <a href="contact.html" class="group inline-flex items-center gap-2 text-base font-semibold text-[#48A9E8] hover:opacity-80 transition-opacity duration-300">
                        Start a project <i class="ph ph-arrow-right transform group-hover:translate-x-1 transition-transform duration-300"></i>
                    </a>
                </div>
            </div>

            <!-- Bottom Section -->
            <div class="w-full text-center md:text-left mb-6">
                <span class="text-lg md:text-xl font-bold"><span class="text-[#171A2B]">Let's create something</span> <span class="text-[#48A9E8]">memorable.</span></span>
            </div>
            
            <div class="w-full h-px bg-gray-200 mb-6"></div>
            
            <div class="flex flex-col md:flex-row justify-between items-center gap-4 text-sm font-medium text-ui-textSec">
                <div class="text-center md:text-left">
                    <span>&copy; 2026 Advrite. All Rights Reserved.</span>
                </div>
                <div class="flex gap-8">
                    <a href="#" class="hover:text-[#48A9E8] transition-colors duration-300">Privacy Policy</a>
                    <a href="#" class="hover:text-[#48A9E8] transition-colors duration-300">Terms</a>
                </div>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
    <script src="js/animations.js"></script>
    <script src="js/navigation.js"></script>
</body>
</html>
"""

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("contact.html written successfully!")
