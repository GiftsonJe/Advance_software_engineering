from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    result = eval(expression)
    return render_template('calculator.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)


