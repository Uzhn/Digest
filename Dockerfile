FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

ENV FLASK_APP=main.py

EXPOSE 5000

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]