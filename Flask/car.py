from flask import Flask, request, render_template
import pickle
import numpy as np



app = Flask(__name__)
rfr=pickle.load(open('car1.pkl','rb'))
@app.route('/')
def home():
    return render_template('car1.html')

@app.route('/predict',methods=['POST'])
def y_predict():
   
    at = int(request.form["abtest"])
    vt = int(request.form["vehicleType"])
    gb = int(request.form["gearbox"])
    pps = int(request.form["powerPS"])
    m = int(request.form["model"])
    ft = int(request.form["fuelType"])
    b = int(request.form["brand"])
    nrd = int(request.form["notRepairedDamage"])
    pc = int(request.form["postalCode"])

    a=np.array([[at,vt,gb,pps,m,ft,b,nrd,pc]])
    print(a)
    result=rfr.predict(a)
    return render_template('car1.html',x=result)


if __name__ == "__main__":
    app.run()


