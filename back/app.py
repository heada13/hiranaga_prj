import os

from flask import Flask, render_template, jsonify
# from api import text_count_bp

app = Flask(__name__, static_folder='../front/dist/static', template_folder='../front/dist')
# app = Flask(__name__, static_folder='../front/public', template_folder='../front/public')
# app.register_blueprint(text_count_bp)

@app.route('/views/start')
def creatQestion():
    import json
    import random

    presufflelist = []
    shuffleList = []
    with open('questionList.json', 'r', encoding="utf-8") as f:
        fLoad = json.load(f)
        for i in fLoad.items():
            i_dict = {i[0]:i[1]}
            presufflelist.append(i_dict)
    shuffleList = random.sample(presufflelist, len(presufflelist))

    creQeustion = {"createQ":None}
    # qeslist = []
    # for i in range(15):
    button = ''
    question = ''
    button = random.sample(shuffleList, 4)
    q_dict = random.choice(button)
    question = list(q_dict.keys())[0]
    quesdict = {
        "question":question,
        "buttons":button
        }
    # qeslist.append(quesdict) 
    # print(qeslist)

    creQeustion.update(createQ = quesdict)

    return jsonify(creQeustion)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))