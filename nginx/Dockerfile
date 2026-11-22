# Build context: repository root (see docker-compose.yml).

# ---- Stage 1: build the frontend ----
FROM node:22-alpine AS build
WORKDIR /app

# Keep the build within the memory of a small host (swap covers peaks).
ENV NODE_OPTIONS=--max-old-space-size=768

COPY frontend/package.json frontend/package-lock.json* ./
RUN if [ -f package-lock.json ]; then npm ci --no-audit --no-fund; \
    else npm install --no-audit --no-fund; fi

COPY frontend/ ./
RUN npm run build

# ---- Stage 2: serve with nginx ----
FROM nginx:1.27-alpine
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://127.0.0.1/healthz || exit 1
