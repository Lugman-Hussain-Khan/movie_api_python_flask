from app import app
from app.controller.company import CompanyRoutes


@app.route("/get_company", methods=["GET"])
def all_companies():
    data = CompanyRoutes.get_company()
    return {"data": data}


@app.route("/add_company", methods=["POST"])
def addCompany():
    data = CompanyRoutes.add_company()
    return {"data": data}
