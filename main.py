from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.api_log import inventario12
from router.api_negocio import api

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(inventario12)
app.include_router(api)
