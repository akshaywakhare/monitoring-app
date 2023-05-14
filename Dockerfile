FROM python:3.9-slim-buster

WORKDIR /app
COPY . . 
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask","run"]