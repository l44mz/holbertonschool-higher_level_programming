#!/usr/bin/python3
"""Simple Flask API secured with Basic Auth and JWT authentication."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me-in-production"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user store: username -> {username, password (hashed), role}
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# --- Basic Auth setup -------------------------------------------------

@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials against the users store."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Ensure Basic Auth failures always return 401."""
    return jsonify({"error": "Unauthorized"}), 401


# --- JWT error handlers (always 401) -----------------------------------

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle a missing Authorization header/token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle a malformed/invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle an expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle a revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle a request that requires a fresh token."""
    return jsonify({"error": "Fresh token required"}), 401


# --- Routes -------------------------------------------------------------

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected with HTTP Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user with username/password and issue a JWT."""
    credentials = request.get_json(silent=True)
    if not credentials:
        return jsonify({"error": "Invalid JSON"}), 400

    username = credentials.get("username")
    password = credentials.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password or ""):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
    )
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected with a valid JWT token."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route only accessible to users with the 'admin' role."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
