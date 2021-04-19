FROM leehoseop/gpt2_lovecraft:1.0

WORKDIR /app
RUN pip install flask requests 

COPY . .

EXPOSE 80

CMD ["python3", "main.py"]
