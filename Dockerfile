# Use an official Python runtime as a parent image
FROM python:3.10-slim
Copy ./app
WORKDIR /app
RUN pip install requirements.txt
CMD python app.py




