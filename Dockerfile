# Build stage for installing dependencies
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Final stage with minimal image
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder . .

# Expose port and run command (same as before)
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
