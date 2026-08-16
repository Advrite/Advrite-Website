// Mobile Menu Logic
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenuClose = document.getElementById('mobile-menu-close');
const mobileMenu = document.getElementById('mobile-menu');
const mobileLinks = document.querySelectorAll('.mobile-link');

function toggleMenu() {
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
        link.addEventListener('click', toggleMenu);
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







// Header Scroll Behavior (Home Page Only)
const mainNav = document.getElementById('main-nav');

if (mainNav && mainNav.classList.contains('bg-transparent')) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            // Smoothly switch to darker opacity when away from top
            mainNav.style.backgroundColor = 'rgba(0, 0, 0, 0.85)';
        } else {
            // Smoothly return to initial zero opacity when at the very top
            mainNav.style.backgroundColor = 'rgba(0, 0, 0, 0)';
        }
    });
}
