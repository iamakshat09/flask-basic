from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="studentdb"
    )

    return connection

@app.route("/", methods=["GET"])
def default():
    data="<h1>Welcome to the Flask</h1>"
    return data

# Get all students
@app.route("/students", methods=["GET"])
def get_students():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(students)


# Get one student
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE id = %s",
        (id,)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    if student:
        return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)