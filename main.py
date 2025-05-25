from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from core.database import Base,engine
#init app



app = FastAPI()

app.mount('/static',StaticFiles(directory='static',),name='static')

Base.metadata.create_all(bind = engine)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app',reload=True)