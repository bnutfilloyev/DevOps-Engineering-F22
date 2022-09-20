FROM python:3.9

WORKDIR /code

COPY Lab /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY Lab /code/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
