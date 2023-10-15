import os.path
import pathlib
import unittest

from src.code.user import User


class BaseCase(unittest.TestCase):
    """
    BaseCase serves as a foundational class for all other unit tests.
    It sets up common procedures for preparing and cleaning the test environment.
    """
    def setUp(self) -> None:
        """
        Creates a new user
        """
        # os.chdir("test")
        # Get the absolute path for the 'data' directory
        abspath = pathlib.Path("data").absolute()
        
         # If the 'data' directory doesn't exist, create it
        if not os.path.exists(abspath):
            os.mkdir(abspath)
        # Print the current working directory (useful for debugging)
        print(os.getcwd())

        # Create a new User instance for testing
        self.user = User("1")

        # Initialize the expected transactions list
        self.expected_list = self.create_transaction()

    def tearDown(self) -> None:
        """
        Removes the user pickle
        """
        abspath = pathlib.Path("data").absolute()
        
        # If the 'data' directory doesn't exist, create it
        if not os.path.exists(abspath):
            os.mkdir(abspath)

    def create_transaction(self):
        """
        Creates the dictionary of transactions
        """
        transaction = {}
        for category in self.user.spend_categories:
            transaction[category] = []
        return transaction

    def add_record(self, category, record):
        """
        Adds a record to the internal expected transactions
        """
        self.expected_list[category].append(record)


if __name__ == '__main__':
    # Execute the unit tests
    unittest.main()
