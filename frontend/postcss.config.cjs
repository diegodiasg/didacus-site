// postcss.config.cjs
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},   // <-- aqui o plugin dedicado
    autoprefixer: {},              // mantém o Autoprefixer
  }
}
