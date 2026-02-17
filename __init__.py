from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create database instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'mysecret12345'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db.init_app(app)

    # Import and register blueprints
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.tasks import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    # Redirect root URL to tasks page or login page
    @app.route('/')
    def home():
        return redirect(url_for('tasks.view_tasks'))  # or 'auth.login' if you prefer

    return app

