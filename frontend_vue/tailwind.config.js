/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./src/**/*.vue', './public/index.html'],
  content: [],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

