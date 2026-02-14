FROM python:3.11-slim

#directory selection 
WORKDIR /app

#package installation 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


#Final Execution 
CMD ["python", "-m", "app.main"]
