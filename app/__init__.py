from flask import Flask
from flask_mail import Mail
from .config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Initialize Flask-Mail
mail = Mail(app)

# Import views to avoid circular imports
from app import views
