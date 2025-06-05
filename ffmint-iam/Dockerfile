FROM python:3.11-slim

# Install uv package manager
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy pyproject.toml and install dependencies with --system
COPY pyproject.toml uv.lock ./
RUN uv pip install --system .

# Copy application code
COPY ./app ./app

# Copy entrypoint and prestart scripts, make them executable
COPY entrypoint.sh prestart.sh ./
RUN chmod +x ./entrypoint.sh ./prestart.sh

ENTRYPOINT ["/app/entrypoint.sh"]
