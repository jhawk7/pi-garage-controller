FROM python:3.9.16-alpine3.16 as base
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN apk update && apk add python3-dev gcc libc-dev
RUN pip3 install --no-cache-dir rpi.gpio

FROM base as app
EXPOSE 8080
WORKDIR app/
COPY . .
CMD ["./start_app.sh"]