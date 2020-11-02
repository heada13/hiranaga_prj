# import functools

# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
# )
# # from werkzeug.security import check_password_hash, generate_password_hash

# # from flaskr.db import get_db

# # authという名前をbuleprintに登録。以後、/authはbpを引けば使える。
# bp = Blueprint('create', __name__)

# # 文字化け回避
# # bp.config['JSON_AS_ASCII'] = False

# @bp.route('/views/start', methods=('GET'))
# def create():
#     creQeustion = []

#     import json
#     import random

#     with open('/qestionList.json') as f:
#         l = f.read()
#         shuffleList = random.sample(l, len(l))

#     for i in range(15):
#         button = None
#         question = None
#         button = random.sample(shuffleList, 4)
#         question = random.choice(button.keys())
#         quesdict = {
#             "question":question,
#             "buttons":button
#             }
#         creQeustion.append(quesdict)
    
#     return jsonify(creQeustion)
