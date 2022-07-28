from flask import Blueprint, jsonify, request
from ..controller.BlogsController import get_all_blogs

blogs = Blueprint('blogs', __name__)

blogs.route("/", methods=['GET'])(get_all_blogs)
