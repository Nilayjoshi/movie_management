from pydantic import BaseModel, Field
from typing import Optional

# Base class
class MovieBase(BaseModel):
    title: str
    director: str
    release_year: int
    genre: str
    rating: int

# Class to create Movies
class MovieCreate(MovieBase):
    pass

# Class to fetch Movies
class MovieOut(MovieBase):
    id: str
    
    model_config = {
        "from_attributes": True
    }

# Class to update Movies
class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    release_year: Optional[int] = None
    genre: Optional[str] = None
    rating: Optional[int] = None
