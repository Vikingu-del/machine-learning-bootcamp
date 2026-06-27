from typing import Union

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
            raise TypeError("every account should be an Account type")
        if any(acc.name == new_account.name for acc in self.accounts):
            raise ValueError(f"Account with name '{new_account.name}' already exists.")
        self.accounts.append(new_account)
        return 


    def transfer(self, origin, dest, amount) -> int:
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        orig_acc = next((acc for acc in self.accounts if acc.name == origin), None)
        dest_acc = next((acc for acc in self.accounts if acc.name == dest), None)

        if not orig_acc or not dest_acc:
            return False

        if self._is_corrupted(orig_acc) or self._is_corrupted(dest_acc):
            return False

        try:
            am = float(amount)
            if am < 0 or am > orig_acc.value:
                return False
            if orig_acc.name == dest_acc.name:
                return True

            orig_acc.value -= am
            dest_acc.value += am
            return True
        except ValueError:
            print('amount must be a float')
            return False


    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False

        # 1. Find the account
        account = next((acc for acc in self.accounts if acc.name == name), None)
        if not account:
            return False
        
        if self._is_corrupted(account):
            for attr in list(account.__dict__.keys()):
                if attr.startswith('b'):
                    delattr(account, attr)

            attrs = account.__dict__.keys()
            has_zip = any(attr.startswith("zip") for attr in attrs)
            has_addr = any(attr.startswith("addr") for attr in attrs)
            if not (has_zip or has_addr):
                setattr(account, 'addr', 'fixed_address')

            if not hasattr(account, 'id') or not isinstance(account.id, int):
                setattr(account, 'id', Account.ID_COUNT)
                Account.ID_COUNT += 1
            if not hasattr(account, 'value') or not isinstance(account.value, (int, float)):
                setattr(account, 'value', 0)

            if len(account.__dict__) % 2 == 0:
                setattr(account, 'dummy_fix', True)

            # Double check if our fixes worked
            return not self._is_corrupted(account)

    def _is_corrupted(self, account):
        attrs = account.__dict__.keys()

        if not isinstance(account, Account):
            print("Not an account object")
            return True


        if not {"id", "name", "value"}.issubset(set(attrs)):
            print("no id, name or value")
            return True

        # 2. Check types of name, id, value
        if not isinstance(account.name, str):
            print("wrong name")
            return True
        if not isinstance(account.id, int):
            print("wrong id")
            return True
        if not isinstance(account.value, int | float):
            print("wrong value")
            return True

        if any(attr.startswith("b") for attr in attrs):
            print("something starts with b")
            return True

        has_zip = any(attr.startswith("zip") for attr in attrs)
        has_addr = any(attr.startswith("addr") for attr in attrs)
        if not (has_zip or has_addr):
            print("no zip or addr")
            return True

        if len(attrs) % 2 == 0:
            print("even attrs")
            return True
        return False

def test():
    a = Account("Erik", value=100, zip="1001", addr="Leopoldauer strasse")
    b = Bank()
    b.add(a)
    if b._is_corrupted(a):
        print("a is corrupted")
    else:
        print("a is correct")

if __name__ == "__main__":
    test()
