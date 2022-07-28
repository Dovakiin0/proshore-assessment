from typing import final
from flask import jsonify, request
from ..models.blogs import Blogs, blog_schema, blogs_schema
from ..models import db

def add_blogs():
    '''
        adds a blog
    '''
    if request.method == "POST":
        data = request.json
        blogs = Blogs(
            title=data['title'],
            description=data['description'],
            image_url=data['image_url'],
            author_name=data['author_name'],
            author_description=data['author_description'],
            reading_time=data['reading_time']
        )
        try:
            db.session.add(blogs)
            db.session.commit()
            return jsonify({"message": "Blog added successfully", "data": data}), 201
        except:
            return jsonify({"message": "Error adding blog"}), 500

def get_all_blogs():
    '''
        returns all blogs with pagination
        takes pages and limit as query
    '''
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    blogs = Blogs.query.paginate(page, limit, error_out=False)
    if not blogs.items:
        return jsonify({"message": "No blogs found"}), 404
    
    result = blogs_schema.dump(blogs.items)
    return jsonify({"data": result, "next": blogs.next_num, "prev": blogs.prev_num}), 200

def get_single_blog(id):
    '''
        returns a single blog
    '''
    blogs = Blogs.query.get_or_404(id)
    if not blogs:
        return jsonify({"message": "Blog not found"}), 404
    result = blog_schema.dump(blogs)
    return jsonify({"data": result}), 200

def update_blogs(id):
    '''
        updates a blog
    '''
    blogs = Blogs.query.get_or_404(id)
    if not blogs:
        return jsonify({"message": "Blog not found"}), 404
    data = request.json
    blogs.title = data['title']
    blogs.description = data['description']
    blogs.image_url = data['image_url']
    blogs.author_name = data['author_name']
    blogs.author_description = data['author_description']
    blogs.reading_time = data['reading_time']
    db.session.commit()
    return jsonify({"message": "Blog updated successfully", "data": data}), 200

def delete_blogs(id):
    '''
        deletes a blog
    '''
    blogs = Blogs.query.get_or_404(id)
    if not blogs:
        return jsonify({"message": "Blog not found"}), 404
    db.session.delete(blogs)
    db.session.commit()
    return jsonify({"message": "Blog deleted successfully"}), 200