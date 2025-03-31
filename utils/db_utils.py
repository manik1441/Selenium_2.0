import psycopg2
from psycopg2.extras import RealDictCursor


class DatabaseUtil:
    def __init__(self, host, port, database, user, password):
        """Initialize the database connection."""
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
                cursor_factory=RealDictCursor
            )
            return self.connection
        except Exception as e:
            raise Exception(f"Error connecting to the database: {e}")

    def execute_query(self, query):
        """Execute a query and return the results."""
        if not self.connection:
            raise Exception("Connection is not established. Call the 'connect' method first.")
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Error executing query: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()