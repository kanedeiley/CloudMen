FROM python:3.7-slim

RUN python -m pip install rasa

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
#CMD ["python", "json_converter.py"]

#COPY knowledge_base_data.json .

ENTRYPOINT ["rasa"]

RUN rasa train

VOLUME /app/models

CMD ["run","actions","run","-m","/app/models","--enable-api","--cors","*", "--debug", "--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]

