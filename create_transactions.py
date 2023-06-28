from db import db
from sqlalchemy.sql import text
import users

def get_income_categories():
    sql = text("SELECT income_name FROM income_categories")
    result = db.session.execute(sql)
    return result.fetchall()

def get_expense_categories():
    sql = text("SELECT expense_name FROM expense_categories")
    result = db.session.execute(sql)
    return result.fetchall()

def insert_income(amount, date, income_category, description): 
    user_id = users.user_id() 
    if user_id == 0:
        return False
    sql = text("INSERT INTO income (user_id, amount, date, income_category, description) VALUES (:user_id, :amount, :date, :income_category, :description)")
    db.session.execute(sql, {"user_id": user_id, "amount": amount, "date": date, "income_category": income_category, "description": description})
    db.session.commit()

def insert_expense(amount, date, expense_category, description):
    user_id = users.user_id() 
    if user_id == 0:
        return False
    sql = text("INSERT INTO expenses (user_id, amount, date, expense_category, description) VALUES (:user_id, :amount, :date, :expense_category, :description)")
    db.session.execute(sql, {"user_id": user_id, "amount": amount, "date": date, "expense_category": expense_category, "description": description})
    db.session.commit()

def valid_amount(amount):
    try:
        amount = float(amount)
        if len(str(amount).split('.')[-1]) > 2:
            return False
        if amount < 0:
            return False
        return True
    except ValueError:
        return False
