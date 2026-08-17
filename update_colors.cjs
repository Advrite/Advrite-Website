const fs = require('fs');
const path = require('path');

const files = ['index.html', 'about.html', 'services.html', 'portfolio.html', 'contact.html'];

const oldConfig = `        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            primary: '#48A9E8',
                            hover: '#171719',
                            accent: '#48A9E8', // Advrite primary
                        },
                        ui: {
                            bg: '#FFFFFF',
                            bgSec: '#F5F5FF',
                            textPrimary: '#17172B',
                            textSec: '#666680',
                        }
                    },
                    fontFamily: {
                        poppins: ['Poppins', 'sans-serif'],
                        inter: ['Inter', 'sans-serif'],
                    },
                    borderRadius: {
                        'btn': '20px',
                        'card': '20px',
                    }
                }
            }
        }`;

const newConfig = `        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: { primary: '#48A9E8', hover: '#171719', accentLav: '#FFD814' },
                        ui: { bg: '#FFFFFF', bgLightLav: '#F3F4F4', bgSoftLav: '#D2CFF2', textPrimary: '#161B2D', textSec: '#666680', textBlack: '#050609' }
                    },
                    fontFamily: { poppins: ['Poppins', 'sans-serif'], inter: ['Inter', 'sans-serif'] },
                    borderRadius: { 'btn': '20px', 'card': '20px' }
                }
            }
        }`;

// Also need to handle the one-liner tailwind configs in some files
const oldConfigOneLiner = `        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: { primary: '#48A9E8', hover: '#171719', accent: '#48A9E8' },
                        ui: { bg: '#FFFFFF', bgSec: '#F5F5FF', textPrimary: '#17172B', textSec: '#666680' }
                    },
                    fontFamily: { poppins: ['Poppins', 'sans-serif'], inter: ['Inter', 'sans-serif'] },
                    borderRadius: { 'btn': '20px', 'card': '20px' }
                }
            }
        }`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace Config
    if (content.includes(oldConfig)) {
        content = content.replace(oldConfig, newConfig);
    } else if (content.includes(oldConfigOneLiner)) {
        content = content.replace(oldConfigOneLiner, newConfig);
    }
    
    // Replace Classes
    content = content.replace(/bg-ui-bgSec/g, 'bg-ui-bgLightLav');
    content = content.replace(/bg-brand-accent/g, 'bg-brand-primary');
    
    // Special case for secondary buttons: "bg-ui-bgSec text-ui-textPrimary" -> "bg-ui-bgLightLav text-brand-hover hover:bg-ui-bgSoftLav"
    // In index.html, portfolio button: class="bg-ui-bgSec text-ui-textPrimary px-8 py-4 rounded-btn btn-text text-center hover:bg-brand-hover hover:text-white transition-colors duration-300"
    content = content.replace(/class="bg-ui-bgLightLav text-ui-textPrimary([^"]+)hover:bg-brand-hover hover:text-white([^"]+)"/g, 'class="bg-ui-bgLightLav text-brand-hover$1hover:bg-ui-bgSoftLav hover:text-brand-hover$2"');
    
    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated ' + file);
});

// Update style.css
const cssFile = path.join(__dirname, 'css', 'style.css');
let cssContent = fs.readFileSync(cssFile, 'utf8');
cssContent = cssContent.replace(/color: #17172B/g, 'color: #161B2D');
cssContent = cssContent.replace(/background-color: #48A9E8;\s*/g, '');
cssContent = cssContent.replace(/\.service-card:hover \.service-title \{\s*color: #FFFFFF;\s*\}\s*/g, '');
cssContent = cssContent.replace(/\.service-card:hover \.service-desc \{\s*color: rgba\(255, 255, 255, 0\.85\);\s*\}\s*/g, '');
// Make icon background primary on hover and icon white
cssContent = cssContent.replace(/\.service-card:hover \.service-icon-wrapper \{/g, '.service-card:hover .service-icon-wrapper {\n        background-color: #48A9E8;\n        color: #FFFFFF;');

fs.writeFileSync(cssFile, cssContent, 'utf8');
console.log('Updated css/style.css');
