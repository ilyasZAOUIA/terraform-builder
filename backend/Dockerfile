# ---- Stage 1: build wheels and fetch terraform ----
FROM python:3.12-slim AS builder
WORKDIR /build

COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# terraform binary, used only for `terraform fmt` on generated code.
ARG TF_VERSION=1.9.8
ARG TARGETARCH=amd64
RUN python - <<EOF
import io, urllib.request, zipfile, os
url = "https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_${TARGETARCH}.zip"
data = urllib.request.urlopen(url, timeout=120).read()
zipfile.ZipFile(io.BytesIO(data)).extract("terraform", "/build")
os.chmod("/build/terraform", 0o755)
EOF

# ---- Stage 2: runtime ----
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TF_IN_AUTOMATION=1 \
    TF_CLI_CONFIG_FILE=/dev/null

RUN useradd --create-home --uid 1000 app \
    && mkdir -p /data && chown app:app /data

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --no-index /wheels/* && rm -rf /wheels
COPY --from=builder /build/terraform /usr/local/bin/terraform

WORKDIR /srv
COPY app ./app

USER app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", \
     "--workers", "1", "--proxy-headers", "--forwarded-allow-ips", "*"]
