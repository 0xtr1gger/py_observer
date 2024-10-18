FROM python:3.12
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 5000
CMD ["python3", "app.py"]