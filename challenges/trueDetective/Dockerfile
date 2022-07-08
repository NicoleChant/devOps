FROM python:3.8-slim

COPY . /
RUN pip install -r requirements.txt
RUN pwd
CMD ["uvicorn","app:app --reload"]
