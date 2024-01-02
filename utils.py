# Helper functions here
import os
from dotenv import load_dotenv

# Utility functions as Class methods: env_setup
class Utils:
    # Initialize Utils class
    def __init__(self):
        print("Initializing Utils class...")

    # Print all environment variables
    @classmethod
    def print_env(cls):
        # Print all environment variables
        print("Printing all environment variables...")
        print("OPENAI_API_BASE:", os.getenv("OPENAI_API_BASE"))
        print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

    # Set up environment variables
    @classmethod
    def env_setup(cls):
        # Set up environment
        print("Setting up environment variables...")
        # try to check local.env exists and load env from .env file, else print error
        try:

            # load env from custom .env file: local.env
            if os.path.exists("local.env"):
                print("Loading environment variables from local.env...")
                load_dotenv(dotenv_path="local.env")

                # print error if above env is empty
                if os.getenv("OPENAI_API_BASE", "") == "" or os.getenv("OPENAI_API_KEY", "") == "":
                    error_msg = "Please set OPENAI_API_KEY and OPENAI_API_BASE in local.env"
                    raise ValueError(error_msg)
                
            else:
                error_msg = "Please create a local.env file, please refer to sample.env for more details"
                raise FileNotFoundError(error_msg)
        finally:
            pass



# main function for local testing
def main():
    # Set up environment variables
    Utils.env_setup()

if __name__ == '__main__':
    main()
