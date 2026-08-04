/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,css}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#F04B4C',
          hover: '#D93F40',
          accent: '#F04B4C',
        },
        ui: {
          bg: '#FFFFFF',
          bgSec: '#F9FAFB',
          textPrimary: '#2C2C2C',
          textSec: '#5F6368',
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
  },
  plugins: [],
}
