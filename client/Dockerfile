FROM python:3.8-slim

COPY ./client /home/app

WORKDIR /home/app

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

CMD [ "uvicorn", "app:app", "--reload", "--host", "0.0.0.0" ]