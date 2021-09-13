#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from flask import Flask, request, jsonify
import json
import re 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"



@app.route("/message", methods=['POST'])
def Message():
    dataReceive = request.get_json()
    user_input = dataReceive['content']
    
    # 1) "잡곡 추천해줘"
    if u"추천" in user_input:
        age = ''
        kcal = ''
        nut1 = ''
        nut2 = ''
        nut3 = ''
        nut4 = ''
        nut5 = ''
        nut6 = ''
        response_data = {
            "message" : {
                "text" : "해당하는 연령대를 입력해주세요. (2030, 40, 50, 60 중에 입력)"
            }
        }
    
    # 2) 나이 입력
    elif u"2030" in user_input:
        age = 2030
        response_data = {
            "message" : {
                "text" : "칼로리를 입력해주세요. (100g 기준)"
            }
        }
    elif u"40" in user_input:
        age = 40
        response_data = {
            "message" : {
                "text" : "칼로리를 입력해주세요. (100g 기준)"
            }
        }
    elif u"50" in user_input:
        age = 50
        response_data = {
            "message" : {
                "text" : "칼로리를 입력해주세요. (100g 기준)"
            }
        }  
    elif u"60" in user_input:
        age = 60
        response_data = {
            "message" : {
                "text" : "칼로리를 입력해주세요. (100g 기준)"
            }
        } 
        
    # 3) 칼로리 입력
    elif u"kcal" in user_input:
        kcal = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "탄수화물을 입력해주세요. (100g 기준)"
            }
        }
    elif u"칼로리" in user_input:
        kcal = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "탄수화물을 입력해주세요. (100g 기준)"
            }
        }
    
    # 4) 탄수화물 입력
    elif u"탄수화물" in user_input:
        nut1 = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "단백질을 입력해주세요. (100g 기준)"
            }
        }
    
    # 5) 단백질 입력
    elif u"단백질" in user_input:
        nut2 = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "지방을 입력해주세요. (100g 기준)"
            }
        }
        
    # 6) 지방 입력
    elif u"지방" in user_input:
        nut3 = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "당류를 입력해주세요. (100g 기준)"
            }
        }
    
    # 7) 당류 입력
    elif u"당류" in user_input:
        nut4 = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "식이섬유를 입력해주세요. (100g 기준)"
            }
        }    
    
    # 8) 식이섬유 입력
    elif u"식이섬유" in user_input:
        nut5 = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "나트륨을 입력해주세요. (100g 기준)"
            }
        }        
    
    # 8) 나트륨 입력
    elif u"나트륨" in user_input:
        nut6 = int(re.sub('[^0-9]','',user_input))
        response_data = {
            "message" : {
                "text" : "입력하신 정보를 확인하시려면 '확인'을 입력해주세요."
            }
        }            
    
    # 9) 사용자 입력정보 확인
    elif u"확인" in user_input:
        result = "연령대: " + str(age) + "\n칼로리: " + str(kcal) + "\n탄수화물: " + str(nut1) + "\n단백질: " + str(nut2) + "\n지방: " + str(nut3) + "\n당류: " + str(nut4) + "\n식이섬유: " + str(nut5) + "\n나트륨: " + str(nut6)       
        response_data = {
            "message" : {
                "text" : "입력하신 정보는 \n" + result + "\n입니다." + "\n" + "해당 정보로 곡물비율을 추천받으시겠습니까? (y/n 입력)"
            }
        }
    
    # 10) 곡물비율 추천
    elif user_input == 'y':
        # 곡물비율 계산하는 알고리즘
        
        
        
        response_data = {
            "message" : {
                "text" : "추천 잡곡비율은 " + "\n" + recommedation + "\n" + '입니다.'
            }
        }
    
    # 잘못된 입력값을 받은 경우
    else:
        response_data = {
            'message' : {
                "text" : "이해할 수 없는 정보입니다" + "\n" + "처음으로 돌아가시려면 '추천'을" + "\n" + "입력하고자 하는 곡물로 돌아가시려면 해당곡물과 원하는 g을 입력하세요. (예: 탄수화물 50g)"
            }
        }
    
    return jsonify(response_data)


if __name__ == "__main__":
        app.run(host = '0.0.0.0', port = 8000)
