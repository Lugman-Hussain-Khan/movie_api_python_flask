from flask import request
from app import db
from app.utils.marshmallow import movie_schema, movies_schema
from app.models.Movie import Movie
from datetime import datetime
import json, time

init_req_time = 0


class MovieRoutes:

    # Before request method
    def before_request():
        global init_req_time
        init_req_time = time.time()

    # Add element to json file
    @classmethod
    def json_writer(cls, new_data, filename="log.json"):
        with open(filename, "r+") as file:
            file_data = json.load(file)
            file_data.update(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)

    # After Request
    def after_request():
        global init_req_time
        now = time.time()
        complete_now = datetime.now()
        new_data = {
            f"req_data_at_{complete_now}": {
                "req_host": request.host,
                "req_path": request.path,
                "req_method": request.method,
                "req_at": complete_now.strftime("%d/%m/%Y, %H:%M:%S"),
                "req_complete_time": now - init_req_time,
            }
        }
        MovieRoutes.json_writer(new_data)

    # Get Methods
    def get_by_genre():
        genre = request.args.get("g")
        data = movies_schema.dump(Movie.query.filter_by(genre=genre).all())
        print(request.url_rule)
        return data

    def get_all():
        data = movies_schema.dump(Movie.query.all())
        return {"all_movies": data}

    # Post Methods
    def add_movie():
        title = request.json["title"]
        genre = request.json["genre"]
        run_time = request.json["run_time"]
        company_id = request.json["company_id"]

        pre_exist = Movie.query.filter_by(title=title).first()

        if pre_exist != None:
            return {"msg": f"{title} already in db!"}

        new_movie = Movie(title, genre, run_time, company_id)

        db.session.add(new_movie)
        db.session.commit()

        return {"msg": "movie added", "movie": movie_schema.dump(new_movie)}

    # Update Methods
    def update_movie():
        new_title = request.json["new_title"]
        old_title = request.json["old_title"]

        movie = Movie.query.filter_by(title=old_title).first()

        if movie == None:
            return {"msg": f"No movie found with the name {old_title}"}

        movie.title = new_title
        db.session.commit()

        new_record = movie_schema.dump(Movie.query.filter_by(title=new_title).first())

        return {
            "msg": f"{old_title} updated with {new_title}",
            "new_record": new_record,
        }

    # Delete method
    def delete_movie():
        title = request.json["title"]

        movie = Movie.query.filter_by(title=title).first()
        if movie == None:
            return {"msg": f"No movie found with the name {title}"}
        db.session.delete(movie)
        db.session.commit()

        return {
            "msg": "Movie deleted successfully",
            "deleted_movie": movie_schema.dump(movie),
        }
