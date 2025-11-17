# ---------- Base Image ----------
FROM python:3.11-slim AS base

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ---------- Install Dependencies ----------
FROM base AS deps

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# ---------- Copy App & Final Runtime ----------
FROM base AS final

# Create non-root user for security
RUN useradd -m appuser
USER appuser

COPY --from=deps /usr/local/lib/python3.11/ /usr/local/lib/python3.11/
COPY --from=deps /usr/local/bin/ /usr/local/bin/

COPY app ./app

EXPOSE 8000

# Start FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
