from flask import Flask, render_template
from .database import SessionLocal, init_db
from .models import Alpha

app = Flask(__name__)


def get_alphas():
    session = SessionLocal()
    try:
        return session.query(Alpha).order_by(Alpha.timestamp.desc()).all()
    finally:
        session.close()


@app.route('/')
def index():
    alphas = get_alphas()
    return render_template('index.html', alphas=alphas)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
