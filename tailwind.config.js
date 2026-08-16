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
          primary: '#7A7AFF',
          hover: '#31316B',
          accent: '#7A7AFF',
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
  },
  plugins: [],
}
