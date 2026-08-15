const fs = require('fs');
const path = require('path');

const cssFile = path.join(__dirname, 'css', 'style.css');

const animations = `
/* About Page Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in-up {
    animation: fadeInUp 600ms ease-out forwards;
    opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
    .animate-fade-in-up {
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
    }
}

.stagger-1 { animation-delay: 100ms; }
.stagger-2 { animation-delay: 200ms; }
.stagger-3 { animation-delay: 300ms; }
.stagger-4 { animation-delay: 400ms; }
`;

fs.appendFileSync(cssFile, animations, 'utf8');
console.log('Appended animations to style.css');
