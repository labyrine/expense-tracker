from app import app
from flask import render_template, request, redirect
import users, create_transactions

@app.route("/")
def index():
    username = users.get_username()
    return render_template("index.html", message=username)

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
        create_transactions.insert_expense(amount, date, expense_category, description)
        return redirect('/')
    else:
        expense_categories = create_transactions.get_expense_categories()
        return render_template('create_transactions.html', form_type='expense', expense_categories=expense_categories)
    
@app.route("/history", methods=["GET", "POST"])
def history():
    return render_template("history.html")