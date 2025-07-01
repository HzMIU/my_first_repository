# my_first_repository

This repository contains an example project for fetching alpha data from the
WQBrain platform, storing it in a MySQL database, and visualizing it on a web
page.

## Setup

1. Install dependencies (preferably in a virtual environment):

```bash
pip install -r wqbrain_app/requirements.txt
```

2. Set the `MYSQL_URI` environment variable to point to your MySQL database.
   Example:

```bash
export MYSQL_URI="mysql+pymysql://user:password@localhost/wqbrain"
```

3. Initialize the database and load alpha data:

```bash
python -m wqbrain_app.load_alpha
```

4. Run the web application:

```bash
python -m wqbrain_app.webapp
```

Then open `http://localhost:5000` to view the alpha data.

## Notes

- `fetch_alpha.py` contains a placeholder for the real API call to the
  WQBrain platform. Update it with your API logic to retrieve alpha data.
- The example uses Flask and SQLAlchemy.
