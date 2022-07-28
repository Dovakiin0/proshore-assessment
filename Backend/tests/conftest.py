import pytest
from Assessment import createApp
from Assessment.models import db
from Assessment.models.blogs import Blogs

@pytest.fixture(scope="session")
def flask_app():
    app = createApp()

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client
    ctx.pop()

@pytest.fixture(scope="session")
def app_with_db():
    db.create_all()

    yield flask_app
    
    db.session.commit()
    db.drop_all()


@pytest.fixture(scope="session")
def app_with_data(app_with_db):
    blogs = Blogs()
    blogs.title = "Test Blog"
    blogs.description = "Test Blog Description"
    blogs.image_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
    blogs.author_name = "Test Author"
    blogs.author_description = "Test Author Description"
    blogs.reading_time = "Test Reading Time"

    db.session.add(blogs)
    db.session.commit()

    yield app_with_db

    db.session.delete(blogs)
    db.session.commit()