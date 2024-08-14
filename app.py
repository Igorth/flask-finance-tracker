from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add_transaction():
    return render_template('add_transaction.html')


@app.route('/view')
def view_transactions():
    return render_template('view_transactions.html')


if __name__ == '__main__':
    app.run(debug=True)
