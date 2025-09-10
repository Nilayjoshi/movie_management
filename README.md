Movie Management API

-> A simple FastAPI application to create, read, update, and delete movies. Includes Swagger documentation.

-> Features

1. Create a movie

2. List all movies

3. Get a specific movie by ID

4. Update a movie

5. Delete a movie

-> Swagger documentation at /docs

-> Tech Stack

1. Python 3.10+

2. FastAPI

3. SQLAlchemy

4. PostgreSQL

5. Pydantic v2

Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/Nilayjoshi/movie_management.git
cd movie_management

2️⃣ Create virtual environment
python -m venv .venv

3️⃣ Activate virtual environment

Windows

.venv\Scripts\activate


Mac/Linux

source .venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Create .env file
DATABASE_URL=postgresql://user:password@localhost:5432/moviedb

6️⃣ Run the application
uvicorn app.main:app --reload


Swagger UI: http://localhost:8000/docs

API Endpoints
Method	Endpoint	Description
POST	/movies/	Create a new movie
GET	/movies/	List all movies
GET	/movies/{movie_id}	Get details of a specific movie by ID
PUT	/movies/{movie_id}	Update an existing movie (partial updates allowed)
DELETE	/movies/{movie_id}	Delete a movie by ID

Example Movie JSON
{
  "title": "Interstellar",
  "director": "Christopher Nolan",
  "release_year": 2014,
  "genre": "Sci-Fi",
  "rating": 9
}
