FROM python:3.9-buster

RUN pip install requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]