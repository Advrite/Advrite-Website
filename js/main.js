// Enable CSS :active pseudo-classes on iOS Safari / touch devices
document.addEventListener('touchstart', function() {}, { passive: true });

// Mobile Menu Logic
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenuClose = document.getElementById('mobile-menu-close');
const mobileMenu = document.getElementById('mobile-menu');
const mobileLinks = document.querySelectorAll('.mobile-link');

function toggleMenu() {
    if (!mobileMenu) return;
    if (mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.remove('hidden');
        mobileMenu.classList.add('flex');
        document.body.style.overflow = 'hidden'; // Prevent scrolling behind menu
    } else {
        mobileMenu.classList.add('hidden');
        mobileMenu.classList.remove('flex');
        document.body.style.overflow = '';
    }
}

if (mobileMenuBtn && mobileMenuClose && mobileMenu) {
    mobileMenuBtn.addEventListener('click', toggleMenu);
    mobileMenuClose.addEventListener('click', toggleMenu);
    
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            toggleMenu();
        });
    });
}

// Contact Form Logic
const contactForm = document.getElementById('contact-form');
const successMessage = document.getElementById('form-success');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(contactForm);
        
        fetch(window.location.pathname, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(formData).toString()
        })
        .then(() => {
            contactForm.style.opacity = '0';
            setTimeout(() => {
                contactForm.classList.add('hidden');
                successMessage.classList.remove('hidden');
                successMessage.classList.add('flex');
            }, 300);
        })
        .catch((error) => alert('Something went wrong. Please try again.'));
    });
}

// Header Scroll Behavior
const mainNav = document.getElementById('main-nav');

if (mainNav) {
    const isDarkNav = mainNav.classList.contains('bg-transparent') || mainNav.classList.contains('bg-black') || mainNav.classList.contains('bg-black/40');
    
    const updateNavScroll = () => {
        if (isDarkNav) {
            const scrollY = window.scrollY;
            // Opacity starts at 0% and gradually scales with scroll up to exactly 85% maximum
            const opacity = Math.min(0.85, (scrollY / 200) * 0.85);
            mainNav.style.backgroundColor = `rgba(0, 0, 0, ${opacity})`;
            if (opacity > 0.01) {
                mainNav.style.backdropFilter = `blur(${Math.min(12, (opacity / 0.85) * 12)}px)`;
            } else {
                mainNav.style.backdropFilter = 'none';
            }
        } else {
            if (window.scrollY > 10) {
                mainNav.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
                mainNav.style.backdropFilter = 'blur(12px)';
                mainNav.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
            } else {
                mainNav.style.backgroundColor = '#FFFFFF';
                mainNav.style.backdropFilter = 'none';
                mainNav.style.boxShadow = 'none';
            }
        }
    };

    window.addEventListener('scroll', updateNavScroll, { passive: true });
    updateNavScroll();
}
