from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

with open('db.yaml', 'r') as f:
    db = yaml.safe_load(f)

app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Get form data
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    userType = request.form['userType']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    phone = request.form['phone']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zipCode = request.form['zipCode']

    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")
    print(f"User Type: {userType}")
    print(f"First Name: {firstName}")
    print(f"Last Name: {lastName}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Zip Code: {zipCode}")

    # Redirect to a success page or another route
    if userType == 'Admin':
        return redirect('/success')
    else: 
        return redirect('/success')

@app.route('/success')
def success():
    return "<h1>Sign Up Successful!</h1>"

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get form data
    userType = request.form['userType']
    username = request.form['username']
    password = request.form['password']

    # Add your login logic here (e.g., check username/password against database)

    # For demo purposes, let's just print the user type, username, and redirect to success page
    print(f"User Type: {userType}")
    print(f"Username: {username}")

    # Redirect to the success page
    return redirect('/success')



@app.route('/about/<username>')
def about(username):
    return f'<h1>This is about page of {username}</h1>'



@app.route('/room_details')
def room_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Room")  # Fetch all room details
    rooms_data = cur.fetchall()
    cur.close()
    #print(rooms_data)
    return render_template('room_details.html', rooms=rooms_data)


if __name__ == '__main__':
    app.run(debug=True)
