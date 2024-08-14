from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import csv

app = Flask(__name__)
app.secret_key = "sachin"  # Replace with your own secret key


class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']
    FORMAT = "%Y-%m-%d"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': float(amount),
            'category': category,
            'description': description,
            # Add more fields as needed (e.g., account, notes)
        }
        with open(cls.CSV_FILE, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        flash('Transaction added successfully!', 'success')
        print('Entry added successfully.')


@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Get data from form
        date = request.form['date']
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        CSV.add_entry(date, amount, category, description)
        return redirect(url_for('index'))
    return render_template('add_transaction.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view')
def view_transactions():
    return render_template('view_transactions.html')


if __name__ == '__main__':
    app.run(debug=True)
