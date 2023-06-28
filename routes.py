from app import app
from flask import render_template, request, redirect, session, url_for
import users, create_transactions, frontpage, report, budget
from history import get_transactions, delete_transaction, update_income, update_expense, get_transaction_by_id
import datetime

@app.route("/")
def index():
    username = users.get_username()
    total_income = frontpage.get_sum_of_income()
    total_expenses = frontpage.get_sum_of_expenses()
    savings_debt = frontpage.get_savings_or_debt()
    return render_template("index.html", message=username, total_income=total_income, total_expenses=total_expenses, savings_debt=savings_debt)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout() 
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if len(username) > 50:
            return render_template("error.html", message="Nimi saa olla korkeintaan 50 merkkiä pitkä")
        if len(username) == 0 or len(password1) == 0 or len(password2) == 0:
            return render_template("error.html", message="Käyttäjänimi tai salasana eivät voi olla tyhjiä")
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/create_income", methods=["GET", "POST"])
def create_income_route():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = request.form.get('amount')
        date = request.form.get('date')
        income_category = request.form.get('income_category')
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("error.html", message="Luvaton toiminto.")
        if len(description) > 50:
            return render_template("error.html", message="Kuvaus saa olla korkeintaan 50 merkkiä pitkä")
        if not create_transactions.valid_amount(amount):
            return render_template("error.html", message="Virheellinen summa! Muista, että desimaaleja saa olla korkeintaan kaksi.")
        date_real = datetime.datetime.strptime(date, '%Y-%m-%d')
        if not (date_real.year in range(2020, 2031)):
            return render_template("error.html", message="Vuoden pitää olla välillä 2020-2030")
        create_transactions.insert_income(amount, date, income_category, description)
        return redirect('/')
    else:
        income_categories = create_transactions.get_income_categories()
        return render_template('create_transactions.html', form_type='income', income_categories=income_categories)

@app.route("/create_expense", methods=["GET", "POST"])
def create_expense_route():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = request.form.get('amount')
        date = request.form.get('date')
        expense_category = request.form.get('expense_category')
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("error.html", message="Luvaton toiminto.")
        if len(description) > 50:
            return render_template("error.html", message="Kuvaus saa olla korkeintaan 50 merkkiä pitkä")
        if not create_transactions.valid_amount(amount):
            return render_template("error.html", message="Virheellinen summa! Muista, että desimaaleja saa olla korkeintaan kaksi.")
        date_real = datetime.datetime.strptime(date, '%Y-%m-%d')
        if not (date_real.year in range(2020, 2031)):
            return render_template("error.html", message="Vuoden pitää olla välillä 2020-2030")
        create_transactions.insert_expense(amount, date, expense_category, description)
        return redirect('/')
    else:
        expense_categories = create_transactions.get_expense_categories()
        return render_template('create_transactions.html', form_type='expense', expense_categories=expense_categories)
    
@app.route("/history", methods=["GET", "POST"])
def history():
    transaction_entries = get_transactions()
    entries = sorted(transaction_entries, key=lambda entry: entry.date, reverse=True)
    return render_template("history.html", entries=entries)

@app.route("/delete", methods=["GET", "POST"])
def delete_entry():
    table_name = request.form.get('table_name')
    id_entry = request.form.get('entry_id')
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Luvaton toiminto.")
    delete_transaction(table_name, id_entry)
    return redirect("/history")

@app.route("/edit", methods=["GET", "POST"])
def edit_route():
    if request.method == 'POST':
        table_name = request.form.get('table_name')
        id_entry = request.form.get('entry_id')
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("error.html", message="Luvaton toiminto.")
        if table_name == 'income':
            return redirect(url_for("edit_income", id_entry=id_entry))
        if table_name == 'expenses':
            return redirect(url_for("edit_expense", id_entry=id_entry))
        
