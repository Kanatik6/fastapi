from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from models import Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get list
@app.get("/posts/", response_model=list[schemas.PostReturn])
async def read_posts(db: Session = Depends(get_db)):
    
    posts = crud.get_posts(db)
    return posts


# get retrieve
@app.get("/posts/{post_id}", response_model=schemas.PostReturn)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        JSONResponse({'message': f'Post with id:{post_id} is not found'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    return db_post


# create
@app.post("/posts/", response_model=schemas.PostReturn)
async def create_post(post: schemas.PostBase, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


# put
@app.put("/posts/{post_id}", response_model=schemas.PostReturn)
async def put_post(*, db: Session = Depends(get_db), post: schemas.PostCreate, post_id: int):
    
    db_post = crud.put_post(db=db, post=post, post_id=post_id)
    return db_post


# patch
@app.patch("/posts/{post_id}", response_model=schemas.PostReturn)
async def patch_post(*, db: Session = Depends(get_db), post: schemas.PostPatch, post_id: int):
    
    db_post = crud.patch_post(db=db, post=post, post_id=post_id)
    return db_post


# delete
@app.delete("/posts/{post_id}", response_model=schemas.PostReturn)
async def delete_post(*, db: Session = Depends(get_db), post_id: int):
    return crud.delete_post(db=db, post_id=post_id)

# --
# get list
@app.get('/authors/', response_model=list[schemas.AuthorReturn])
async def get_list(*, db: Session = Depends(get_db)):
    return crud.get_authors(db=db)


# get retrieve
@app.get('/authors/{author_id}', response_model=schemas.AuthorPostsReturn)
async def get_retrieve(*, db: Session = Depends(get_db), author_id: int):
    
    author = crud.get_author(db=db, author_id=author_id)
    if author:
        return author
    return JSONResponse({'message': f'Author with id:{author_id} is not found'}, 
                        status=status.HTTP_400_BAD_REQUEST)


# create
@app.post('/authors/', response_model=schemas.AuthorReturn)
async def create_author(*, db: Session = Depends(get_db), author: schemas.AuthorBase):
    return crud.create_author(db=db, author=author)


# put
@app.put('/authors/{author_id}', response_model=schemas.AuthorReturn)
async def put_author(*, db: Session = Depends(get_db), author: schemas.AuthorBase, author_id: int):
    return crud.put_author(db=db, author=author, author_id=author_id)


# patch
@app.patch('/authors/{author_id}', response_model=schemas.AuthorReturn)
async def patch_author(*, db: Session = Depends(get_db), author: schemas.AuthorPatch, author_id: int):
    return crud.patch_author(db=db, author=author, author_id=author_id)


# delete
@app.delete('/authors/{author_id}', response_model=schemas.AuthorReturn)
async def delete_author(*, db: Session = Depends(get_db), author_id: int):
    return crud.delete_author(db=db, author_id=author_id)
