from app import app
from app.controller.movies import MovieRoutes


@app.before_request
def before_request():
    MovieRoutes.before_request()


@app.after_request
def after_request(response):
    MovieRoutes.after_request()
    return response


@app.route("/all_movies", methods=["GET"])
def all_movies():
    data = MovieRoutes.get_all()
    return {"data": data}


@app.route("/get_by_genre", methods=["GET"])
def get():
    data = MovieRoutes.get_by_genre()
    return {"data": data}


@app.route("/add", methods=["POST"])
def add():
    data = MovieRoutes.add_movie()
    return {"data": data}


@app.route("/update_title", methods=["PATCH"])
def update():
    data = MovieRoutes.update_movie()
    return {"data": data}


@app.route("/delete", methods=["DELETE"])
def delete():
    data = MovieRoutes.delete_movie()
    return {"data": data}
