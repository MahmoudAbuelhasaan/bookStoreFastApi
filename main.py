from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from core.database import Base,engine
#init app

from api.book import router as book_router


app = FastAPI()



app.mount('/static',StaticFiles(directory='static',),name='static')

app.include_router(book_router)

Base.metadata.create_all(bind = engine)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app',reload=True)