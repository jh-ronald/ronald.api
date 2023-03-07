FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install openai

# Run app.py when the container launches
CMD ["python3", "ronald.py"]