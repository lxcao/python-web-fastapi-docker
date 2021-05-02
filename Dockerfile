FROM python:3.9
RUN pip3 install fastapi uvicorn
COPY ./service /service
CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "15400"]