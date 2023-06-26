from app import app
from flask import render_template, request, redirect, session, url_for
import users, create_transactions, frontpage
from history import get_transactions, delete_transaction, update_income, update_expense, get_transaction_by_id

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
        update_expense(id_entry, amount, date, expense_category, description)
        return redirect('/history')
    else:
        id_entry = request.args.get('id_entry')
        transaction = get_transaction_by_id('expenses', id_entry)
        if transaction is None:
            return render_template("error.html", message="Menoa ei löytynyt")
        expense_categories = create_transactions.get_expense_categories()
        return render_template('edit_transactions.html', form_type='expense', expense_categories=expense_categories, transaction=transaction)
    
@app.route("/report")
def monthly_report():
    return render_template("report.html")
