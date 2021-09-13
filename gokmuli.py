# server.py

from flask import Flask, request, jsonify
import sys

## DB용 라이브러리
import pymysql
import pandas as pd
import numpy as np

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
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']   
    # 나이 입력값
    content = content['action']
    content = content['params']
    content = int(content['age'])

    # DB로 전송
    cursor = db.cursor()
    sql = "INSERT INTO chatbot (id, age, calory, carbohydrate, protein, fat, sugars, dietaryfiber, sodium) VALUES('" + str(user_id) + "', " + str(content) +  ", 173.5, 37.887, 3.632, 0.556, 0.102, 1.68, 96.8);"
    cursor.execute(sql)
    db.commit()

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "열량은 얼마나 섭취하고 싶으신가요?\n(100g 기준. 97~358kcal 사이의 값을 입력해주세요.)"                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 열량
@app.route('/calory', methods=['POST'])
def Calory():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "탄수화물은 얼마나 섭취하고 싶으신가요?\n(100g 기준. 21.09~78.84g사이의 값을 입력해주세요.)"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 탄수화물
@app.route('/carbohydrate', methods=['POST'])
def Carbohydrate():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "단백질은 얼마나 섭취하고 싶으신가요?\n(100g 기준. 2.02~8.52g 사이의 값을 입력해주세요.)"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 단백질
@app.route('/protein', methods=['POST'])
def Protein():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "지방은 얼마나 섭취하고 싶으신가요?\n(100g 기준. 0.19~1.06g 사이의 값을 입력해주세요.)"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 지방
@app.route('/fat', methods=['POST'])
def Fat():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "당류는 얼마나 섭취하고 싶으신가요?\n(100g 기준. 0~0.46g 사이의 값을 입력해주세요.)"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 당류
@app.route('/sugars', methods=['POST'])
def Sugars():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "식이섬유는 얼마나 섭취하고 싶으신가요?\n(100g 기준. 0.1~8.4g 사이의 값을 입력해주세요.)"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 식이섬유
@app.route('/dietaryfiber', methods=['POST'])
def DietaryFiber():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "나트륨은 얼마나 섭취하고 싶으신가요?\n(100g 기준. 0.001~0.459g 사이의 값을 입력해주세요.)"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)

# 나트륨and 블랜딩응답
@app.route('/sodium', methods=['POST'])
def Sodium():

    content = request.get_json()
    # 사용자 고유 id
    user_id = content['userRequest']['user']['properties']['plusfriendUserKey']
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
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type" : "basicCard",
                        "items": [
                            {
                                "title" : "",
                                "description" : "모든 응답을 완료했습니다.\n현재 선택하신 내용은 "+ "\n나이: " + str(user_input[0][0])+'세'+"\n열량: " + str(user_input[0][1])+'kcal'+"\n탄수화물: " + str(user_input[0][2])+'g'+ "\n단백질: " + str(user_input[0][3])+'g'+"\n지방: " + str(user_input[0][4])+'g'+"\n당류: " + str(user_input[0][5])+'g'+"\n식이섬유: " + str(user_input[0][6])+'g'+"\n나트륨: " + str(user_input[0][7])+'g'+"\n입니다.\n선택하신 내용에 맞게 추천된 블랜딩 비율은 \n 흑미 " + str(np.array(grain_percent)[0][0])  + " % \n 현미 " + str(np.array(grain_percent)[0][1]) + "% \n 보리 " + str(np.array(grain_percent)[0][2]) + "% \n 차조 " + str(np.array(grain_percent)[0][3]) + "% \n 기장 " + str(np.array(grain_percent)[0][4]) + "% \n 율무 " + str(np.array(grain_percent)[0][5]) + "% \n 수수 " + str(np.array(grain_percent)[0][6]) + "% \n 찹쌀 " + str(np.array(grain_percent)[0][7]) + "% \n 적두 " + str(np.array(grain_percent)[0][8]) + "% \n 서리태 " + str(np.array(grain_percent)[0][9]) + "% \n 입니다."                           }
                        ]
                    }
                }
                        ]
                    }
                }
    return jsonify(dataSend)



if __name__ == "__main__":
    app.run(host='0.0.0.0') # Flask 기본포트 5000번

