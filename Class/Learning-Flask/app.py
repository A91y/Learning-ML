from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/second")
def second():
    return render_template("new.html")


# print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
