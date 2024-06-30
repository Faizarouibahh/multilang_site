module.exports = {
  content: [
    './main/templates/main/**/*.html', // Tous les fichiers HTML sous main/templates/main
    './static/js/**/*.js',             // Tous les fichiers JavaScript sous static/js
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1a202c',
        secondary: '#2d3748',
      },
      fontFamily: {
        sans: ['Graphik', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'), // Plugin pour les formulaires
  ],
}
