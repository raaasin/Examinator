from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Firebase initialization
cred = credentials.Certificate('firebase_config.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'YOUR_FIREBASE_DATABASE_URL'})

# Routes
@app.route('/')
def login():
    # Render the login page
    return render_template('login.html')

# Add more routes for admin and student pages

if __name__ == '__main__':
    app.run(debug=True)
