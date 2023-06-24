from db import db
from sqlalchemy.sql import text
import users

def get_sum_of_income():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("SELECT COALESCE(SUM(amount), 0) FROM income WHERE user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    sum_of_income = result.fetchone()[0]
    formatted_sum_of_income = "{:.2f}".format(sum_of_income)
    return float(formatted_sum_of_income)

def get_sum_of_expenses():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    sum_of_expenses = result.fetchone()[0]
    formatted_sum_of_expenses = "{:.2f}".format(sum_of_expenses)
    return float(formatted_sum_of_expenses)

def get_savings_or_debt():
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("SELECT (SELECT COALESCE(SUM(amount), 0) FROM income WHERE user_id = :user_id) - (SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE user_id = :user_id)")
    result = db.session.execute(sql, {"user_id": user_id})
    savings_or_debt = result.fetchone()[0]
    formatted_savings_or_debt = "{:.2f}".format(savings_or_debt)
    return float(formatted_savings_or_debt)