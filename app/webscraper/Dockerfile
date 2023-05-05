FROM python:latest

COPY html_code.html .
COPY requirements.txt wait-for-it.sh /

RUN pip install --no-cache-dir -r requirements.txt

COPY webscraper.py /

CMD ["python", "webscraper.py", "mysqldb:3306"]
