from flask import jsonify

def get_all_blogs():
    return jsonify({"message": "All blogs"})