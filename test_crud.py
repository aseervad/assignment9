import os
import sys
from flask import Flask
from models import db, User, SpeakingTest, ListeningTest
from config import Config

def create_app():
    # Create test Flask application
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    return app

def test_user_crud():
    """Test CRUD operations on User model"""
    print("===== Testing User CRUD Operations =====")
    
    # Create a new user
    print("\nCreating new user...")
    user = User.add_user("Test User", "test@example.com", "password123")
    print(f"Created user: {user.name} with ID: {user.id}")
    
    # Get user by ID
    print("\nGetting user by ID...")
    retrieved_user = User.get_user_by_id(user.id)
    print(f"Retrieved user: {retrieved_user.name}")
    
    # Update user
    print("\nUpdating user...")
    updated_user = User.update_user(user.id, name="Updated Test User")
    print(f"Updated user name: {updated_user.name}")
    
    # Get all users
    print("\nGetting all users...")
    all_users = User.get_all_users()
    print(f"Total users: {len(all_users)}")
    
    # Delete user
    print("\nDeleting user...")
    result = User.delete_user(user.id)
    print(f"User deleted: {result}")
    
    # Verify deletion
    print("\nVerifying deletion...")
    deleted_user = User.get_user_by_id(user.id)
    print(f"User should be None: {deleted_user is None}")

def test_speaking_test_crud():
    """Test CRUD operations on SpeakingTest model"""
    print("\n===== Testing SpeakingTest CRUD Operations =====")
    
    # Create a test user first
    user = User.add_user("Speaking Test User", "speaking@example.com", "password123")
    
    # Create a new test
    print("\nCreating new speaking test...")
    test = SpeakingTest.add_test(
        user_id=user.id,
        question="Describe your hometown.",
        response="My hometown is a beautiful city...",
        score=7.5
    )
    print(f"Created test with ID: {test.id}")
    
    # Get test by ID
    print("\nGetting test by ID...")
    retrieved_test = SpeakingTest.get_test_by_id(test.id)
    print(f"Retrieved test score: {retrieved_test.score}")
    
    # Update test
    print("\nUpdating test...")
    updated_test = SpeakingTest.update_test(test.id, score=8.0)
    print(f"Updated test score: {updated_test.score}")
    
    # Get tests by user
    print("\nGetting tests by user...")
    user_tests = SpeakingTest.get_tests_by_user(user.id)
    print(f"User tests count: {len(user_tests)}")
    
    # Delete test
    print("\nDeleting test...")
    result = SpeakingTest.delete_test(test.id)
    print(f"Test deleted: {result}")
    
    # Clean up the test user
    User.delete_user(user.id)

def test_listening_test_crud():
    """Test CRUD operations on ListeningTest model"""
    print("\n===== Testing ListeningTest CRUD Operations =====")
    
    # Create a test user first
    user = User.add_user("Listening Test User", "listening@example.com", "password123")
    
    # Create a new test
    print("\nCreating new listening test...")
    test = ListeningTest.add_test(
        user_id=user.id,
        question="Listen to the conversation and answer the questions.",
        response="The conversation was about...",
        score=6.5
    )
    print(f"Created test with ID: {test.id}")
    
    # Get test by ID
    print("\nGetting test by ID...")
    retrieved_test = ListeningTest.get_test_by_id(test.id)
    print(f"Retrieved test score: {retrieved_test.score}")
    
    # Update test
    print("\nUpdating test...")
    updated_test = ListeningTest.update_test(test.id, score=7.0)
    print(f"Updated test score: {updated_test.score}")
    
    # Get tests by user
    print("\nGetting tests by user...")
    user_tests = ListeningTest.get_tests_by_user(user.id)
    print(f"User tests count: {len(user_tests)}")
    
    # Delete test
    print("\nDeleting test...")
    result = ListeningTest.delete_test(test.id)
    print(f"Test deleted: {result}")
    
    # Clean up the test user
    User.delete_user(user.id)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Run tests
        test_user_crud()
        test_speaking_test_crud()
        test_listening_test_crud()
        
        print("\nAll CRUD tests completed successfully!")