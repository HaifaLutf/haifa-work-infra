# --- Stage 1: Build Stage ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies (if any were needed for C-extensions)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Copy requirements and install to a local directory
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# --- Stage 2: Final Runtime Stage ---
FROM python:3.11-slim

WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
# Copy your application code
COPY app.py .
COPY templates/ ./templates/
# Ensure the scripts in .local/bin are in the PATH
ENV PATH=/root/.local/bin:$PATH

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
