from Assessment import createApp

if __name__ == "__main__":
    app = createApp()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5050)