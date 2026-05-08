# 1. Use a stable Python version
FROM python:3.10-slim

# 2. Set the working folder inside the container
WORKDIR /app

# 3. Copy your requirements file first
COPY requirements.txt .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your project files (Note the space between dots!)
COPY . .

# 6. Open port 5000 for web traffic
EXPOSE 5000
# 7. Start the Flask app correctly
CMD ["python", "app.py"]