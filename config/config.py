class EnvironmentProcessor:
    """Singleton-based class to store and access environment settings."""
    _instance = None
    env_details = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EnvironmentProcessor, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def setup_environment(self, env):
        """
        Process environment settings based on the environment.
        """
        if not self.env_details:  # Load environment configuration once
            if env == "demo":
                self.env_details = {
                    "env": "si",
                    "url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
                    "username": "si_user",
                    "password": "si_password",
                    "db": "si_db",
                    "host": "si-db.example.com",
                    "port": 5432,
                    "base_url":"https://reqres.in"
                }
            elif env == "qa":
                self.env_details = {
                    "env": "qa",
                    "url": "https://qa.example.com/api/",
                    "username": "qa_user",
                    "password": "qa_password",
                    "db": "qa_db",
                    "host": "qa-db.example.com",
                    "port": 5432,
                    "base_url": "https://reqres.in"
                }
            elif env == "uat":
                self.env_details = {
                    "env": "uat",
                    "url": "https://uat.example.com/api/",
                    "username": "uat_user",
                    "password": "uat_password",
                    "db": "uat_db",
                    "host": "uat-db.example.com",
                    "port": 5432,
                    "base_url": "https://reqres.in"
                }
            else:
                raise ValueError(f"Unsupported environment: {env}")

        return self.env_details

def env_setups(request):
    """Set up the environment and its values"""
    try:
        env = request.config.getoption("env")
        print("Env Setup --------------------------", env)
        return EnvironmentProcessor().setup_environment(env)
    except Exception as e:
        print("Env Setup Failure --------------------------", e)

ENVIRONMENT = {}

DEBUG_LOG = False
TIMEOUT = 20