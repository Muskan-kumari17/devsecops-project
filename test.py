from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecret123"   # Vulnerable: hardcoded secret

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Vulnerable: SQL Injection
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        user = cursor.fetchone()
        conn.close()

        if user:
            return "Login successful"
        else:
            return "Invalid credentials"

    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)   # Vulnerable: debug mode enabled
