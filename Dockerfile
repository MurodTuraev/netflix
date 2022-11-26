FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install -r requariments.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]