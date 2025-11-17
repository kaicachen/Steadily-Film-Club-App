# Stage 1: build
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install all dependencies (including dev)
RUN npm install --legacy-peer-deps

# Copy the rest of the app
COPY . .

# Build the Next.js app
RUN npm run build

# Stage 2: production image
FROM node:20-alpine AS runner
WORKDIR /app

# Copy production dependencies only
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

CMD ["npm", "start"]
