FROM node:16.13.1-alpine

WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build && npm prune --production
ENV PORT 3000
EXPOSE 3000
CMD ["node", "build"]
