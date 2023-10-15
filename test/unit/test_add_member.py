import unittest
from BaseCase import BaseCase
class TestAddmember(BaseCase):
    """
    Unit test for adding custom category
    """
    def test_add_member(self):
        """
        Adding a custom category, reflects the new category in the list
        """
        custom_member = "bbb"
        custom_id="0001"
        custom_email="12333333@qq.com"
        self.user.add_member(custom_member,custom_email,custom_id)
        raw_content = self.user.members.keys()

        userlists=[]
        for mem in raw_content:
            userlists.append(mem)
        assert custom_member in userlists
if __name__ == '__main__':
    unittest.main()
