from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/")
def top_page():
    return render_template("index.html")

if_name_ == "_name_":
    app.run(debug=True)
