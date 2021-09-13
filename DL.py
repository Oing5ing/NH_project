#!/usr/bin/env python
# coding: utf-8

# In[28]:


def deeplearning(u_age,kcal,carbo,protein,fat,sugars,fiber,natrium):
    # 라이브러리 불러오기 
    import pandas as pd
    import numpy as np
    import tensorflow as tf
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import StandardScaler
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.models import load_model

    PATH = '/home/ec2-user/project/NH_project'
    df = pd.read_csv(PATH + "grain+nutrition_fact_백미제외.csv", encoding='euc-kr')
    col_names= ['에너지(cal)', '탄수화물(g)', '단백질(g)', '지방(g)', '당류(g)',
           '식이섬유(g)', '나트륨(mg)', '흑미', '현미', '보리', '차조', '기장', '율무',
           '수수', '찹쌀', '적두', '서리태']
    df = df[col_names]

    feature_names = ['에너지(cal)', '탄수화물(g)', '단백질(g)', '지방(g)', '당류(g)', '식이섬유(g)', '나트륨(mg)']
    label_names = ['흑미', '현미', '보리', '차조', '기장', '율무', '수수', '찹쌀', '적두', '서리태']

    preference_df = pd.read_csv(PATH + '선호도_영양성분_벡터.csv', encoding='cp949')
    preference_df.set_index('(%)', inplace = True)
    preference_df1 = pd.read_csv(PATH + '나이대별_양곡선호도.csv', encoding='utf-8')
    preference_df1.set_index('(%)', inplace = True)

    ## 사용자 나이 입력 ##
    age = int(u_age)
    n = age // 10
    if n <= 3 :
        prefer = list(preference_df.loc['2030']/100)
        prefer1 = list(preference_df.loc['2030']/100)
        age1 = '2030'
    elif n == 4:
        prefer = list(preference_df.loc['40']/100)
        prefer1 = list(preference_df.loc['40']/100)
        age1 = '40'
    elif n == 5:
        prefer = list(preference_df.loc['50']/100)
        prefer1 = list(preference_df.loc['50']/100)
        age1 = '50'
    elif n >= 6:
        prefer = list(preference_df.loc['60세 이상']/100)
        prefer1 = list(preference_df.loc['60세 이상']/100)
        age1 = '60'

    feature_df = df[feature_names]
    label_df = df[label_names]

    for i in range(len(prefer)):
        feature_df[feature_names[i]] = feature_df[feature_names[i]] * prefer[i]
    for i in range(len(prefer1)):
        label_df[label_names[i]] = label_df[label_names[i]] * prefer1[i]  

    # X_scale
    scaler = MinMaxScaler().fit(feature_df)
    X_scaled = scaler.transform(feature_df)
    # y = label_df.values
    # %를 소수점으로 변환
    y = (label_df / 100).values

    model = load_model(PATH + 'model_' + age1 + '.h5')

    # kcal = 400
    # carbo = 25
    # protein = 5
    # fat = 0.5
    # sugars= 0
    # fiber = 0.5
    # natrium = 30
    ## 사용자 입력값 ##
    n = (kcal,carbo,protein,fat,sugars,fiber,natrium)

    test_x = np.array([n])
    test_x_prefer = []
    for i in range(len(test_x)):
        temp = []
        for j in range(len(prefer)):
            temp.append(test_x[i][j] * prefer[j])
        test_x_prefer.append(temp)

    test_x_scaled = scaler.transform(test_x_prefer)

    p = model.predict(test_x_scaled)

    return tf.nn.softmax(p)


# In[ ]:




