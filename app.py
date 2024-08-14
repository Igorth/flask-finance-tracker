from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

app = Flask(__name__)
# app.secret_key = 'your-secret-key'  # Replace with your own secret key

CSV_FILE = 'finance_data.csv'
COLUMNS = ['date', 'amount', 'category', 'description']  # Add more fields


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Get data from form
        date = request.form['date']
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']

        # Add transaction to database
        new_entry = {
            'date': date,
            'amount': float(amount),
            'category': category,
            'description': description,
            # Add more fields as needed (e.g., account, notes)
        }
        df = pd.DataFrame([new_entry])
        df.to_csv(CSV_FILE, mode='a', header=False, index=False)

        flash('Transaction added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_transaction.html')


@app.route('/view')
def view_transactions():
    return render_template('view_transactions.html')


if __name__ == '__main__':
    app.run(debug=True)
