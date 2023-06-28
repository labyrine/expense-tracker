from db import db
from sqlalchemy.sql import text
import calendar
import users

def get_start_and_end_date(month, year):
    _, last_day = calendar.monthrange(int(year), int(month))
    start_date = f"{year}-{month}-01"
    end_date = f"{year}-{month}-{last_day}"
    return (start_date, end_date) 
 
def monthly_transactions_report(start_date, end_date):
    user_id = users.user_id()

    sql_income = text("SELECT COALESCE(SUM(amount), 0) FROM income WHERE user_id = :user_id AND date BETWEEN :start_date AND :end_date")
    result_income = db.session.execute(sql_income, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    month_income = result_income.fetchone()[0]

    sql_expenses = text("SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE user_id = :user_id AND date BETWEEN :start_date AND :end_date")
    result_expenses = db.session.execute(sql_expenses, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    month_expenses = result_expenses.fetchone()[0]

    sql_savings = text("SELECT (SELECT COALESCE(SUM(amount), 0) FROM income WHERE user_id = :user_id AND date BETWEEN :start_date AND :end_date) - (SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE user_id = :user_id AND date BETWEEN :start_date AND :end_date)")
    result_savings = db.session.execute(sql_savings, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    month_savings = result_savings.fetchone()[0]

    db.session.commit()

    return (month_income, month_expenses, month_savings)

def monthly_category_report(start_date, end_date):
    user_id = users.user_id()
    sql_category_expenses = text("SELECT expense_category, SUM(amount) AS total_expenses FROM expenses WHERE user_id = :user_id AND date BETWEEN :start_date AND :end_date GROUP BY expense_category HAVING SUM(amount) > 0")
    result_category_expenses = db.session.execute(sql_category_expenses, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    monthly_category_expenses = result_category_expenses.fetchall()

    total_expenses = sum(expenses for _, expenses in monthly_category_expenses)

    for i, (category, expenses) in enumerate(monthly_category_expenses):
        percentage = (expenses / total_expenses) * 100
        monthly_category_expenses[i] = (category, expenses, percentage)

    db.session.commit()
    return (monthly_category_expenses)

def monthly_budget_report(start_date, end_date):
    user_id = users.user_id()
    sql_budget = text("SELECT COALESCE(budget_amount, 0) FROM monthly_budget WHERE user_id = :user_id AND start_date = :start_date AND end_date = :end_date")
    result_budget = db.session.execute(sql_budget, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    row = result_budget.fetchone()
    month_budget = row[0] if row else 0

    sql_expenses = text("SELECT COALESCE(SUM(amount), 0) FROM expenses WHERE user_id = :user_id AND date BETWEEN :start_date AND :end_date")
    result_expenses = db.session.execute(sql_expenses, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    month_expenses = result_expenses.fetchone()[0]

    budget_savings = month_budget - month_expenses 

    db.session.commit()
    return (month_budget, budget_savings)

def monthly_category_and_budget_report(start_date, end_date):
    user_id = users.user_id()
    sql_report = text("""
        SELECT ec.expense_name AS category,
               cb.budget_amount AS budget,
               COALESCE(SUM(e.amount), 0) AS expenses,
               cb.budget_amount - COALESCE(SUM(e.amount), 0) AS savings
        FROM expense_categories ec
        INNER JOIN category_budget cb ON ec.expense_name = cb.expense_category
        LEFT JOIN expenses e ON ec.expense_name = e.expense_category
        WHERE cb.user_id = :user_id AND cb.start_date = :start_date AND cb.end_date = :end_date
        AND e.user_id = :user_id AND e.date BETWEEN :start_date AND :end_date
        GROUP BY ec.expense_name, cb.budget_amount
    """)
    result_report = db.session.execute(sql_report, {"user_id": user_id, "start_date": start_date, "end_date": end_date})
    category_budget_report = result_report.fetchall()

    db.session.commit()
    return category_budget_report
