from flask import Flask, render_template, request


@app.route("/circle_input")
def circle_input():
    return render_template("circle_input.html")

@app.route("/circle_result")
def circle_result():
    radius = int(request.args.get("radius"))
    result = 3.14 * radius ** 2
    return render_template("circle_resurt.html", result=result)