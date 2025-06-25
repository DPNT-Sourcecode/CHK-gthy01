
class CheckoutSolution:

    #     Our price table and offers:
    # +------+-------+----------------+
    # | Item | Price | Special offers |
    # +------+-------+----------------+
    # | A    | 50    | 3A for 130     |
    # | B    | 30    | 2B for 45      |
    # | C    | 20    |                |
    # | D    | 15    |                |
    # +------+-------+----------------+

# Requirements
#  - Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds.
#  - For example, item A might cost 50 pounds individually, but this week we have a special offer:
#  - buy three As and they'll cost you 130.
#  - For any illegal input return -1

    # skus = unicode string
    def checkout(self, skus):
        """
        - param[0] = a string containing the SKUs of all the products in the basket
        - @return = an integer representing the total checkout value of the items
        """
        breakpoint()
        _skus = skus.split()

        total_price = 0
        l, r: int = 0, len(_skus) - 1
        for sku in _skus:
            # Check whether or not skus equate to one another
            
        return -1 # Returning -1 as it's our base case




