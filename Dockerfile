FROM python:3-alpine  
COPY . /  
CMD ["python3", "quiz.py"]