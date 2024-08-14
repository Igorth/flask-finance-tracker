# Finance Tracker

A finance tracking application built with Flask and Python. This application allows you to add, view, and filter financial transactions, and also provides instant feedback through success and error messages.

## Features

- **Add Transactions:** Add new financial transactions with date, amount, category, and description.
- **View Transactions:** View a list of transactions within a specific date range.
- **Flash Messages:** Receive instant feedback on actions performed, such as adding transactions.

## Requirements

- Python 3.x
- Flask
- pandas
- matplotlib

## Installation

1. **Clone the repository:**

```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
```
2. **Install the dependencies**:

Create a virtual environment and install the required libraries.

```bash
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Create the requirements.txt file**:

If you don't already have one, create a requirements.txt file with the following content:
```commandline
Flask
pandas
matplotlib
```

4. **Run the Flask application**:
```commandline
python app.py
The application will be available at http://127.0.0.1:5000/.
```

## Project Structure
- **app.py**: The main script that defines the routes and logic for the Flask application.
- **templates/**: Contains the HTML files for the application.
- **base.html**: Base template for the application's layout.
- **index.html**: The index page for the application
- **view_transactions.html**: The home page that displays the list of transactions and forms for adding and filtering transactions.
- **add_transaction.html**: Page for adding new transactions.
- **static/**: Contains static files such as CSS.
- **styles.css**: CSS file for application styles.
- **finance_data.csv**: CSV file where transactions are stored.

## Usage
### Adding Transactions
1. Go to the page to add a new transaction (/add).
2. Fill in the form with the date, amount, category, and description of the transaction.
3. Click "Add Transaction". A success message will be displayed, and you will be redirected to the main page.

### Viewing Transactions
1. Go to the main page (/transactions).
2. Use the form to filter transactions by date range.
3. Click "Filter". The filtered transactions will be displayed, and if there are any transactions within the range, the list will be updated.