from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)

model_RF=pickle.load(open('RF_winner2.pkl', 'rb')) 
model_KNN=pickle.load(open('KNN_winner2.pkl', 'rb')) 
model_K_SVM=pickle.load(open('K_SVM_winner2.pkl', 'rb')) 
model_DT=pickle.load(open('DT_winner2.pkl', 'rb')) 
# model_NB=pickle.load(open('/content/drive/My Drive/NB_winner2.pkl', 'rb')) 




@app.route('/')
def home():
  return render_template("index.html")

   
#------------------------------About us-------------------------------------------
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')



@app.route('/internship')
def internship():
    return render_template('internship.html')

@app.route('/Blog')
def Blog():
    return render_template('Blog.html')
  

@app.route('/contact')
def contact():
    return render_template('contact.html')
  
@app.route('/predict',methods=['GET'])

def predict():
  T1= int(request.args.get('T1'))
  T2= int(request.args.get('T2'))
  C = float(request.args.get('C'))
  rl=int(request.args.get('rl'))
  bl=int(request.args.get('bl'))
  Tr=int(request.args.get('Tr'))
  CR=int(request.args.get('CR'))
  RR=int(request.args.get('RR'))
  Wl=int(request.args.get('Wl'))
  Model = (request.args.get('Model'))

  if Model=="Random Forest Classifier":
    prediction = model_RF.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])

  elif Model=="Decision Tree Classifier":
    prediction = model_DT.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])

  elif Model=="KNN Classifier":
    prediction = model_KNN.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])

  else:
    prediction = model_K_SVM.predict([[T1,T2,C,rl,bl,Tr,CR,RR,Wl]])

   
    
  if prediction == [1]:
    return render_template('index.html', prediction_text='Batting team Win the match', extra_text ="-> Prediction by " + Model)
    
  else:
    return render_template('index.html', prediction_text='Bowling team Win the match', extra_text ="-> Prediction by " + Model)

if __name__=="__main__":
  app.run(debug=True)
  
