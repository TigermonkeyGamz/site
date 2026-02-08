# server.py
from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Replace with your SMTP settings
SMTP_SERVER = 'smtp.gmail.com'       # or your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'calebn.ramey@gmail.com'
EMAIL_PASSWORD = "Sh0shi'sBro"

@app.route('/submit-email', methods=['POST'])
def submit_email():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'No email provided'}), 400

    # Send email to you
    msg = EmailMessage()
    msg['Subject'] = f'Canva Whiteboard Access Request from {email}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f'{email} requested access to your Canva Whiteboard.')

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({'status': 'success'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
