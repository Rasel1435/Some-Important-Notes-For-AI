from flask import Flask, request, jsonify, render_template
from pipelines import util

app = Flask(__name__)

# Route for serving the app.html file
@app.route('/')
def app_html():
    return render_template('app.html')


if __name__ == "__main__":
    print("Starting Python Flask Server...")
    app.run(debug=True)