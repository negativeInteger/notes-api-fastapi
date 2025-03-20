from fastapi import FastAPI
from app import routes

# create fastapi app instance
app = FastAPI(
    title='Notes API',
    version='1.0.0',
    description='A Notes API with JSON file storage'
)

app.include_router(routes.router)