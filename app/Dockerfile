# Docker file to run fastapi and spark
FROM python:3.8

# Step 2: Install dependencies
RUN pip install fastapi uvicorn pyspark

# Step 3: Copy the application code
WORKDIR /app
COPY . /app

# Step 4: Set the entry point
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]