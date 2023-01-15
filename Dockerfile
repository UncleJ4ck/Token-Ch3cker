FROM python:3.8-slim

RUN mkdir /checker
WORKDIR /checker

COPY scams.json .
COPY tokens.json .
COPY index.py .
COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "index.py"]

# docker build -t token-ch3ker:latest .
# docker run --name checker token-ch3ker
