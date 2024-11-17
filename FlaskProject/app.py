from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify, g
from models import User
import databaseOperations as db
from flask_mail import Mail, Message  #pip install flask-mail
from datetime import datetime

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

@app.before_request
def before_request():
    email = request.cookies.get('email')  # Get the user's email from the cookie
    if email:
        g.fullname = db.getFullNameFromEmail(email)  # Retrieve the user's fullname using the email
        g.logText = 'Logout'
        g.loginroute = 'logout'
    else:
        g.fullname = None  # Set as None or Guest if the user is not logged in
        g.logText = 'Login'
        g.loginroute = 'login'

@app.route('/')
#@app.route('/SignupSceens', methods=['POST'])
def home():     
    return render_template('Login.html')

@app.route('/make_booking', methods=['POST'])
def make_booking(): 
    try:
        data = request.get_json()
        place = data.get('param')
        booking_date = datetime.now()
        email = get_cookie()
        print(f'Email from cookie: {email}')  # Print email to check its value
       # print('cookie + : ' + email)
        if  email is None:
            print('if block hit')
            return jsonify({'status': 'error', 'error': str('User not found. Please log in.')}), 400
        
        name = db.getUserNameFromEmail(email)
        db.insertBookingRecords(email, place)
        send_email(place, email, name ,booking_date)
        return jsonify({'status': 'success', 'message': 'Booked'})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})


@app.route('/send_email', methods=['POST'])
def send_email(place, email, name, booking_date):
    try:
        if not email:
            raise ValueError('Please sign up/login.')
        msg = Message(
            f'Booking details for {place}',
            sender='Explore Asia',
            recipients=[email]
        )
        msg.body = f'Your booking details for {place} will be sent shortly.'
        msg.html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
            <h2>Your Booking Details</h2>
            <p>Dear {name},</p>
            <p>Thank you for booking with us. Below are your booking details:</p>

            <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                <tr>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #4CAF50; color: white;">Name</th>                   
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #4CAF50; color: white;">Booking Date</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #4CAF50; color: white;">Place</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #4CAF50; color: white;">Details</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background-color: #4CAF50; color: white;">Remarks</th>
                </tr>
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{name}</td>                    
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{booking_date}</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{place}</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">Details will be sent shortly</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">One of our representives will connect you via mail</td>
                </tr>
            </table>

            <p>We look forward to serving you!</p>
            <p>Best regards,<br>Booking Team</p>
        </body>
        </html>
        """
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



@app.route('/Profile')
def profile():  
    userDetails = db.getUserDetails(get_cookie()) 
    print(userDetails)
    return render_template('Profile.html', userDetails = userDetails)



@app.route('/signup', methods=['GET', 'POST'])
def signup():    
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        middle_name = request.form.get('middleName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User (first_name, middle_name, last_name, email, password)
        db.insertUserRecords(user)
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
           # response.set_cookie('name', db.getFullNameFromEmail(email))
            g.fullname = db.getFullNameFromEmail(email)
            return response  # Return the response object with the cookie
        else:
            error_message = "Invalid email or password."  # Error message if login fails
            return render_template('Login.html', error_message=error_message)  # Show error on the login page
    return render_template('Login.html')

def get_cookie():
   
    return request.cookies.get('email')

@app.route('/BookingDetails')
def bookingdetails():
    email = get_cookie()  
    print("Email in get_cookie:", email)
    allBookingDetails = db.getAllBookingDetailsFromEmail(email)  # Fetch booking details from the database  
    for d in allBookingDetails:
        print(f'{d.id} {d.email} {d.place} {d.bookingDate} {d.remarks}')
    return render_template('bookingDetails.html', allBookingDetails=allBookingDetails)


@app.route('/setcookie')
def set_cookie():
    # Create a response object
    response = make_response("Cookie has been set!")
    
    # Set a cookie with a name 'username' and value 'JohnDoe'
    response.set_cookie('username', 'JohnDoe')
    
    # Return the response
    return response



@app.route('/logout')
def logout():
    # Create a response object
    response = make_response(redirect(url_for('firstpage')))
    print('I am in logout')
    
    # Set a cookie with a name 'username' and value 'JohnDoe'
    response.delete_cookie('email')
    
    # Return the response
    return response



if __name__ == '__main__':
    app.run(debug=True)