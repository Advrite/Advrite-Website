const fs = require('fs');
const path = require('path');

const files = ['index.html', 'about.html', 'services.html', 'portfolio.html', 'contact.html'];

const oldConfig = `        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: { primary: '#7A7AFF', hover: '#31316B', accentLav: '#B899ED' },
                        ui: { bg: '#FFFFFF', bgLightLav: '#F0F0FB', bgSoftLav: '#D2CFF2', textPrimary: '#161B2D', textSec: '#666680', textBlack: '#050609' }
                    },
                    fontFamily: { poppins: ['Poppins', 'sans-serif'], inter: ['Inter', 'sans-serif'] },
                    borderRadius: { 'btn': '20px', 'card': '20px' }
                }
            }
        }`;

const newConfig = `        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: { primary: '#7A7AFF', hover: '#31316B', accentLav: '#B899ED', creativeYellow: '#FFFC00' },
                        ui: { bg: '#FFFFFF', bgLightLav: '#F0F0FB', bgSoftLav: '#D2CFF2', textPrimary: '#161B2D', textSec: '#666680', textBlack: '#050609' }
                    },
                    fontFamily: { poppins: ['Poppins', 'sans-serif'], inter: ['Inter', 'sans-serif'] },
                    borderRadius: { 'btn': '20px', 'card': '20px' }
                }
            }
        }`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // 1. Replace Config
    content = content.replace(oldConfig, newConfig);
    
    // 2. Update Sparkle Icons (e.g. on homepage hero and badges)
    content = content.replace(/class="ph-fill ph-sparkle"/g, 'class="ph-fill ph-sparkle text-brand-creativeYellow"');
    
    // 3. Update stars (e.g. in testimonials and hero)
    content = content.replace(/text-amber-400/g, 'text-brand-creativeYellow');
    
    // 4. Update Portfolio hover details to include yellow accents
    // Originally: <p class="text-white/80 font-medium translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-75">Branding • Logo Design</p>
    // I'll add a yellow dot or something, or change the bullet to yellow.
    content = content.replace(/•/g, '<span class="text-brand-creativeYellow">•</span>');
    
    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated ' + file);
});
