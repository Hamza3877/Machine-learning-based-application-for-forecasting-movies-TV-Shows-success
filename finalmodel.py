import pandas as pd
from flask import Flask
from flask import request
import pickle
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

pima = pd.read_csv(r'F:\9 july 2021 fyp all files\dataset new\update scoll intern copy of check new se.csv',encoding='ISO-8859-1')


pima.drop(['name','rating','released','runtime','score','votes','year'],axis='columns',inplace=True)

inputs = pima.drop('success',axis='columns')
y = pima['success']



from sklearn.preprocessing import LabelEncoder


inputs_n = inputs[["budget","company","country","director","genre","star","writer"]]

le = LabelEncoder()

inputs_n["company_L_enc"]=le.fit_transform(inputs["company"])
inputs_n["country_L_enc"] = le.fit_transform(inputs["country"])
inputs_n["director_L_enc"] = le.fit_transform(inputs["director"])
inputs_n["genre_L_enc"] = le.fit_transform(inputs["genre"])
inputs_n["star_L_enc"] = le.fit_transform(inputs["star"])
inputs_n["writer_L_enc"] = le.fit_transform(inputs["writer"])
inputs_n.get

X=inputs_n.drop(['company','country','director','genre','star','writer'],axis='columns')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


dt= DecisionTreeClassifier(criterion="gini", max_depth=3)

gb= GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
    max_depth=1, random_state=0)

voting_clf = VotingClassifier(estimators=[ ('DecisionTree',dt), ('GradientBoost', gb)], voting='hard')



voting_clf.fit(X_train, y_train)

prediction = (voting_clf.predict([[10000000,1124,888,2736,380,2465,2121]]))

# prediction = (voting_clf.predict([[8000000,698,54,2272,1,2574,3839]]))




if prediction == 0:

    print("Flop")

else:
    print("Hit")

pred = voting_clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, pred))



# pickle.dump(voting_clf,open('finalmodel.pkl','wb'))
# model=pickle.load(open('finalmodel.pkl','rb'))



# flask api code below

# from flask import Flask
# from flask import request
# import pickle
#
# app = Flask(__name__)
#
#
#
# with open(r'/home/Hamza18359/mysite/finalmodel.pkl', 'rb') as file:
#     model = pickle.load(file)
#
#
# @app.route('/')
# def index_page():
#     print(__name__)
#     return "Hellow"
#
#
# @app.route('/predict', methods=["POST"])
# def predict_logic():
#     genre = int(request.form['Genre'])
#     director = int(request.form['Director'])
#     writer = int(request.form['Writer'])
#     star = int(request.form['Star'])
#     country = int(request.form['Country'])
#     productioncompany = int(request.form['Productioncompany'])
#     budget = float(request.form['Budget'])
#
#
#
#     print(genre)
#     print(director)
#     print(writer)
#     print(star)
#     print(country)
#     print(productioncompany)
#
#
#     pred_name = \
#     model.predict([[budget, productioncompany, country, director, genre, star, writer]]).tolist()[0]
#
#
#
#
#     if pred_name == 0:
#
#         pred_name = "Flop"
#
#
#     else:
#         pred_name = "Hit"
#
#     return (str(pred_name))
