from flask import Flask, render_template, request

app = Flask(__name__)

converter = {
    "KG": {
        "Weight in LB": lambda w: w / 0.454,
        "Weight in OZ": lambda w: (w * 16) / 0.454
    },
    "LB": {
        "Weight in KG": lambda w: w * 0.454,
        "Weight in OZ": lambda w: w * 16
    },
    "OZ": {
        "Weight in KG": lambda w: (w * 0.454) / 16,
        "Weight in LB": lambda w: w / 16
    },
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        unit = request.form.get("unit")
        weight = request.form.get("weight")

        try:
            weight = float(weight)
            if weight > 0 and unit in converter:
                result = {key: round(func(weight), 2)
                          for key, func in converter[unit].items()}
            else:
                result = {"Error": "Invalid input! Enter a valid number."}
        except ValueError:
            result = {"Error": "Invalid input! Enter a number."}
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
