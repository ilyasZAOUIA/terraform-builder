# Archi Builder

A visual AWS architecture designer that generates Terraform.

- **Canvas editor**: drag AWS services from the palette, nest them (EC2 → subnet → VPC), connect them and edit their properties.
- **Terraform generation**: turns the diagram into `main.tf`, `variables.tf` and `outputs.tf`, wiring connected resources together.
- **Chat assistant** (optional): describe an architecture in plain language and get an editable diagram.

## Stack

| Layer    | Tech                                                        |
|----------|-------------------------------------------------------------|
| Frontend | React, Vite, TypeScript, React Flow, Tailwind, Framer Motion, Monaco |
| Backend  | FastAPI, Pydantic, Jinja2, SQLite                           |
| Infra    | Docker Compose, Nginx (optional Caddy for HTTPS)            |

## Quick start

```bash
cp .env.example .env        # optionally set ANTHROPIC_API_KEY
docker compose up -d --build
curl localhost/api/health
```

Then open `http://<host>/`.

> Full run, deploy and update instructions will be added once the app is complete.
