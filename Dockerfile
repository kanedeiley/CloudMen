FROM python:latest

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "webscraper.py", "mydb:3306"]
