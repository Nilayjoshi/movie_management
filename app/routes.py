from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from . import models
from .schemas import MovieCreate, MovieOut, MovieUpdate
from .database import get_db, engine
import uuid
from sqlalchemy.exc import IntegrityError

router = APIRouter()

# Add table in DB.
@router.on_event("startup")
async def startup_event():
    models.Base.metadata.create_all(bind=engine)

@router.post("/movies", response_model=MovieOut)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db), summary="Create a new movie", description="Add a movie to the database with all details."):
    movie_id = str(uuid.uuid4()) 
    db_movie = models.Movie(id=movie_id, title=movie.title, director=movie.director, release_year=movie.release_year, genre=movie.genre, rating=movie.rating)
    db.add(db_movie)
    try:
        db.commit()
        db.refresh(db_movie)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid data: violates check constraint")
    return db_movie

@router.get("/movies", response_model=list[MovieOut], summary="List all movies", description="Retrieve a list of all movies stored in the database.")
def list_movies(db: Session = Depends(get_db)):
    db_movies = db.query(models.Movie).all()
    if not db_movies:
        raise HTTPException(status_code=404, detail="Movies not found")
    return db_movies

@router.get("/movies/{movie_id}", response_model=MovieOut)
def get_movie(movie_id: str, db: Session = Depends(get_db), summary="Get a movie by ID", description="Retrieve details of a specific movie using its unique ID."):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.put("/movies/{movie_id}", response_model=MovieOut)
def update_movie(movie_id: str, movie: MovieUpdate, db: Session = Depends(get_db), summary="Update a movie", description="Update fields of an existing movie identified by its ID."):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    for key, value in movie.model_dump(exclude_unset=True).items():
        setattr(db_movie, key, value)

    try:
        db.commit()
        db.refresh(db_movie)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid data: violates check constraint")
    return db_movie

@router.delete("/movies/{movie_id}", response_model=MovieOut)
def delete_movie(movie_id: str, db: Session = Depends(get_db), summary="Delete a movie", description="Delete a specific movie from the database using its ID."):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    db.delete(db_movie)
    db.commit()
    return Response(status_code=204)
