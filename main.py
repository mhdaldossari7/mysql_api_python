import pymysql
from app import app
import mysql.connector
from flask import jsonify, flash, request
from django.http import HttpResponse


@app.route("/userID", methods=["POST"])
def send_user_id():
    try:
        _json = request.json
        _user_id = _json["user_id"]

        # insert record in database
        sqlQuery = "INSERT INTO usersInfo(user_id) VALUES(%s)"
        data = (_user_id, )
        conn = mysql.connector.connect(user="root",
                                       password="root",
                                       database="post_notifications")
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        resp = {
            "data": {
                "user_id": _user_id
            },
            "success": True,
            "message": "Added"
        }
        res = jsonify(resp)
        res.status_code = 200

        return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/userID", methods=["DELETE"])
def delete_user_id():
    try:
        _json = request.json
        _user_id = _json["user_id"]

        sqlQuery = "DELETE FROM usersInfo WHERE user_id = %s"
        data = (_user_id, )
        conn = mysql.connector.connect(user="root",
                                       password="root",
                                       database="post_notifications")
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        resp = {
            "data": {
                "user_id": _user_id
            },
            "success": True,
            "message": "Deleted"
        }
        res = jsonify(resp)
        res.status_code = 200

        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/userID", methods=["GET"])
def get_user_id():
    try:
        _json = request.json
        _user_id = _json["user_id"]

        sqlQuery = "SELECT user_id FROM usersInfo WHERE user_id = %s"
        data = (_user_id, )
        conn = mysql.connector.connect(user="root",
                                       password="root",
                                       database="post_notifications")
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        result = cursor.fetchall()
        print(len(result))
        if len(result) > 0:
            res = jsonify("The user id is already stored in database.")
            res.status_code = 200
            return res
        else:
            res = jsonify("The user id is not stored in the database.")
            res.status_code = 200
            return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/userID/<int:user_id>", methods=["GET"])
def get_passed_user_id(user_id):
    try:
        sqlQuery = "SELECT user_id FROM usersInfo WHERE user_id = %s"
        data = (user_id, )
        conn = mysql.connector.connect(user="root",
                                       password="root",
                                       database="post_notifications")
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        result = cursor.fetchall()
        if len(result) > 0:
            res = jsonify("The user is is already stored in database.")
            res.status_code = 200
            return res
        else:
            res = jsonify("The user id is not stored in the database.")
            res.status_code = 200
            return res

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()
