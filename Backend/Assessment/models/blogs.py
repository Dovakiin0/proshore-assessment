from . import db, ma
from marshmallow import fields

class Blogs(db.Model):
    __tablename__ = "blogs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
    author_name = db.Column(db.String(1000), nullable=False)
    author_description = db.Column(db.String(1000), nullable=False)
    reading_time = db.Column(db.String(1000), nullable=False)
    blog_image_url = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"<Blog {self.id}>"

class BlogsSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    image_url = fields.Str(required=True)
    author_name = fields.Str(required=True)
    author_description = fields.Str(required=True)
    reading_time = fields.Str(required=True)
    blog_image_url = fields.Str(required=True)

    class Meta:
        fields = ("id", "title", "description", "image_url", "author_name", "author_description", "reading_time", "blog_image_url")

blogs_schema = BlogsSchema(many=True)
blog_schema = BlogsSchema()