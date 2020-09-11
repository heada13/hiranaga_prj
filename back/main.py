from flask import Flask, render_template

app = Flask(__name__, static_folder='../front/dist/static', template_folder='../front/dist')
# app = Flask(__name__, static_folder='../front/public', template_folder='../front/public')

@app.route('/')

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()