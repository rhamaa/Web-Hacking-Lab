FROM redis:5.0.5

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install python curl netcat -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./start.sh /
RUN chmod +x /start.sh

EXPOSE 3333

ENTRYPOINT ["/start.sh"]
