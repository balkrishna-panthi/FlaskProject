from flask import Flask, render_template, redirect, url_for, request, make_response
from models import User
import databaseOperations as db

app = Flask(__name__)

@app.route('/')
#@app.route('/SignupSceens', methods=['POST'])
def home():   
    return render_template('SignupSceens.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():    
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        middle_name = request.form.get('middleName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User (first_name, middle_name, last_name, email, password)

        # After processing the form, redirect or render a new page
        return render_template('SignupSceens.html')  # You can redirect or display a success message

    return render_template('SignupSceens.html')

@app.route('/China')
def china():
    return render_template('China.html')

@app.route('/ChinaBook')
def chinabook():
    return render_template('ChinaBook.html')

@app.route('/FirstPage')
def firstpage():
    return render_template('FirstPage.html')

@app.route('/Indo')
def indo():
    return render_template('Indo.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        allUsers = db.getAllUsers()
        if any(user.email == email and user.password == password for user in allUsers):
              # Create a response object
            response = make_response(redirect(url_for('firstpage')))  # Redirect after successful login
            
            # Set a cookie with the user's email
            response.set_cookie('email', email)  # You can also set expiry or secure flag here if needed
            
            return response  # Return the response object with the cookie
        else:
            error_message = "Invalid email or password."  # Error message if login fails
            return render_template('Login.html', error_message=error_message)  # Show error on the login page
    return render_template('Login.html')

@app.route('/Malaysia')
def malasiya():
    return render_template('Malaysia.html')

@app.route('/Philipines')
def philipines():
    return render_template('Philipines.html')

# @app.route('/SignupSceens')
# def signupsceens():
#     return render_template('SignupSceens.html')

@app.route('/Singapore')
def singapore():
    return render_template('Singapore.html')

@app.route('/setcookie')
def set_cookie():
    # Create a response object
    response = make_response("Cookie has been set!")
    
    # Set a cookie with a name 'username' and value 'JohnDoe'
    response.set_cookie('username', 'JohnDoe')
    
    # Return the response
    return response

if __name__ == '__main__':
    app.run(debug=True)