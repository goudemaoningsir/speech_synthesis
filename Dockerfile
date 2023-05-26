FROM sanmaomashi/python:3.9.16-ubuntu20.04

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1701"]