from flask import Flask,request,render_template
import re


app=Flask(__name__)

#Route and functionality
@app.route('/', methods=['GET','POST'])
def index_fun():
    if request.method=='POST':
        r=0
        p = request.form["in_1"]
        s = request.form['in_2']
        pattern=re.compile(p)
        matches =[(ele.start(), ele.end()) for ele in re.finditer(pattern,s)]
        r=int(len(matches))
        return render_template('index.html', string=s, regex=p, match=matches, result=r)
    return render_template('index.html')

#run the app
if __name__=='__main__':
    app.run(debug=True)
