from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    prefix='/user',
    tags=['Users']
    )
get_db = database.get_db

@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash.get_password_hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.showuser)
def get_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The user with id {id} not available')
    return user
