# Backend Service

This service provides the API services. It includes all the CRUD operations for the blogs. The technology used for this service are as follows:

- Python with Flask
- Flask-SQLAlchemy for ORM
- Postgres for Database
- pytest for testing

Features such as pagination, sorting, and searching are implemented here to reduce the load and optimize the speed on the client side.
For the architectural pattern, Model-View-Controller (MVC) pattern is used. The app contains separate controller, routes, and models. This pattern makes it easier for the developer to understand the code and makes it easier to maintain the code.

By default, the app is running on port `5050`.
The entrypoint is `app.py`

### Endpoints

| endpoint             | method | description         |
| -------------------- | ------ | ------------------- |
| /api/v1/blogs        | GET    | Get all the blogs   |
| /api/v1/blogs        | POST   | Create a new blog   |
| /api/v1/blogs/bulk   | POST   | Bulk adds new blogs |
| /api/v1/blogs/int:id | GET    | Get a blog by id    |
| /api/v1/blogs/int:id | PUT    | Update a blog by id |
| /api/v1/blogs/int:id | DELETE | Delete a blog by id |
| /api/v1/blogs        | DELETE | Delete all blogs    |
