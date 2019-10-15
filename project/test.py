from flask import Flask

app = Flask(__name__)
# app.config["DEBUG"] = True
app.config.from_envvar("FLASK",silent=True)   ## True
if __name__ == '__main__':
    app.run()


