from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from models import User
import databaseOperations as db
from flask_mail import Mail, Message  #pip install flask-mail

app = Flask(__name__)


# Configure Flask-Mail
# Gmail configuration with App Password
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # Port 465 for SSL
app.config['MAIL_USE_SSL'] = True  # Use SSL for port 465
app.config['MAIL_USE_TLS'] = False  # No TLS for port 465
app.config['MAIL_USERNAME'] = 'balkrishna.panthi.dev@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'jmyf degy mtsi ddyv'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'balkrishna.panthi.dev@gmail.com'  # Replace with your email

mail = Mail(app) 


@app.route('/')
#@app.route('/SignupSceens', methods=['POST'])
def home():     
    return render_template('Login.html')

@app.route('/send_email', methods=['POST'])
def send_email(): 
    data = request.get_json()
    param = data.get('param')
    
    try:
        msg = Message(
            'Hello',
            sender='balkrishna.panthi.dev@gmail.com',
            recipients=['balkrishnapanthi22@gmail.com']
        )
        msg.body = f'Your booking details for {param} will be sent shortly.'
        mail.send(msg)
        
        return jsonify({'status': 'success', 'message': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})
   
   



@app.route('/China')
def china():
    return render_template('China.html')

@app.route('/India')
def india():
    return render_template('India.html')

@app.route('/Nepal')
def nepal():
    return render_template('Nepal.html')

@app.route('/FirstPage')
def firstpage():
    return render_template('FirstPage.html')

@app.route('/Indonesia')
def indonesia():
    return render_template('Indonesia.html')

@app.route('/Malaysia')
def malaysia():
    return render_template('Malaysia.html')

@app.route('/Philippines')
def philippines():
    return render_template('Philippines.html')


@app.route('/Singapore')
def singapore():
    return render_template('Singapore.html')

@app.route('/SriLanka')
def srilanka():
    return render_template('SriLanka.html')




@app.route('/ChinaBook')
def chinabook():
    return render_template('ChinaBook.html')

@app.route('/IndonesiaBook')
def indonesiabook():
    return render_template('IndonesiaBook.html')

@app.route('/NepalBook')
def nepalbook():
    return render_template('NepalBook.html')

@app.route('/MalaysiaBook')
def malaysiabook():
    return render_template('MalaysiaBook.html')

@app.route('/PhilipipnesBook')
def philippinesbook():
    return render_template('PhilippinesBook.html')

@app.route('/SingaporeBook')
def singaporebook():
    return render_template('SingaporeBook.html')

@app.route('/SriLankaBook')
def srilankabook():
    return render_template('SriLankaBook.html')

@app.route('/IndiaBook')
def indiabook():
    return render_template('IndiaBook.html')







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