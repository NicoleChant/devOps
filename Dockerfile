FROM python:3
RUN mkdir -p /home/app
COPY . /home/app
RUN pip install -r requirements.txt
CMD ["uvicorn" , "app:app --reload"]
