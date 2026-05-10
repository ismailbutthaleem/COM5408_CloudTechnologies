FROM node:20 AS builder

WORKDIR /app/web

COPY package*.json ./

RUN npm install

COPY . .

RUN npm prune --production

FROM node:20-alpine

WORKDIR /app/web

COPY --from=builder /app/web/ .

EXPOSE 3000

CMD ["npm", "start"]