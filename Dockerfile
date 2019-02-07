FROM python:3
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LANG=en_AU.UTF-8
RUN mkdir /code
WORKDIR /code
# Ensures pip install is dependant on requirements file
COPY requirements.txt /code/ 
RUN pip install -r requirements.txt
COPY . /code/