"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    # TODO: need to implement this

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {}, {}, {}, {}>".format(self.first_name, 
                self.last_name, self.email, self.password)

def read_customer(filepath):

    customer = {}

    with open(filepath) as file:  # automatically closes the file
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.rstrip().split("|")
    
            customer[email] = Customer(first_name,
                                       last_name,
                                       email,
                                       password)

            # can use: customer[email] = Customer(*line.rstrip().split("|"))

    return customer


def get_by_email(email):

    return customer.get(email, False)




customer = read_customer("customers.txt")


