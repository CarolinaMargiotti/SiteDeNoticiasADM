from flask import Flask, render_template
from controllers import news_bp,subjects_bp
from waitress import serve

app = Flask(__name__)
app.register_blueprint(news_bp)
app.register_blueprint(subjects_bp)

if __name__ == '__main__':
    # app.run()
    serve(app, host='0.0.0.0', port=5000)

