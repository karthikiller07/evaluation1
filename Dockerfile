FROM python:3.8.3-alpine

WORKDIR /usr/src/work/

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/work
RUN pip install -r requirements.txt
COPY . /usr/src/work


EXPOSE 8000


ENTRYPOINT ["python","manage.py"]
CMD ["runserver","0.0.0.0:8000"]
