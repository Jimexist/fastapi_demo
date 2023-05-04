FROM python:3.10

WORKDIR /opt/server

COPY ./requirements.txt ./requirements.txt

RUN pip install \
  --no-cache-dir \
  --upgrade \
  --require-hashes \
  -r ./requirements.txt

COPY ./app /opt/server/app

EXPOSE 80

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
