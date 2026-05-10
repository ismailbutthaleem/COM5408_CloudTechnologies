FROM node:20 AS builder

WORKDIR /app/backend

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm prune --production

FROM node:20-alpine

WORKDIR /app/backend

COPY --from=builder /app/backend/ .

USER node

EXPOSE 5000

CMD ["node","server.js"]