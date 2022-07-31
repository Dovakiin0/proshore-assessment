from dotenv import load_dotenv, find_dotenv
from Assessment import createApp
import os

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    app = createApp(db_uri=os.getenv("SQLALCHEMY_DATABASE_URI"))
    if(os.getenv("MODE") == "PRODUCTION"):
        from waitress import serve
        serve(app, host="0.0.0.0", port=5050)
    else:
        app.run(debug=True, port=5050)