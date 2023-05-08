FROM python:latest

COPY html_code.html /

COPY requirements.txt wait-for-it.sh /

RUN pip install --no-cache-dir -r requirements.txt

COPY webscraper.py /

RUN ["chmod", "+x", "wait-for-it.sh"]

CMD ["./wait-for-it.sh", "mysqldb:3306", "--timeout=300", "--", "python", "webscraper.py"]
