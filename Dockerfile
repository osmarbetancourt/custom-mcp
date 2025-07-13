

# Use official Python 3.10 image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (so orchestrator.py, config, etc. are available)
COPY . .

# Generate FastAPI code from OpenAPI spec at build time

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
