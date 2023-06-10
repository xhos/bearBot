FROM python:3.11.2

WORKDIR /.

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "bear.py"]