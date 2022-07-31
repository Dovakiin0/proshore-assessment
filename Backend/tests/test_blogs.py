
def test_getBlogs(app_with_data):
    '''
        Test to get all blogs
    '''
    response = app_with_data.get(
        "/api/v1/blogs/",
    )
    data = response.json
    assert "data" in response.json 
    assert response.status_code == 200

def test_getSingleBlog(app_with_data):
    '''
        Test to get a single blog
    '''
    response = app_with_data.get("/api/v1/blogs/1")
    assert "data" in response.json 
    assert response.status_code == 200

def test_addBlogs(app_with_db):
    '''
        Test to add a new blog
    '''
    response = app_with_db.post("/api/v1/blogs/", json={
        "title": "Test Blog",
        "description": "Test Blog Description",
        "image_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
        "author_name": "Test Author",
        "author_description": "Test Author Description",
        "reading_time": "Test Reading Time",
        "blog_image_url": "HELLO"
    })

    assert "data" in response.json 
    assert response.status_code == 201

def test_updateBlogs(app_with_data):
    '''
        Test to update an existing blog
    '''
    response = app_with_data.put("/api/v1/blogs/1", json={
        "title": "Test Blog Updated",
        "description": "Test Blog Description Updated",
        "image_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png Updated",
        "author_name": "Test Author Updated",
        "author_description": "Test Author Description Updated",
        "reading_time": "Test Reading Time Updated",
        "blog_image_url": "HELLO Updated"
    })
    assert "data" in response.json 
    assert response.status_code == 200

def test_deleteBlogs(app_with_data):
    '''
        Test to delete an existing blog
    '''
    response = app_with_data.delete("/api/v1/blogs/1")
    assert response.status_code == 200

def test_deleteAllBlogs(app_with_data):
    '''
        Test to delete all blogs
    '''
    response = app_with_data.delete("/api/v1/blogs/")
    assert response.status_code == 200

def test_bulkAddBlogs(app_with_db):
    '''
        Test to bulk add new blogs
    '''
    data = [
            {
                "title": "Test Blog",
                "description": "Test Blog Description",
                "image_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                "author_name": "Test Author",
                "author_description": "Test Author Description",
                "reading_time": "Test Reading Time",
                "blog_image_url": "HELLO"
            },
            {
                "title": "Test Blog",
                "description": "Test Blog Description",
                "image_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                "author_name": "Test Author",
                "author_description": "Test Author Description",
                "reading_time": "Test Reading Time",
                "blog_image_url": "HELLO"
            }
        ]
    response = app_with_db.post("/api/v1/blogs/bulk", json=data)
    assert "data" in response.json
    assert response.status_code == 201