FROM redis:5.0.5

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install python curl -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 3333

ENTRYPOINT ["python"]
CMD ["www/app.py"]
