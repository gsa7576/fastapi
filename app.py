#pip install sqlalchemy alembic psycopg2-binary asyncpg
#pip install fastapi[all]


from fastapi import FastAPI

from api.auth import auth_router


app = FastAPI()
app.include_router(router=auth_router)