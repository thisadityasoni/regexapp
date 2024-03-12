import re
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    if email:
        if re.match(email_pattern, email):
            return jsonify({'valid': True})
    return jsonify({'valid': False})

@app.route('/', methods=['GET', 'POST'])
def index_fun():
    if request.method == 'POST':
        r = 0
        p = request.form["in_1"]
        s = request.form['in_2']

        if p == "email":
            return render_template('index.html', string=s, regex=p)

        pattern = re.compile(p)
        matches = [(ele.start(), ele.end()) for ele in re.finditer(pattern, s)]
        r = len(matches)
        return render_template('index.html', string=s, regex=p, match=matches, result=r)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
