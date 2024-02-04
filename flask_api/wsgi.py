from server import app
import os


if __name__ == "__main__":
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    print(f'FLASK_RUN_PORT= {FLASK_RUN_PORT}')
    app.run(port=FLASK_RUN_PORT)
