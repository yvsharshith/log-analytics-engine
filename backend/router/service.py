from config.sql_config import database_connection
from fastapi import FastAPI, HTTPException
from mysql.connector import Error

app = FastAPI()

@app.post("/create_user/")
def create_user(name: str, email: str, password: str):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "INSERT INTO tbluser(name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        db.commit()
        return {"message": "user created successfully"}
    
    except Error as e:
        print({"error": "cannot perform the operation"}, e)
    finally:
        cursor.close()
        db.close()

@app.get("/get_users/")
def get_user_by_id(user_id: int):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT id, name, email, password FROM tbluser WHERE id=%s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        return {"message": "user fetched successfully", "data": user}
    
    except Error as e:
        print({"error": "cannot perform the operation"}, e)
    finally:
        cursor.close()
        db.close()


@app.put("/update_users/")
def update_user(user_id: int, name: str, email: str):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "UPDATE tbluser SET name=%s, email=%s WHERE id=%s"
        cursor.execute(query, (name, email, user_id))
        db.commit()
        return {"message": "user updated successfully"}
    
    except Error as e:
        print({"error": "cannot perform the operation"}, e)
    finally:
        cursor.close()
        db.close()


@app.delete("/delete_users/")
def delete_user(user_id: int):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "DELETE FROM tbluser WHERE id=%s"
        cursor.execute(query, (user_id,))
        db.commit()
        return {"message": "user deleted successfully"}
    
    except Error as e:
        print({"error": "cannot perform the operation"}, e)
    finally:
        cursor.close()
        db.close()
