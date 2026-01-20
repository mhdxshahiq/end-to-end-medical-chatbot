# Use 3.10+ to satisfy 'unstructured' and 'langchain-google-genai' requirements
FROM python:3.10-slim-buster

WORKDIR /app

# Upgrade pip to ensure smooth installation of modern wheels
RUN pip install --no-cache-dir --upgrade pip

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# AWS Elastic Beanstalk / EC2 standard port
EXPOSE 8080

CMD ["python3", "app.py"]