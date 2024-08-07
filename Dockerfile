FROM python:3.10
COPY . /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENV PORT=8080
EXPOSE $PORT
ENV GUNICORN_WORKER=2
RUN pip install gunicorn
ENV FLASK_APP=app.py
EXPOSE $PORT
CMD sh -c "gunicorn --bind 0.0.0.0:$PORT app:app"