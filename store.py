class Store:
    """
    Class for managing store
    """
    def __init__(self, name='Store', num_workers=0,
                 contact_number='+7(999)999-99-99'):
        self.name = name
        self.num_workers = num_workers
        self.contact_number = contact_number

    @property
    def email(self):
        return self.name + '@email.com'

    @property
    def contacts(self):
        return {"Contact Number": self.contact_number,
                "Email": self.email}

    def hire_workers(self, num_workers=1):
        self.num_workers += num_workers


class GroceryStore(Store):
    """
    Subclass for managing Grocery Store
    """
    def __init__(self, name, num_workers, num_vegetables=0):
        super().__init__(name, num_workers)
        self.num_vegetables = num_vegetables

    def order_vegetables(self, num_vegetables=1):
        self.num_vegetables += num_vegetables
