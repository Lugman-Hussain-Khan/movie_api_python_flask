from flask import request
from app import db
from app.utils.marshmallow import company_schema
from app.models.Company import Company


class CompanyRoutes:
    def add_company():
        name = request.json["name"]
        country = request.json["country"]

        new_company = Company(name, country)

        db.session.add(new_company)
        db.session.commit()

        return {
            "msg": f"{name} added successfully",
            "data": company_schema.dump(new_company),
        }

    def get_company():
        id = request.args.get("id")
        data = company_schema.dump(Company.query.filter_by(id=id).first())

        return {"company": data}
