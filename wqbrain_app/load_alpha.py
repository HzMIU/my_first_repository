"""Utility script to store alpha data from WQBrain into the database."""

import logging

from .database import SessionLocal, init_db
from .models import Alpha
from .fetch_alpha import fetch_alpha


def main() -> None:
    """Fetch alpha records and persist them."""

    init_db()
    session = SessionLocal()
    try:
        alphas = fetch_alpha()
        for item in alphas:
            alpha = Alpha(name=item.get("name"), value=item.get("value"))
            session.add(alpha)
        session.commit()
        logging.info("Loaded %d alphas", len(alphas))
    finally:
        session.close()


if __name__ == "__main__":
    main()
