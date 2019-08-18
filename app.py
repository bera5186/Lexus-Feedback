from flask import Flask, flash, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

        #print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message="Please enter required feilds")
        return render_template('sucess.html')

if __name__ == '__main__':
    app.debug = True
    app.run()