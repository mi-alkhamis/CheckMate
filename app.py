# app.py

from flask import render_template
import config
from models import User, UserSchema

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    users = User.query.all()
    return render_template("home.html", users=users)

@app.route("/users")
def users():
    users = User.query.all()
    users_schema = UserSchema(many=True)
    return users_schema.dump(users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
