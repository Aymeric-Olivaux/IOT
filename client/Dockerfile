# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN sudo apt install python3-gpiozero
# 
COPY ./app /code/app

# 
CMD ["python3", "app/main.py"]


