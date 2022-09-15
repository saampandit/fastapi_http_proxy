# 
FROM python:3.10.4

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY . /app

# 
CMD ["uvicorn", "app.main", "--host", "0.0.0.0", "--port", "8000"]

