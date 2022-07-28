from flask import Blueprint
from ..controller.BlogsController import get_all_blogs, add_blogs, delete_blogs, update_blogs, get_single_blog, bulk_add

blogs = Blueprint('blogs', __name__)

blogs.route("/", methods=['GET'])(get_all_blogs)
blogs.route("/<int:id>", methods=['GET'])(get_single_blog)
blogs.route("/", methods=['POST'])(add_blogs)
blogs.route("/bulk", methods=['POST'])(bulk_add)
blogs.route("/<int:id>", methods=['PUT'])(update_blogs)
blogs.route("/<int:id>", methods=['DELETE'])(delete_blogs)
