from app import create_app

app, PORT = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, use_reloader=True, debug=True)

