# 
FROM python:3.10

# 
WORKDIR /home

# 
COPY ./requirements.txt /home/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt

# 
WORKDIR /home/app

# 
COPY ./app /home/app

# 
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]


