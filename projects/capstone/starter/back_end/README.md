# Capstone Project: Star In Making Backend

## Getting Started

### Installing Dependencies

#### Python 3.9
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/back_end` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
- [jose] JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to find the application. 

## API Documentation
Here you can find authentication details, all existing endpoints, which methods can be used, how to work with them & example responses you´ll get.

### Authentication

- Casting Assistant:
A casting assistant is the lowest level of authority and is only permitted to view actors and movies.

Permissions:
get:actors | get:movies
get:home   | get:about
get:contact

- Casting Director
A casting director mid-level authority and is permitted to view actors and movies as well as deleting an actor or adding an actor in the database and lastly, modifying actors and movies.

Permissions:
get:actors    | get:movies 
get:home      | get:about
delete:actors | post:actors
patch:actors  | patch:movies
get:contact

- Executive Producer
The executive producer is the highest level of authority and is permitted to do any of the actions across the application.

Permissions:
get:home      | get:about
get:actors    | get:movies 
delete:actors | delete:movies 
post:actors   | post:movies
patch:actors  | patch:movies
get:contact

### Endpoints

GET '/'

- To get home page
- No request
- It returns "Welcome to Star in Making"

GET '/about'

- To get about page
- No request
- It returns "A Professional Casting Agency"

GET '/actors'

- First checks that the token provided is allowed to perform this operation. If authorized, then fetches a dictionary of actors.
- Request Arguments: token
- Returns: Each object in the actors dictionary and an object showing the total number of actors.
Sample: curl http://127.0.0.1:5000/actors

{
  "actors": [
      {
      "age": 22,
      "first_name": "Anny",
      "gender": "Female",
      "id": 1,
      "image_link": null,
      "last_name": "Smitha"
    },
    {
      "age": 38,
      "first_name": "Priyanka",
      "gender": "Female",
      "id": 17,
      "image_link": "https://pbs.twimg.com/profile_images/1356538427529904128/O_WwpJrT_400x400.jpg",
      "last_name": "Chopra Jonas"
       }
  ],
  "success": true,
  "total_actors": 2
}

POST '/actors'

- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the new actor namely the first_name, last_name, age, gender and image_link.
- Request Arguments: token
- Returns: An object containing the newly created actors's id, each object in the list of modified actors and an object showing the total number of actors.

Sample: curl http://127.0.0.1:5000/actors/add -X POST -H "Content-Type: application/json" -d '{"age": 32, "first_name": "Zain", "last_name": "Imam", "gender": "Male", "image_link": "https://www.instantstories.com/uploads/stories/zain-imam/zain-imam-latest-hd-images-5epd-lg.jpg?v=1569221647"}'

{
    "actors": [
        {
            "age": 32,
            "first_name": "Zain",
            "gender": "Male",
            "id": 14,
            "image_link": "https://www.instantstories.com/uploads/stories/zain-imam/zain-imam-latest-hd-images-5epd-lg.jpg?v=1569221647",
            "last_name": "Imam"
        }
    ],
    "success": true,
    "total_actors": 3


PATCH '/actors/<int:actor_id>'

- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the desired fields to be changes.
- Request Arguments: token, actor_id
- Returns: An object containing the updated actor.

Sample: curl http://127.0.0.1:5000/actors/1 -X PATCH -H "Content-Type: application/json" -d '{"age": 25}'

{
  "actors": [
    {
      "age": 25,
      "first_name": "Anny",
      "gender": "Female",
      "id": 1,
      "image_link": null,
      "last_name": "Smitha"
    }
    ],
  "success": true,
}

DELETE '/actors/<int:actor_id>'

- First checks that the token provided is allowed to perform this operation. If authorized, then takes in a actor ID, if the actor exists, then it is deleted from the database
- Request Arguments: token, actor_id
- Returns: The ID of the deleted actor and each object in the list of modified actors and an object showing the total number of actors.

Sample: curl http://127.0.0.1:5000/actors/1 -X DELETE

{
      "deleted": 1, 
      "success": true
  }

GET '/movies'

- First checks that the token provided is allowed to perform this operation. If authorized, then fetches a dictionary of movies.
- Request Arguments: token
- Returns: Each object in the movies dictionary and an object showing the total number of movies.

Sample: curl http://127.0.0.1:5000/movies

{
  "recent_movies": [
{
      "id": 5,
      "image_link": "https://resize.indiatvnews.com/en/resize/newbucket/715_-/2021/02/pjimage-34-1614420957.jpg",
      "release_date": "Fri, 26 Feb 2021 00:00:00 GMT",
      "title": "The Girl on The Train"
    },
    {
      "id": 6,
      "image_link": "https://m.media-amazon.com/images/M/MV5BZmYzMzU4NjctNDI0Mi00MGExLWI3ZDQtYzQzYThmYzc2ZmNjXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg",
      "release_date": "Fri, 26 Mar 2021 00:00:00 GMT",
      "title": "Godzilla vs. Kong"
    }
  ],
  "recent_movies_count": 2,
  "success": true,
  "total_movies": 4,
  "upcoming_movies": [
    {
      "id": 8,
      "image_link": "https://st1.photogallery.ind.sh/wp-content/uploads/indiacom/satyameva-jayate-2-202102-1612182947.jpg",
      "release_date": "Fri, 14 May 2021 00:00:00 GMT",
      "title": "Satyameva Jayate 2"
    },
    {
      "id": 7,
      "image_link": "https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Toofan_film_poster.jpg/220px-Toofan_film_poster.jpg",
      "release_date": "Fri, 21 May 2021 00:00:00 GMT",
      "title": "Toofan"
    }
    ],
  "upcoming_movies_count": 2
}

POST '/movies/add'

- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the new movie namely the title, release_date and image_link.
- Request Arguments: token
- Returns: An object containing the newly created movie's id, each object in the list of modified movies and an object showing the total number of movies.

Sample: curl http://127.0.0.1:5000/actors/add -X POST -H "Content-Type: application/json" -d '{ "title": "The Conjuring 3: The Devil Made Me Do It", "release_date": "Fri, 04 Jun 2021 00:00:00 GMT", "image_link": "https://1.bp.blogspot.com/-dMWqn6Tr5KU/XlJBeQgkcGI/AAAAAAAAAEU/7UMazYCaeQw9Ku3VrbRHcA58pa9udvLBwCLcBGAsYHQ/s640/The%2BConjuring%2BThe%2BDevil%2BMade%2BMe%2BDo%2BIt%2B%25282020%2529.jpg" }'

{
    "movies": [
        {
      "id": 9,
      "image_link": "https://1.bp.blogspot.com/-dMWqn6Tr5KU/XlJBeQgkcGI/AAAAAAAAAEU/7UMazYCaeQw9Ku3VrbRHcA58pa9udvLBwCLcBGAsYHQ/s640/The%2BConjuring%2BThe%2BDevil%2BMade%2BMe%2BDo%2BIt%2B%25282020%2529.jpg",
      "release_date": "Fri, 04 Jun 2021 00:00:00 GMT",
      "title": "The Conjuring 3: The Devil Made Me Do It"
    }

    ],
     "success": true,
    "total_movies": 5
}

PATCH '/movies/<int:movie_id>'

- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the desired fields to be changes.
- Request Arguments: token, movie_id
- Returns: An object containing the updated movie.

Sample: curl http://127.0.0.1:5000/movies/5 -X PATCH -H "Content-Type: application/json" -d '{"release_date":  "20-02-2021"}'

{
  "movies": [
    {
      "id": 5,
      "image_link": "https://resize.indiatvnews.com/en/resize/newbucket/715_-/2021/02/pjimage-34-1614420957.jpg",
      "release_date": "Sat, 20 Feb 2021 00:00:00 GMT",
      "title": "The Girl on The Train"
    }
    ],
  "success": true,
}

DELETE '/movies/<int:movie_id>'

- First checks that the token provided is allowed to perform this operation. If authorized, then takes in a movie ID, if the movie exists, then it is deleted from the database
- Request Arguments: token, movie_id
- Returns: The ID of the deleted movie and each object in the list of modified movies and an object showing the total number of movies.

Sample: curl http://127.0.0.1:5000/movies/5 -X DELETE

{
      "deleted": 5, 
      "success": true
  }


GET '/contact'

- To get home page
- No request
- It returns "Contact Us"


## Testing
To run the tests, run
```
dropdb capstone_test
createdb capstone_test
psql capsone_test < capstone.psql
python test_app.py