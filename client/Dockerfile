# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "./app/merge.py"]
