import unittest
from BaseCase import BaseCase
class TestAddmember(BaseCase):
    """
    Unit test for adding or reducing members
    """
    def test_add_member(self):
        """
        Adding a custom member, reflects the new member in the list
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

    def test_delete_member(self):
        """
        deleting undesired members
        """
        custom_member = "bbb"
        custom_id="0001"
        self.user.delete_member(custom_member,custom_id)
        raw_content = self.user.members.keys()
        userlists=[]
        
        for mem in raw_content:
            userlists.append(mem)
        assert custom_member not in userlists
        
if __name__ == '__main__':
    unittest.main()
