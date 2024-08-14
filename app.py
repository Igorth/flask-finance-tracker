from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import csv
from datetime import datetime

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

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format=cls.FORMAT)

        start_date = datetime.strptime(start_date, cls.FORMAT)
        end_date = datetime.strptime(end_date, cls.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        filtered_df['date'] = filtered_df['date'].dt.strftime(cls.FORMAT)

        return filtered_df


@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Get data from form
        date = request.form['date']
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        CSV.add_entry(date, amount, category, description)
        flash('Transaction added successfully!', 'success')

    return render_template('add_transaction.html')


@app.route('/transactions', methods=['GET', 'POST'])
def view_transactions():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        df = CSV.get_transactions(start_date, end_date)
        transactions = df.to_dict(orient='records')

        return render_template('view_transactions.html', transactions=transactions)

    return render_template('view_transactions.html', transactions=[])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
