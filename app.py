from flask import Flask
from dynaconf import FlaskDynaconf


class App:
    def __init__(self) -> None:
        self.app = Flask(__name__)

    def create_app(self) -> Flask:
        FlaskDynaconf(app=self.app, extensions_list=True)
        return self.app


app = App().create_app()

if __name__ == "__main__":
    app.run(debug=True)
