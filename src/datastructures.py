"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{'id':1, 'first_name': 'John', 'last_name':self.last_name, 'age':33, 'lucky_numbers':[7, 13, 22]}, 
                         {'id': self._generate_id(), 'first_name': 'Jane', 'last_name':self.last_name, 'age':35, 'lucky_numbers':[10, 14, 32]},
                         {'id': self._generate_id(), 'first_name': 'Jimy', 'last_name':self.last_name, 'age':5, 'lucky_numbers':[1]}]  

    # Read-only: Use this method to generate random members ID's when adding members into the list
    
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['last_name'] = self.get_last_name()
        self._members.append(member)
        return

    def delete_member(self, id):
         self._members = [item for item in self._members if item['id'] != id]
        # Fill this method and update the return
         return self.members

    def get_member(self, id):
        member = [row for row in self._members if row['id'] == id]
        return member


    def get_last_name(self):
       return self.last_name


       # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
