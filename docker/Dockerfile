# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ /app/src/

# Default command (for testing sensor script)
CMD ["python", "src/sensors/sensor_simulator.py"]