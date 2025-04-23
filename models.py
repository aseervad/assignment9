from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    """User model representing test takers"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Should be hashed in production
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    speaking_tests = db.relationship('SpeakingTest', backref='user', lazy=True)
    listening_tests = db.relationship('ListeningTest', backref='user', lazy=True)
    
    def __repr__(self):
        return f"<User {self.name}>"

    # CRUD Operations
    @staticmethod
    def add_user(name, email, password):
        """Add a new user"""
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID"""
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_email(email):
        """Get user by email"""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_all_users():
        """Get all users"""
        return User.query.all()
    
    @staticmethod
    def update_user(user_id, **kwargs):
        """Update user details"""
        user = User.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
            return user
        return None
    
    @staticmethod
    def delete_user(user_id):
        """Delete a user"""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False


class SpeakingTest(db.Model):
    """SpeakingTest model for speaking test records"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    response = db.Column(db.Text, nullable=True)  # Audio response transcript or details
    score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<SpeakingTest {self.id} by User {self.user_id}>"
    
    # CRUD Operations
    @staticmethod
    def add_test(user_id, question, response=None, score=None):
        """Add a new speaking test"""
        test = SpeakingTest(user_id=user_id, question=question, response=response, score=score)
        db.session.add(test)
        db.session.commit()
        return test
    
    @staticmethod
    def get_test_by_id(test_id):
        """Get test by ID"""
        return SpeakingTest.query.get(test_id)
    
    @staticmethod
    def get_tests_by_user(user_id):
        """Get all tests for a specific user"""
        return SpeakingTest.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_all_tests():
        """Get all tests"""
        return SpeakingTest.query.all()
    
    @staticmethod
    def update_test(test_id, **kwargs):
        """Update test details"""
        test = SpeakingTest.query.get(test_id)
        if test:
            for key, value in kwargs.items():
                if hasattr(test, key):
                    setattr(test, key, value)
            db.session.commit()
            return test
        return None
    
    @staticmethod
    def delete_test(test_id):
        """Delete a test"""
        test = SpeakingTest.query.get(test_id)
        if test:
            db.session.delete(test)
            db.session.commit()
            return True
        return False


class ListeningTest(db.Model):
    """ListeningTest model for listening test records"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    response = db.Column(db.Text, nullable=True)
    score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ListeningTest {self.id} by User {self.user_id}>"
    
    # CRUD Operations
    @staticmethod
    def add_test(user_id, question, response=None, score=None):
        """Add a new listening test"""
        test = ListeningTest(user_id=user_id, question=question, response=response, score=score)
        db.session.add(test)
        db.session.commit()
        return test
    
    @staticmethod
    def get_test_by_id(test_id):
        """Get test by ID"""
        return ListeningTest.query.get(test_id)
    
    @staticmethod
    def get_tests_by_user(user_id):
        """Get all tests for a specific user"""
        return ListeningTest.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_all_tests():
        """Get all tests"""
        return ListeningTest.query.all()
    
    @staticmethod
    def update_test(test_id, **kwargs):
        """Update test details"""
        test = ListeningTest.query.get(test_id)
        if test:
            for key, value in kwargs.items():
                if hasattr(test, key):
                    setattr(test, key, value)
            db.session.commit()
            return test
        return None
    
    @staticmethod
    def delete_test(test_id):
        """Delete a test"""
        test = ListeningTest.query.get(test_id)
        if test:
            db.session.delete(test)
            db.session.commit()
            return True
        return False