FROM python:3.10-bullseye
COPY requirements.txt /bot/
WORKDIR /bot
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "launcher.py"]