# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
COPY run.sh /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY baliqchi /app/baliqchi

# Expose port
EXPOSE 8000

# Run the entrypoint script
CMD ["./run.sh"]