from operator import contains, or_
from flask import jsonify, request
from sqlalchemy import asc, desc, func
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
            blog_image_url=data['blog_image_url'],
            author_description=data['author_description'],
            reading_time=data['reading_time']
        )
        try:
            db.session.add(blogs)
            db.session.commit()
            return jsonify({"message": "Blog added successfully", "data": data}), 201
        except:
            return jsonify({"message": "Error adding blog"}), 500

def bulk_add():
    '''
        bulk adds blogs
    '''
    data = request.json
    db.session.expunge_all()
    for blog in data:
        blogs = Blogs(
            title=blog['title'],
            description=blog['description'],
            image_url=blog['image_url'],
            blog_image_url=blog['blog_image_url'],
            author_name=blog['author_name'],
            author_description=blog['author_description'],
            reading_time=blog['reading_time']
        )
        db.session.add(blogs)
    db.session.commit()
    return jsonify({"message": "Blogs added successfully"}), 201

def get_all_blogs():
    '''
        returns all blogs with filters and pagination
    '''
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    search_str = request.args.get('keyword', "", type=str)
    sort_str = request.args.get('sort', "id", type=str)
    order_str = request.args.get('order', "asc", type=str)

    sorts = {
        "id": Blogs.id,
        "title": Blogs.title,
        "description": Blogs.description,
        "author_name": Blogs.author_name,
        "author_description": Blogs.author_description,
        "reading_time": Blogs.reading_time
    }

    # function to decide whether to return asc or desc order
    def get_asc_or_desc(str, sort_str):
        if str == "asc":
            return asc(sorts[sort_str])
        else:
            return desc(sorts[sort_str])
    search_str = func.lower(search_str)
    blogs = Blogs.query.order_by(get_asc_or_desc(order_str, sort_str)).filter(
        func.lower(Blogs.title).contains(search_str) | func.lower(Blogs.description).contains(search_str) | func.lower(Blogs.author_description).contains(search_str) | func.lower(Blogs.author_name).contains(search_str) | func.lower(Blogs.reading_time).contains(search_str)
        ).paginate(page, limit, error_out=False)
    if not blogs.items:
        return jsonify({"message": "No blogs found"}), 404
    
    result = blogs_schema.dump(blogs.items)
    return jsonify({"data": result,"page":blogs.page, "next": blogs.next_num, "prev": blogs.prev_num, "total": blogs.total}), 200

def get_single_blog(id):
    '''
        returns a single blog
    '''
    blogs = Blogs.query.get(id)
    if not blogs:
        return jsonify({"message": "Blog not found"}), 404
    result = blog_schema.dump(blogs)
    return jsonify({"data": result}), 200

def update_blogs(id):
    '''
        updates a blog
    '''
    blogs = Blogs.query.get(id)
    if not blogs:
        return jsonify({"message": "Blog not found"}), 404
    data = request.json
    blogs.title = data['title']
    blogs.description = data['description']
    blogs.image_url = data['image_url']
    blogs.blog_image_url = data['blog_image_url']
    blogs.author_name = data['author_name']
    blogs.author_description = data['author_description']
    blogs.reading_time = data['reading_time']
    db.session.commit()
    return jsonify({"message": "Blog updated successfully", "data": data}), 200

def delete_blogs(id):
    '''
        deletes a blog
    '''
    blogs = Blogs.query.get(id)
    if not blogs:
        return jsonify({"message": "Blog not found"}), 404
    db.session.delete(blogs)
    db.session.commit()
    return jsonify({"message": "Blog deleted successfully"}), 200

def delete_all_blogs():
    '''
        deletes all blogs
    '''
    db.session.query(Blogs).delete()
    db.session.commit()
    return jsonify({"message": "All blogs deleted successfully"}), 200