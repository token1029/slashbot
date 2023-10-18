import unittest
from BaseCase import BaseCase
from src.code.user import User
class Testsplitbill(BaseCase):
    """
       Unit test for splitbill
       """
    def test_split_bill(self):
        """
        Adding a custom user id, reflects the new user in the list
        Adding a custom bill, reflects the total bill in an event
        """
        custom_id=["001"]
        custom_bill=55
        debit=custom_bill/len(custom_id)
        self.user.split_bill(custom_bill, custom_id)
        assert debit == custom_bill

if __name__ == '__main__':
    unittest.main()