from db import db
from sqlalchemy.sql import text
import users

def get_transactions():
    user_id = users.user_id()
    sql = text("SELECT 'Tulo' AS type, date, description, amount, income_category, id FROM income WHERE user_id = :user_id UNION ALL SELECT 'Meno' AS type, date, description, amount, expense_category, id FROM expenses WHERE user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    return result.fetchall()

def delete_transaction(table_name, id_entry):
    user_id = users.user_id()
    if table_name == 'income':
        sql = text("DELETE FROM income WHERE id = :id_entry AND user_id = :user_id")
        db.session.execute(sql, {"id_entry": id_entry, "user_id": user_id})
    elif table_name == 'expenses':
        sql = text("DELETE FROM expenses WHERE id = :id_entry AND user_id = :user_id")
        db.session.execute(sql, {"id_entry": id_entry, "user_id": user_id})
    
    db.session.commit()

def update_income(id_entry, amount, date, income_category, description):
    sql = text("UPDATE income SET amount=:amount, date=:date, income_category=:income_category, description=:description WHERE id=:id_entry")
    db.session.execute(sql, {"amount": amount, "date": date, "income_category": income_category, "description": description, "id_entry": id_entry})
    db.session.commit()

def update_expense(id_entry, amount, date, expense_category, description):
    sql = text("UPDATE expenses SET amount=:amount, date=:date, expense_category=:expense_category, description=:description WHERE id=:id_entry")
    db.session.execute(sql, {"amount": amount, "date": date, "expense_category": expense_category, "description": description, "id_entry": id_entry})
    db.session.commit()

def get_transaction_by_id(table_name, id_entry):
    if table_name == 'income':
        sql = text("SELECT 'Tulo' AS type, date, description, amount, income_category, id FROM income WHERE id = :id_entry")
    elif table_name == 'expenses':
        sql = text("SELECT 'Meno' AS type, date, description, amount, expense_category, id FROM expenses WHERE id = :id_entry")
    result = db.session.execute(sql, {"id_entry": id_entry})
    return result.fetchone()