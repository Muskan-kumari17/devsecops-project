# Stage 1: Build stage
FROM python:3.10-slim as builder

WORKDIR /app

# Install dependencies into a local folder
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final Runtime stage (The "Hardened" part)
FROM python:3.10-slim-buster

# Create a non-root user for security (Principle of Least Privilege)
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy only the necessary files from the builder
COPY --from=builder /root/.local /home/appuser/.local
COPY . .

# Set environment variables
ENV PATH=/home/appuser/.local/bin:$PATH
ENV APP_HOST=0.0.0.0
ENV APP_PORT=5000

# Switch to the non-root user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
