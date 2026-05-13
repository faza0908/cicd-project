"""
Counter Service - A simple Flask application
"""
from flask import Flask, jsonify, request, abort
import logging

# Create the Flask application
app = Flask(__name__)
app.config["TESTING"] = False

# In-memory counter storage
COUNTERS = {}

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(levelname)s [%(name)s] %(message)s",
    level=logging.INFO
)


############################################################
# Health endpoint
############################################################
@app.route("/health")
def health():
    """Returns a health check response."""
    return jsonify({"status": "OK"})


############################################################
# Index endpoint
############################################################
@app.route("/")
def index():
    """Root endpoint"""
    return jsonify({"status": "SERVICE RUNNING", "port": 8000})


############################################################
# Counter endpoints
############################################################
@app.route("/counters", methods=["GET"])
def list_counters():
    """Returns all counters."""
    logger.info("Request to list all counters")
    return jsonify(COUNTERS)


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a counter with the given name."""
    logger.info("Request to create counter: %s", name)
    if name in COUNTERS:
        return jsonify(
            {"error": f"Counter '{name}' already exists."}
        ), 409
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), 201


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read the counter with the given name."""
    logger.info("Request to read counter: %s", name)
    if name not in COUNTERS:
        return jsonify(
            {"error": f"Counter '{name}' does not exist."}
        ), 404
    return jsonify({name: COUNTERS[name]})


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Increment the counter with the given name."""
    logger.info("Request to update counter: %s", name)
    if name not in COUNTERS:
        return jsonify(
            {"error": f"Counter '{name}' does not exist."}
        ), 404
    COUNTERS[name] += 1
    return jsonify({name: COUNTERS[name]})


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete the counter with the given name."""
    logger.info("Request to delete counter: %s", name)
    if name not in COUNTERS:
        return jsonify(
            {"error": f"Counter '{name}' does not exist."}
        ), 404
    del COUNTERS[name]
    return "", 204


############################################################
# Main entry point
############################################################
if __name__ == "__main__":
    logger.info("**** SERVICE RUNNING on port 8000 ****")
    app.run(host="0.0.0.0", port=8000, debug=True)
