from flask import Flask,render_template,request
from quote import quote
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
@app.route('/generate',methods=['GET','POST'])
def quotes():
    if request.method=="GET":
        return render_template('form.html')
    else:
        search = request.form['author']
        number= int(request.form['number'])
        result = quote(search, limit=number)
        return render_template('form.html',quotes=result)
app.run(debug=True)