from flask import Flask, render_template
from api import text_count_bp

app = Flask(__name__, static_folder='../front/dist/static', template_folder='../front/dist')
# app = Flask(__name__, static_folder='../front/public', template_folder='../front/public')
app.register_blueprint(text_count_bp)

# @app.route('/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()