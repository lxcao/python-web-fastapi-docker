FROM python:3.9
RUN apt-get update
RUN apt-get install net-tools
RUN pip3 install fastapi uvicorn httpx pydantic
COPY ./interfaces /app/interfaces
COPY ./models /app/models
COPY ./services /app/services
COPY main.py /app/main.py
# CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "15400"]
CMD ["python3", "/app/main.py"]