# frontend/Dockerfile
FROM node:20-slim

WORKDIR /app

# Copia pacotes e instala dependências
COPY package*.json ./
RUN npm install

# Copia o resto do código
COPY . .

# Expõe porta do Vite
EXPOSE 3000

# Comando padrão (modo dev, servindo em 0.0.0.0 para acesso externo)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]