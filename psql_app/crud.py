from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

import models
import schemas
from sqlalchemy.orm import Session


# get list
def get_posts(db: Session):
    return db.query(models.PostModel).all()


# get retrieve
def get_post(db: Session, post_id: int):
    return db.query(models.PostModel).filter(
        models.PostModel.id == post_id).first()


# create
def create_post(db: Session, post: schemas.PostBase):
    db_post = models.PostModel(
        title=post.title,
        descriptions=post.descriptions,
        author_id=post.author_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


# put
def put_post(db: Session, post: schemas.PostCreate, post_id: int):
    db.query(models.PostModel).filter(
        models.PostModel.id == post_id).update(post.dict())
    db.commit()
    return db.query(models.PostModel).filter(models.PostModel.id == post_id).first()


# patch
def patch_post(db: Session, post: schemas.PostPatch, post_id: int):
    db.query(models.PostModel).filter(
            models.PostModel.id ==post_id).update(
            post.dict(exclude_unset=True))
    db.commit()
    return db.query(models.PostModel).filter(models.PostModel.id == post_id).first()


# delete
def delete_post(db: Session, post_id: int):
    post = db.query(models.PostModel).filter(
        models.PostModel.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return JSONResponse({"message": f'Post with id:{post_id} is deleted'}, status_code=status.HTTP_204_NO_CONTENT)
    return JSONResponse({"message":f"post with id {post_id} is not found"},status_code=status.HTTP_400_BAD_REQUEST)
# --

# get retrieve 
def get_author(db: Session, author_id):
    return db.query(models.AuthorModel).filter(models.AuthorModel.id == author_id).first()


# get list 
def get_authors(db: Session):
    return db.query(models.AuthorModel).all()


# create
def create_author(db: Session, author: schemas.AuthorBase):
    print(author.dict())
    author = models.AuthorModel(first_name=author.first_name,
                                last_name=author.last_name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


# put 
def put_author(db: Session, author: schemas.AuthorBase, author_id: int):
    db.query(models.AuthorModel).filter(
        models.AuthorModel.id == author_id).update(author.dict())
    db.commit()
    return db.query(models.AuthorModel).filter(models.AuthorModel.id == author_id).first()


# patch
def patch_author(db: Session, author: schemas.AuthorBase, author_id: int):
    db.query(models.AuthorModel).filter(models.AuthorModel.id ==
                                        author_id).update(author.dict(exclude_unset=True))
    db.commit()
    return db.query(models.AuthorModel).filter(models.AuthorModel.id == author_id).first()


# delete
def delete_author(db: Session, author_id: int):
    author = db.query(models.AuthorModel).filter(models.AuthorModel.id ==
                                        author_id).first()
    print(author)
    if author:
        db.delete(author)
        db.commit()
        return JSONResponse({"message": f'Author with id:{author_id} is deleted'}, status_code=status.HTTP_204_NO_CONTENT)
    return JSONResponse({"message":f"Author with id {author_id} is not found"},status_code=status.HTTP_400_BAD_REQUEST)
