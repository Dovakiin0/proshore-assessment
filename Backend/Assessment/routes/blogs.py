from flask import Blueprint
from ..controller.BlogsController import delete_all_blogs, get_all_blogs, add_blogs, delete_blogs, update_blogs, get_single_blog, bulk_add, delete_all_blogs

blogs = Blueprint('blogs', __name__)

blogs.route("/", methods=['GET'])(get_all_blogs)
blogs.route("/<int:id>", methods=['GET'])(get_single_blog)
blogs.route("/", methods=['POST'])(add_blogs)
blogs.route("/bulk", methods=['POST'])(bulk_add)
blogs.route("/<int:id>", methods=['PUT'])(update_blogs)
blogs.route("/<int:id>", methods=['DELETE'])(delete_blogs)
blogs.route("/", methods=['DELETE'])(delete_all_blogs)
