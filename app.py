from flask import Flask
from faker import Faker
from tools import file_action
from tools import get_user
from tools import csv_average
from tools import spaceman

app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h1>Hi, This Is My Homework</h1>"


@app.route("/requirements/")
def read_file() -> str:
    return "".join(f"<p>{str}</p>" for str in file_action.read_file().split("/n"))


@app.route("/generate-users")
@app.route("/generate-users/<int:amount>")
def generate_users(amount: int = 100) -> str:
    for i in range(amount):
        yield ''.join(f"<ol>{i + 1}: {get_user.User()}</ol>")


@app.route("/space")
def space() -> str:
    current_spaceman = spaceman.humans()
    iss_list = []
    tiangong_list = []
    for i in current_spaceman["people"]:
        for j in i.values():
            if j == "ISS":
                iss_list.append(i["name"])
            else:
                tiangong_list.append(i["name"])
    return (
        f'<p>spaceman: {current_spaceman["number"]}</p>'
        f'<p>ISS spaceman: {", ".join(iss_list)}</p>'
        f'<p>tiangong spaceman: {", ".join(tiangong_list)}</p>'
        )


@app.route("/mean")
def mean() -> str:
    return f"{csv_average.average()}"


if __name__ == "__main__":
    app.run(debug=True)
