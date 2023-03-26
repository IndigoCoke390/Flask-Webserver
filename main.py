import os
from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__)

@app.route("/")
def index():
    print("Available routes:" + "\n" + "\n".join([f"/{file}" for file in os.listdir("static")]))
    return redirect("/index.html")

@app.route("/<filename>")
def show_file(filename):
    if os.path.isfile(f"static/{filename}"):
        return send_from_directory('static', filename)
    return f"File '{filename}' not found."

if __name__ == "__main__":
    app.run()

