FROM python:3.8.6
EXPOSE 8080
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY product_variable/.env .
CMD ["alembic", "upgrade", "head"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]