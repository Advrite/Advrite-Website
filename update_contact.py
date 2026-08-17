import os

file_path = "contact.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "        <!-- Dynamic Info Grid -->"
end_marker = "    </main>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = """        <!-- Unified Contact Section -->
        <section class="py-16 md:py-24 bg-white">
            <div class="container mx-auto px-6 max-w-7xl">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24">
                    
                    <!-- Left: Contact Info -->
                    <div class="flex flex-col gap-12 reveal">
                        <div>
                            <h2 class="text-4xl md:text-5xl font-bold text-ui-textPrimary mb-6">Get in Touch</h2>
                            <p class="text-xl text-ui-textSec leading-relaxed">Let's discuss how we can help your brand grow and succeed.</p>
                        </div>

                        <!-- Contact Details -->
                        <div class="flex flex-col gap-8">
                            <!-- Email -->
                            <div>
                                <h4 class="text-sm font-bold tracking-widest uppercase text-ui-textPrimary mb-4">Email Us</h4>
                                <a href="mailto:hello@advrite.com" class="flex items-center gap-3 text-lg font-medium text-ui-textSec hover:text-[#48A9E8] transition-colors duration-300">
                                    <i class="ph ph-envelope-simple text-2xl text-[#48A9E8]"></i> hello@advrite.com
                                </a>
                            </div>
                            
                            <!-- Phone -->
                            <div>
                                <h4 class="text-sm font-bold tracking-widest uppercase text-ui-textPrimary mb-4">Call Us</h4>
                                <div class="flex flex-col gap-4 text-lg font-medium text-ui-textSec">
                                    <a href="tel:+917012008225" class="flex items-center gap-3 hover:text-[#48A9E8] transition-colors duration-300">
                                        <i class="ph ph-phone text-2xl text-[#48A9E8]"></i> +91 70120 08225
                                    </a>
                                    <a href="tel:+918590008225" class="flex items-center gap-3 hover:text-[#48A9E8] transition-colors duration-300">
                                        <i class="ph ph-whatsapp-logo text-2xl text-[#48A9E8]"></i> +91 85900 08225
                                    </a>
                                </div>
                            </div>

                            <!-- Hours -->
                            <div>
                                <h4 class="text-sm font-bold tracking-widest uppercase text-ui-textPrimary mb-4">Business Hours</h4>
                                <p class="text-lg font-medium text-ui-textSec">Mon-Fri: 9am - 6pm IST</p>
                            </div>
                            
                            <!-- Socials -->
                            <div>
                                <h4 class="text-sm font-bold tracking-widest uppercase text-ui-textPrimary mb-4">Connect Socially</h4>
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
                        </div>
                    </div>
                    
                    <!-- Right: Form -->
                    <div class="bg-ui-bgLightLav p-8 md:p-12 rounded-[40px] relative overflow-hidden reveal reveal-delay-1">
                        <!-- Success State -->
                        <div id="success-state" class="absolute inset-0 bg-ui-bgLightLav z-20 hidden flex-col items-center justify-center text-center p-8">
                            <svg class="w-24 h-24 mb-6" viewBox="0 0 100 100">
                                <circle class="success-circle" cx="50" cy="50" r="45" fill="none" stroke="#22c55e" stroke-width="5"/>
                                <path class="success-check" d="M30 50 L45 65 L70 35" fill="none" stroke="#22c55e" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            <h3 class="text-3xl font-bold text-ui-textPrimary mb-3">Inquiry Received</h3>
                            <p class="text-ui-textSec mb-8 font-medium">Thank you! Our strategy team will review your project details and reach out shortly.</p>
                            <button onclick="resetForm()" class="text-[#48A9E8] font-bold hover:underline">Send another inquiry</button>
                        </div>

                        <div id="form-container">
                            <h3 class="text-2xl font-bold text-ui-textPrimary mb-2">Project Brief</h3>
                            <p class="text-ui-textSec mb-8">Tell us what you're trying to build.</p>
                            
                            <form id="contact-form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="space-y-6">
                                <input type="hidden" name="form-name" value="contact" />
                                <p class="hidden">
                                    <label>Donâ€™t fill this out if you're human: <input name="bot-field" /></label>
                                </p>

                                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                    <div>
                                        <label for="name" class="block text-sm font-bold text-ui-textPrimary mb-2">Full Name <span class="text-[#48A9E8]">*</span></label>
                                        <input type="text" id="name" name="name" class="w-full px-5 py-4 rounded-xl bg-white border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary" placeholder="John Doe">
                                        <span class="error-msg text-red-500 text-sm hidden mt-1">Please enter your name.</span>
                                    </div>
                                    <div>
                                        <label for="email" class="block text-sm font-bold text-ui-textPrimary mb-2">Email Address <span class="text-[#48A9E8]">*</span></label>
                                        <input type="email" id="email" name="email" class="w-full px-5 py-4 rounded-xl bg-white border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary" placeholder="john@company.com">
                                        <span class="error-msg text-red-500 text-sm hidden mt-1">Please enter a valid email address.</span>
                                    </div>
                                </div>
                                
                                <div>
                                    <label for="service" class="block text-sm font-bold text-ui-textPrimary mb-2">Primary Service Needed</label>
                                    <div class="relative">
                                        <select id="service" name="service" class="w-full px-5 py-4 rounded-xl bg-white border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary appearance-none cursor-pointer font-medium">
                                            <option value="branding">Brand Identity Design</option>
                                            <option value="uiux">UI/UX Design</option>
                                            <option value="webdev">Web Development (Next.js / Webflow)</option>
                                            <option value="marketing">Digital Marketing / Content</option>
                                            <option value="other">Other / Custom Strategy</option>
                                        </select>
                                        <i class="ph-bold ph-caret-down absolute right-5 top-1/2 transform -translate-y-1/2 text-ui-textSec pointer-events-none"></i>
                                    </div>
                                </div>

                                <div>
                                    <label for="budget" class="block text-sm font-bold text-ui-textPrimary mb-2">Estimated Budget</label>
                                    <div class="relative">
                                        <select id="budget" name="budget" class="w-full px-5 py-4 rounded-xl bg-white border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary appearance-none cursor-pointer font-medium">
                                            <option value="under_5k">Under $5,000</option>
                                            <option value="5k_15k">$5,000 - $15,000</option>
                                            <option value="15k_30k">$15,000 - $30,000</option>
                                            <option value="over_30k">$30,000+</option>
                                        </select>
                                        <i class="ph-bold ph-caret-down absolute right-5 top-1/2 transform -translate-y-1/2 text-ui-textSec pointer-events-none"></i>
                                    </div>
                                </div>

                                <div>
                                    <label for="message" class="block text-sm font-bold text-ui-textPrimary mb-2">Project Details <span class="text-[#48A9E8]">*</span></label>
                                    <textarea id="message" name="message" rows="4" class="w-full px-5 py-4 rounded-xl bg-white border border-transparent focus:outline-none focus:border-[#48A9E8] focus:ring-1 focus:ring-[#48A9E8] transition-all text-ui-textPrimary resize-none" placeholder="Tell us about your company, current challenges, and goals..."></textarea>
                                    <span class="error-msg text-red-500 text-sm hidden mt-1">Please provide some project details.</span>
                                </div>
                                
                                <div class="pt-2">
                                    <button type="submit" id="submit-btn" class="w-full bg-ui-textPrimary text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-[#48A9E8] transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center gap-2">
                                        <span>Send Inquiry</span>
                                        <i class="ph-bold ph-paper-plane-right"></i>
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </section>
"""
    
    final_html = content[:start_idx] + new_html + "\n    </main>" + content[end_idx + len("    </main>"):]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Replaced Contact section successfully.")
else:
    print("Failed to find markers.")