@app.route("/edit_income", methods=["GET", "POST"])
def edit_income():
    if request.method == 'POST':
        id_entry = request.form.get('entry_id')
        transaction = get_transaction_by_id('income', id_entry)
        if session["csrf_token"] != request.form["csrf_token"]:
           return render_template("error.html", message="Luvaton toiminto.")
        description = request.form.get('description')
        amount = request.form.get('amount')
        date = request.form.get('date')
        income_category = request.form.get('income_category')
        if len(description) > 50:
            return render_template("error.html", message="Kuvaus saa olla korkeintaan 50 merkkiä pitkä")
        if not create_transactions.valid_amount(amount):
            return render_template("error.html", message="Virheellinen summa! Muista, että desimaaleja saa olla korkeintaan kaksi.")
        date_real = datetime.datetime.strptime(date, '%Y-%m-%d')
        if not (date_real.year in range(2020, 2031)):
            return render_template("error.html", message="Vuoden pitää olla välillä 2020-2030")
        update_income(id_entry, amount, date, income_category, description)
        return redirect('/history')
    else:
        id_entry = request.args.get('id_entry')
        transaction = get_transaction_by_id('income', id_entry)
        if transaction is None:
            return render_template("error.html", message="Tuloa ei löytynyt")
        income_categories = create_transactions.get_income_categories()
        return render_template('edit_transactions.html', form_type='income', income_categories=income_categories, transaction=transaction)

@app.route("/edit_expense", methods=["GET", "POST"])
def edit_expense():
    if request.method == 'POST':
        id_entry = request.form.get('entry_id')
        transaction = get_transaction_by_id('expenses', id_entry)
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("error.html", message="Luvaton toiminto.")
        description = request.form.get('description')
        amount = request.form.get('amount')
        date = request.form.get('date')
        expense_category = request.form.get('expense_category')
        if len(description) > 50:
            return render_template("error.html", message="Kuvaus saa olla korkeintaan 50 merkkiä pitkä")
        if not create_transactions.valid_amount(amount):
            return render_template("error.html", message="Virheellinen summa! Muista, että desimaaleja saa olla korkeintaan kaksi.")
        date_real = datetime.datetime.strptime(date, '%Y-%m-%d')
        if not (date_real.year in range(2020, 2031)):
            return render_template("error.html", message="Vuoden pitää olla välillä 2020-2030")
        update_expense(id_entry, amount, date, expense_category, description)
        return redirect('/history')
    else:
        id_entry = request.args.get('id_entry')
        transaction = get_transaction_by_id('expenses', id_entry)
        if transaction is None:
            return render_template("error.html", message="Menoa ei löytynyt")
        expense_categories = create_transactions.get_expense_categories()
        return render_template('edit_transactions.html', form_type='expense', expense_categories=expense_categories, transaction=transaction)
    
@app.route("/report", methods=["GET", "POST"])
def monthly_report():
    if request.method == 'POST':
        month = request.form.get('month')
        year = request.form.get('year')
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("error.html", message="Luvaton toiminto.")
        start_date, end_date = report.get_start_and_end_date(month, year)
        monthly_income, monthly_expenses, monthly_savings = report.monthly_transactions_report(start_date, end_date)
        monthly_category_expenses = report.monthly_category_report(start_date, end_date)
        monthly_budget, budget_savings = report.monthly_budget_report(start_date, end_date)
        category_budget_report = report.monthly_category_and_budget_report(start_date, end_date)
        return render_template('report.html', selected_month=month, selected_year=year, monthly_income=monthly_income, monthly_expenses=monthly_expenses, monthly_savings=monthly_savings, monthly_category_expenses=monthly_category_expenses, monthly_budget=monthly_budget, budget_savings=budget_savings, category_budget_report=category_budget_report)
    return render_template("report.html")

@app.route('/month_budget', methods=['POST'])
def handle_month_budget():
    month = request.form.get('month')
    year = request.form.get('year')
    budget_amount = request.form.get('amount')
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Luvaton toiminto.")
    if not create_transactions.valid_amount(budget_amount):
        return render_template("error.html", message="Virheellinen summa! Muista, että desimaaleja saa olla korkeintaan kaksi.")
    start_date, end_date = report.get_start_and_end_date(month, year)
    budget.insert_monthly_budget(start_date, end_date, budget_amount)
    return redirect('/create_budget')

@app.route('/category_budget', methods=['POST'])
def handle_category_budget():
    month = request.form.get('month')
    year = request.form.get('year')
    expense_category = request.form.get('expense_category')
    budget_amount = request.form.get('amount')
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("error.html", message="Luvaton toiminto.")
    if not create_transactions.valid_amount(budget_amount):
        return render_template("error.html", message="Virheellinen summa! Muista, että desimaaleja saa olla korkeintaan kaksi.")
    start_date, end_date = report.get_start_and_end_date(month, year)
    budget.insert_monthly_category_budget(start_date, end_date, expense_category, budget_amount)
    return redirect('/create_budget')

@app.route('/create_budget')
def create_budget_route():
    expense_categories = create_transactions.get_expense_categories()
    return render_template('budget.html', expense_categories=expense_categories)
