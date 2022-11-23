FROM python:3-alpine3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
RUN python training.py
EXPOSE 3000
CMD python chatbot.py 