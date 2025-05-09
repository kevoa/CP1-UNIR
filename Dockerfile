FROM python:3.9-slim

WORKDIR /usr/src/app

ENV PYTHONPATH /usr/src/app 

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.api
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD [ "python", "-m", "flask", "run" ]