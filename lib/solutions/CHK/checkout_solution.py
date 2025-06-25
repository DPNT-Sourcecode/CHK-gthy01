
class CheckoutSolution:

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


# Requirements


    # skus = unicode string
    def checkout(self, skus):
        """
        - param[0] = a string containing the SKUs of all the products in the basket
        - @return = an integer representing the total checkout value of the items
        """
        if skus == "":
            return 0
        skus_on_offer = ["A", "B", "E"]
        pricing: dict[str, tuple[int, int]] = { "A": (50, 0), "B": (30, 0), "C": (20, 0), "D": (15, 0), "E": (40, 0) }

        total_price = 0
        for sku in skus:
            if sku not in pricing:
                return -1 # Returning -1 as it's our base case
            if sku not in skus_on_offer:
                total_price += pricing[sku][0]

            pricing[sku] = (pricing[sku][0], 1 + pricing[sku][1])
        breakpoint()

        if pricing["A"][1] > 0:
            # X the offer amount of 150 * how many times pricing is divisible by 3
            # then I need the remainder of the overall total occurances and then I need to add that by 50 
            # then add both values to get total amount
            offers = (pricing["A"][1] // 3) * 130
            remaining = 0
            if pricing["A"][1] % 3 != 0:
                remaining = (pricing["A"][1] % 3) * 50
            # breakpoint()
            total_price += offers + remaining

        # Duplication probably not needed as we always have constant values on our hashmap
        if pricing["B"][1] > 0:
            offers = (pricing["B"][1] // 2) * 45
            remaining = 0

            if pricing["B"][1] % 2 != 0:
                remaining = (pricing["B"][1] % 2) * 30
            total_price += offers + remaining

        if pricing["E"][1] > 0:
            offers = ((pricing["E"][1] // 2) * 40) + 30
            remaining = 0

            if pricing["E"][1] % 2 != 0:
                remaining = (pricing["E"][1] % 2) * 30


            total_price += offers + remaining

        # breakpoint()
        return total_price





