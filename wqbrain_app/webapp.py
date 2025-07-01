from flask import Flask, render_template, redirect, url_for

from .database import SessionLocal, init_db
from .models import Alpha
from .fetch_alpha import fetch_alpha

app = Flask(__name__)


def get_alphas():
    session = SessionLocal()
    try:
        return session.query(Alpha).order_by(Alpha.timestamp.desc()).all()
    finally:
        session.close()


def refresh_data() -> None:
    """Fetch new alpha data and store it."""
    session = SessionLocal()
    try:
        for item in fetch_alpha():
            alpha = Alpha(name=item.get("name"), value=item.get("value"))
            session.add(alpha)
        session.commit()
    finally:
        session.close()


@app.route('/')
def index():
    alphas = get_alphas()
    return render_template('index.html', alphas=alphas)


@app.route('/refresh')
def refresh():
    refresh_data()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
