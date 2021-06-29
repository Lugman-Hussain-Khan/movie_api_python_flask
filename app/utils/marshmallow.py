from app.models.Company import Company
from app.models.Movie import Movie
from app import ma


class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company

    id = ma.auto_field()
    name = ma.auto_field()
    country = ma.auto_field()
    movies = ma.auto_field()


class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        include_fk = True


company_schema = CompanySchema()

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
