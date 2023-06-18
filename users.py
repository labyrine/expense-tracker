from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    session.pop("user_id", None)

def register(username, password):
    if len(username) == 0 or len(password) == 0:
        return False
    
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def get_username():
    if "user_id" in session:
        user_id = session["user_id"]
        sql = text("SELECT username FROM users WHERE id=:id")
        result = db.session.execute(sql, {"id": user_id})
        user = result.fetchone()
        if user:
            return user.username
    return None

def user_id():
    return session.get("user_id",0)

