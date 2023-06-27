from db import db
from sqlalchemy.sql import text
import users

def insert_monthly_budget(start_date, end_date, budget_amount):
    user_id = users.user_id() 
    if user_id == 0:
        return False
    
    sql_existing_budget = text("SELECT * FROM monthly_budget WHERE user_id = :user_id AND start_date = :start_date AND end_date = :end_date")
    existing_budget = db.session.execute(sql_existing_budget, {"user_id": user_id, "start_date": start_date, "end_date": end_date}).fetchone()

    if existing_budget:
        sql_update = text("UPDATE monthly_budget SET budget_amount = :budget_amount WHERE id = :id")
        db.session.execute(sql_update, {"budget_amount": budget_amount, "id": existing_budget.id})
    else:
        sql_insert = text("INSERT INTO monthly_budget (user_id, budget_amount, start_date, end_date) VALUES (:user_id, :budget_amount, :start_date, :end_date)")
        db.session.execute(sql_insert, {"user_id": user_id, "budget_amount": budget_amount, "start_date": start_date, "end_date": end_date})

    db.session.commit()

def insert_monthly_category_budget(start_date, end_date, expense_category, budget_amount):
    user_id = users.user_id() 
    if user_id == 0:
        return False
    
    sql_existing_budget = text("SELECT * FROM category_budget WHERE user_id = :user_id AND start_date = :start_date AND end_date = :end_date AND expense_category = :expense_category")
    existing_budget = db.session.execute(sql_existing_budget, {"user_id": user_id, "start_date": start_date, "end_date": end_date, "expense_category": expense_category}).fetchone()

    if existing_budget:
        sql_update = text("UPDATE category_budget SET budget_amount = :budget_amount WHERE id = :id")
        db.session.execute(sql_update, {"budget_amount": budget_amount, "id": existing_budget.id})
    else:
        sql_insert = text("INSERT INTO category_budget (user_id, expense_category, budget_amount, start_date, end_date) VALUES (:user_id, :expense_category, :budget_amount, :start_date, :end_date)")
        db.session.execute(sql_insert, {"user_id": user_id, "expense_category": expense_category, "budget_amount": budget_amount, "start_date": start_date, "end_date": end_date})

    db.session.commit()
