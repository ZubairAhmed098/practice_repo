from flask import Flask

app = Flask(__name__)

@app.route('/track')
def track():
    return {'message': 'Tracking Page'}

@app.route('/about')
def about():
    return {'message' : 'About page, with fixes.'}

@app.route('/')
def home():
    return {'message' : 'Hello! Flask World'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
