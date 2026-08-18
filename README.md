# Student Management REST API

A simple beginner-friendly **REST API** built using **Python Flask** and **MySQL**.

This project demonstrates how to:

* Create a Flask REST API
* Connect Python Flask with MySQL
* Store student data in a MySQL table
* Retrieve data from MySQL using SQL queries
* Return MySQL data in JSON format
* Test APIs using Postman
* Install project dependencies using `requirements.txt`

---

## Project Architecture

The basic flow of this project is:

```text
Postman
   |
   | HTTP GET Request
   ↓
Flask API
   |
   | MySQL Connector
   ↓
MySQL Database
   |
   | SQL Query
   ↓
students Table
   |
   ↓
Flask
   |
   | JSON Response
   ↓
Postman
```

---

# 1. Technologies Used

| Technology      | Purpose                              |
| --------------- | ------------------------------------ |
| Python          | Programming language                 |
| Flask           | Web framework for creating REST APIs |
| MySQL           | Database                             |
| MySQL Connector | Connects Python with MySQL           |
| Postman         | API testing                          |
| Git             | Version control                      |
| GitHub          | Source code repository               |

---

# 2. Project Structure

```text
flask-project/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Flask application, MySQL connection and API routes.

### `requirements.txt`

Contains the Python packages required to run the project.

### `README.md`

Contains project documentation and setup instructions.

---

# 3. Prerequisites

Before running this project, make sure the following are installed:

1. Python
2. MySQL Server
3. MySQL Shell or MySQL Command Line Client
4. Postman
5. Git

Check Python installation:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

# 4. Clone the Repository

Clone the GitHub repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Go inside the project directory:

```bash
cd flask-project
```

---

# 5. Create a Virtual Environment

It is recommended to create a virtual environment for the project.

Create the virtual environment:

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

For Command Prompt:

```bash
venv\Scripts\activate
```

For PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

After activation, you should see something similar to:

```text
(venv)
```

at the beginning of your terminal.

---

# 6. Install Required Packages

This project uses `requirements.txt`.

Install all required packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
Flask
mysql-connector-python
```

You do not need to install these packages individually if you use:

```bash
pip install -r requirements.txt
```

---

# 7. Create MySQL Database

Open MySQL.

You can connect using:

```bash
mysql -u root -p
```

Enter your MySQL root password.

---

# 8. Create Database

Run:

```sql
CREATE DATABASE studentdb;
```

Select the database:

```sql
USE studentdb;
```

---

# 9. Create Students Table

Create the `students` table:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
```

---

# 10. Insert Sample Data

Insert some sample students:

```sql
INSERT INTO students (name, age, course)
VALUES
('Rahul', 20, 'Python'),
('Priya', 21, 'Java'),
('Amit', 22, 'Data Science');
```

Check the data:

```sql
SELECT * FROM students;
```

Expected result:

```text
+----+-------+-----+-------------+
| id | name  | age | course      |
+----+-------+-----+-------------+
|  1 | Rahul |  20 | Python      |
|  2 | Priya |  21 | Java        |
|  3 | Amit  |  22 | Data Science|
+----+-------+-----+-------------+
```

---

# 11. Configure MySQL Connection

Open `app.py`.

Find the MySQL connection:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="studentdb"
)
```

Replace:

```text
YOUR_MYSQL_PASSWORD
```

with your actual MySQL root password.

For example:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="studentdb"
)
```

**Important:** Never upload your real MySQL password to GitHub.

For a learning project, you can temporarily put the password directly in the code, but for real projects use environment variables.

---

# 12. Run the Flask Application

Make sure the virtual environment is activated.

Run:

```bash
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
* Debug mode: on
```

This means the Flask server is running.

---

# 13. API Endpoints

This project currently provides the following APIs:

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/students`      | Get all students         |
| GET    | `/students/<id>` | Get a particular student |

---

# 14. Get All Students

Open Postman.

Select:

```text
GET
```

Enter:

```text
http://127.0.0.1:5000/students
```

Click **Send**.

Expected response:

