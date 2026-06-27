class Account(object):

    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        print(self.__dict__)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")

        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")


    def transfer(self, amount):
        self.value += amount



# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []


    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return -1
        self.accounts.append(new_account)


    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """


    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
