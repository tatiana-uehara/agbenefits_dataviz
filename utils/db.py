import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
import pandas as pd


def get_terradot_db_session():
    """
    Establish a SQLAlchemy session for the Terradot database.
    Assumes you have GCP running and your .env file has the correct credentials.
    """
    # Get environment variables
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")

    # Check if all required environment variables are present
    if not all([DB_HOST, DB_NAME, DB_USER]):
        print(
            "Error: Missing required environment variables (DB_HOST, DB_NAME, DB_USER)"
        )
        return None

    # Use DB_PORT if provided, otherwise default to 5432
    port = int(DB_PORT) if DB_PORT else 5432

    # Construct the database URL for SQLAlchemy
    # PostgreSQL URL format: postgresql://user:password@host:port/database_name
    DATABASE_URL = f"postgresql://{DB_USER}@{DB_HOST}:{port}/{DB_NAME}"

    try:
        # Create a SQLAlchemy engine
        engine = create_engine(DATABASE_URL)

        # Create a sessionmaker to produce new Session objects
        Session = sessionmaker(bind=engine)

        # Create and return a new session
        session = Session()
        print("Terradot database session established successfully!")
        return session
    except SQLAlchemyError as e:
        print(f"Terradot database session creation failed: {e}")
        return None


def read_pd_from_db_sql(
    query: str, session: Session, params: dict = None, **kwargs
) -> pd.DataFrame:
    """
    Read data from the database into a pandas DataFrame using a SQL query
    with a SQLAlchemy Session.

    Parameters
    ----------
    query : str
        SQL query to execute. It's highly recommended to use SQLAlchemy's
        `text()` construct for raw SQL queries to enable proper parameter binding.
    session : sqlalchemy.orm.Session
        The SQLAlchemy session object to use for the database operation.
        The session should be managed (opened and closed) by the caller.
    params : dict, optional
        Query parameters to bind. For SQLAlchemy, it's typically a dictionary
        when using `text()` constructs (e.g., {"param_name": "value"}).
        Pandas `read_sql` can also accept tuples for positional parameters with
        some DBAPIs, but `text()` with dict is more robust.
    **kwargs
        Additional arguments passed to pd.read_sql.

    Returns
    -------
    pd.DataFrame
        Query results as a DataFrame.

    Raises
    ------
    Exception
        If query execution fails.
    """
    try:
        if isinstance(query, str):
            sql_query = text(query)
        else:
            sql_query = query
        df = pd.read_sql(sql_query, session.bind, params=params, **kwargs)
        return df
    except SQLAlchemyError as e:
        if session:
            session.rollback()
        raise Exception(f"Failed to execute query: {str(e)}")
    except Exception as e:
        # Catch other potential exceptions from pandas or elsewhere
        if session:
            session.rollback()
        raise Exception(f"An unexpected error occurred: {str(e)}")


def display_results(column_names, results):
    """Display the query results."""
    if not results:
        print("No results found.")
        return

    # Print column names
    print(" | ".join(column_names))
    print("-" * (sum(len(name) for name in column_names) + 3 * (len(column_names) - 1)))

    # Print rows
    for row in results:
        print(" | ".join(str(value) for value in row))
