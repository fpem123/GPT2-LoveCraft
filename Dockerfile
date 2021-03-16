FROM python:3.7

WORKDIR /app
RUN pip install flask requests
COPY . .

EXPOSE 80

CMD ["python3", "main.py"]