```json
[
    {
        "age": 20,
        "course": "Python",
        "id": 1,
        "name": "Rahul"
    },
    {
        "age": 21,
        "course": "Java",
        "id": 2,
        "name": "Priya"
    },
    {
        "age": 22,
        "course": "Data Science",
        "id": 3,
        "name": "Amit"
    }
]
```

The data shown in Postman is coming directly from the MySQL `students` table.

---

# 15. Get a Particular Student

To get a particular student, provide the student ID.

For example:

```text
GET http://127.0.0.1:5000/students/2
```

Expected response:

```json
{
    "age": 21,
    "course": "Java",
    "id": 2,
    "name": "Priya"
}
```

---

# 16. Student Not Found

If the requested ID does not exist:

```text
GET http://127.0.0.1:5000/students/100
```

The API returns:

```json
{
    "message": "Student not found"
}
```

The HTTP status code will be:

```text
404 Not Found
```

---

# 17. How the Code Works

## Flask Application

The application is created using:

```python
app = Flask(__name__)
```

This creates the Flask application.

---

## MySQL Connection

The following function connects Flask to MySQL:

```python
def get_db_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="studentdb"
    )

    return connection
```

The connection contains:

* `host` → MySQL server location
* `user` → MySQL username
* `password` → MySQL password
* `database` → Database to use

---

# 18. Get All Students API

The route is:

```python
@app.route("/students", methods=["GET"])
```

The SQL query is:

```sql
SELECT * FROM students
```

The result is converted into dictionaries using:

```python
cursor = connection.cursor(dictionary=True)
```

Finally, Flask converts the result into JSON:

```python
return jsonify(students)
```

---

# 19. Get Student by ID API

The route is:

```python
@app.route("/students/<int:id>", methods=["GET"])
```

For example:

```text
/students/2
```

The `2` is passed to the Python function as `id`.

The SQL query is:

```sql
SELECT * FROM students WHERE id = %s
```

The value is safely passed using:

```python
(id,)
```

This allows the API to retrieve a particular student.

---

# 20. Stopping the Flask Server

To stop the Flask server, press:

```text
CTRL + C
```

in the terminal.

---

# 21. Installing the Project on Another Computer

If someone downloads this project from GitHub, they do not need to manually install every Python package.

They only need to:

### Step 1

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2

Go inside the project:

```bash
cd flask-project
```

### Step 3

Create virtual environment:

```bash
python -m venv venv
```

### Step 4

Activate it:

```bash
venv\Scripts\activate
```

### Step 5

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 6

Create the MySQL database and table.

### Step 7

Configure the MySQL password in `app.py`.

### Step 8

Run Flask:

```bash
python app.py
```

### Step 9

Open Postman and test:

```text
GET http://127.0.0.1:5000/students
```

---

# 22. Troubleshooting

## MySQL Access Denied

If you get:

```text
Access denied for user 'root'@'localhost'
```

Check the username and password in `app.py`.

Make sure the password is the same password that you use when connecting to MySQL.

Test your MySQL login:

```bash
mysql -u root -p
```

---

## Database Does Not Exist

If you get an error related to `studentdb`, create it:

```sql
CREATE DATABASE studentdb;
```

Then:

```sql
USE studentdb;
```

---

## Table Does Not Exist

Create the table:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
```

---

## Flask Command Not Found

Make sure the virtual environment is activated and install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Port Already in Use

If port `5000` is already being used, change:

```python
app.run(debug=True)
```

to:

```python
app.run(debug=True, port=5001)
```

Then use:

```text
http://127.0.0.1:5001/students
```

in Postman.

---

# 23. Future Improvements

This project can be extended to a complete CRUD application.

Future APIs can include:

```text
GET     /students
GET     /students/<id>
POST    /students
PUT     /students/<id>
DELETE  /students/<id>
```

These would allow the application to:

* Create students
* Read students
* Update students
* Delete students

---

# 24. Learning Outcome

After completing this project, you should understand the basic flow of a REST API:

```text
Client
  ↓
HTTP Request
  ↓
Flask Route
  ↓
Python Function
  ↓
MySQL Query
  ↓
MySQL Database
  ↓
Python
  ↓
JSON Response
  ↓
Client/Postman
```

This project is intended as a beginner-level introduction to building a **Python Flask REST API connected to a MySQL database**.
