from flask import Blueprint, jsonify, request
from models import db, User, SpeakingTest, ListeningTest

bp = Blueprint('test_routes', __name__)

@bp.route('/test', methods=['GET'])
def test_route():
    """Simple test route to verify API is working"""
    return jsonify({"message": "API is working correctly!"})

# User routes
@bp.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = User.get_all_users()
    result = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify({"status": "success", "data": result})

@bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['name', 'email', 'password']):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    # Check if user already exists
    existing_user = User.get_user_by_email(data['email'])
    if existing_user:
        return jsonify({"status": "error", "message": "Email already registered"}), 409
    
    # Create new user
    user = User.add_user(data['name'], data['email'], data['password'])
    
    return jsonify({
        "status": "success", 
        "message": "User created successfully",
        "data": {"id": user.id, "name": user.name, "email": user.email}
    }), 201

# Speaking test routes
@bp.route('/speaking-tests', methods=['GET'])
def get_speaking_tests():
    """Get all speaking tests"""
    tests = SpeakingTest.get_all_tests()
    result = [{
        "id": test.id,
        "user_id": test.user_id,
        "question": test.question,
        "response": test.response,
        "score": test.score,
        "created_at": test.created_at
    } for test in tests]
    return jsonify({"status": "success", "data": result})

@bp.route('/speaking-tests', methods=['POST'])
def create_speaking_test():
    """Create a new speaking test"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['user_id', 'question']):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    # Create new test
    test = SpeakingTest.add_test(
        user_id=data['user_id'],
        question=data['question'],
        response=data.get('response'),
        score=data.get('score')
    )
    
    return jsonify({
        "status": "success", 
        "message": "Speaking test created successfully",
        "data": {
            "id": test.id,
            "user_id": test.user_id,
            "question": test.question
        }
    }), 201

# Listening test routes
@bp.route('/listening-tests', methods=['GET'])
def get_listening_tests():
    """Get all listening tests"""
    tests = ListeningTest.get_all_tests()
    result = [{
        "id": test.id,
        "user_id": test.user_id,
        "question": test.question,
        "response": test.response,
        "score": test.score,
        "created_at": test.created_at
    } for test in tests]
    return jsonify({"status": "success", "data": result})

@bp.route('/listening-tests', methods=['POST'])
def create_listening_test():
    """Create a new listening test"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['user_id', 'question']):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    # Create new test
    test = ListeningTest.add_test(
        user_id=data['user_id'],
        question=data['question'],
        response=data.get('response'),
        score=data.get('score')
    )
    
    return jsonify({
        "status": "success", 
        "message": "Listening test created successfully",
        "data": {
            "id": test.id,
            "user_id": test.user_id,
            "question": test.question
        }
    }), 201