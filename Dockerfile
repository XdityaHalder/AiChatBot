FROM ubuntu:jammy

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt
CMD python3 AiChatBot.py
