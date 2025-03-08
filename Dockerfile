# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install required packages
RUN pip install -U scikit-learn joblib

# Run the ML model script
CMD ["python", "ml-model.py"]
