
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
        _skus = skus.split()
        breakpoint()
        # Adapting pricing to take into account frequency
        # This should allow me to calculate the amount of offers fit into the pricing and frequency
        pricing: dict[str, tuple[int, int]] = { "A": (50, 0), "B": (30, 0), "C": (20, 0), "D": (15, 0) }  

        total_price = 0
        for sku in _skus:
            if sku not in pricing:
                return -1 # Returning -1 as it's our base case
            if sku not in ["A", "B"]:
                total_price += pricing[sku][0]

            pricing[sku] = (pricing[sku][0], 1 + pricing[sku][1])


        if pricing["A"]:
            # X the offer amount of 150 * how many times pricing is divisible by 3
            # then I need the remainder of the overall total occurances and then I need to add that by 50 
            # then add both values to get total amount
            offers = (pricing["A"][1] // 3) * 130
            remaining = 0
            if pricing["A"][1] % 3 != 0:
                remaining = (pricing["A"][1] % 3) * 50

            total_price += offers + remaining

        if "B" in pricing:
            offers = (pricing["B"][1] // 2) * 45
            remaining = 0

            if pricing["B"][1] % 2 != 0:
                remaining = (pricing["B"][1] % 2) * 30
            total_price += offers + remaining

        return total_price










