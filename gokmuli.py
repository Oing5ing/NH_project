# server.py

from flask import Flask, request, jsonify
import sys

## DB용 라이브러리
import pymysql
import pandas as pd
import numpy as np
import re

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='Oing55555!',
                     db = 'NH_project',
                     use_unicode=True,
                     charset="utf8")

# 딥러닝
import DL

app = Flask(__name__)

# 나이
@app.route('/age', methods=['POST'])
def Age():
    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 나이 입력값
    content = content['action']
    content = content['params']
    content = int(re.sub('[^0-9]', '', content['age']))

    # DB로 전송
    cursor = db.cursor()
    sql = "INSERT INTO chatbot (id, age, calory, carbohydrate, protein, fat, sugars, dietaryfiber, sodium) VALUES('" + str(user_id) + "', " + str(content) +  ", 173.5, 37.887, 3.632, 0.556, 0.102, 1.68, 96.8);"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "age": content
            }
    }
    return jsonify(dataSend)

# 열량
@app.route('/calory', methods=['POST'])
def Calory():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['calory']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET calory =" + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "calory": content
            }
    }
    return jsonify(dataSend)


# 탄수화물
@app.route('/carbohydrate', methods=['POST'])
def Carbohydrate():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['carbohydrate']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET carbohydrate = " + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "carbohydrate": content
            }
    }
    return jsonify(dataSend)

# 단백질
@app.route('/protein', methods=['POST'])
def Protein():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['protein']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET protein =" + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "protein": content
            }
    }
    return jsonify(dataSend)

# 지방
@app.route('/fat', methods=['POST'])
def Fat():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['fat']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET fat =" + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "fat": content
            }
    }
    return jsonify(dataSend)

# 당류
@app.route('/sugars', methods=['POST'])
def Sugars():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['sugars']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET sugars =" + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "sugars": content
            }
    }
    return jsonify(dataSend)

# 식이섬유
@app.route('/dietaryfiber', methods=['POST'])
def DietaryFiber():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['dietaryfiber']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET dietaryfiber =" + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "data": {
            "dietaryfiber": content
            }
    }
    return jsonify(dataSend)

# 나트륨and 블랜딩응답
@app.route('/sodium', methods=['POST'])
def Sodium():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['botUserKey']
    # 사용자 입력값
    content = content['action']
    content = content['params']
    content = content['sodium']
    content = float(content.split(':')[1].split(',')[0])

    # DB로 전송
    cursor = db.cursor()
    sql = "UPDATE chatbot SET sodium =" + str(content) + "WHERE id = '" + str(user_id) + "';"
    cursor.execute(sql)
    db.commit()

    # DB에서 변수들 받아오기
    cursor = db.cursor()
    sql = "SELECT age, calory, carbohydrate, protein, fat, sugars, dietaryfiber, sodium FROM chatbot WHERE id = '" + str(user_id) + "' ;"
    cursor.execute(sql)

    user_input = cursor.fetchall() # DB에 저장한 유저입력값 가져오기

    # user_lst = []
    # for cell in user_input:
       # user_lst.append(list(cell)[0])

    # 딥러닝모델
    grain_percent = DL.deeplearning(user_input[0][0], user_input[0][1], user_input[0][2], user_input[0][3], user_input[0][4], user_input[0][5], user_input[0][6],user_input[0][7])
    grain_percent = grain_percent * 100

    dataSend = {
        "version": "2.0",
        "data": {
            "age": user_input[0][0],
            "calory": user_input[0][1],
            "carbohydrate": user_input[0][2],
            "protein": user_input[0][3],
            "fat": user_input[0][4],
            "sugars": user_input[0][5],
            "dietaryfiber": user_input[0][6],
            "sodium": user_input[0][7],
            "heugmi": str(np.round(np.array(grain_percent)[0][0], 2)),
            "hyeonmi": str(np.round(np.array(grain_percent)[0][1], 2)),
            "boli": str(np.round(np.array(grain_percent)[0][2], 2)),
            "chajo": str(np.round(np.array(grain_percent)[0][3], 2)),
            "gijang": str(np.round(np.array(grain_percent)[0][4], 2)),
            "yulmu": str(np.round(np.array(grain_percent)[0][5], 2)),
            "susu": str(np.round(np.array(grain_percent)[0][6], 2)),
            "chabssal": str(np.round(np.array(grain_percent)[0][7], 2)),
            "jeogdu": str(np.round(np.array(grain_percent)[0][8], 2)),
            "seolitae": str(np.round(np.array(grain_percent)[0][9], 2))
        }
    }
    return jsonify(dataSend)



if __name__ == "__main__":
    app.run(host='0.0.0.0') # Flask 기본포트 5000번

