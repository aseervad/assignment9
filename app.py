from flask import Flask
from flask_cors import CORS
from models import db
from config import Config
from flask_migrate import Migrate

# Create Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Import routes
from routes.test_routes import bp
app.register_blueprint(bp, url_prefix='/api')

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return {"message": "Welcome to the IELTS Speaking Test API"}

if __name__ == '__main__':
    app.run(debug=True)