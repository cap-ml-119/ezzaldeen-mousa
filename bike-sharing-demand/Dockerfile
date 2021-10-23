FROM python:3.8-slim-buster
WORKDIR /app
COPY /app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/src .

EXPOSE 80

CMD [ "python", "api.py" ]