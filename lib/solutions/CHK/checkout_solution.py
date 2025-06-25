
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
        offers = 0
        remaining = 0

        total_price = 0
        for sku in skus:
            if sku not in pricing:
                return -1 # Returning -1 as it's our base case
            if sku not in skus_on_offer:
                total_price += pricing[sku][0]

            pricing[sku] = (pricing[sku][0], 1 + pricing[sku][1])

        if pricing["A"][1] > 0:
            # TODO: Need to isolate the offers vs a mix
            # Checking different offers before adding
            if pricing["A"][1] % 3 == 0 and pricing["A"][1] % 5 == 0: 
                offers += (pricing["A"][1] // 3) * 130
                offers += (pricing["A"][1] // 5) * 200
            elif pricing["A"][1] % 3 == 0:
                remaining = (pricing["A"][1] % 3) * 50
            elif pricing["A"][1] % 5 == 0:
                offers = (pricing["A"][1] // 5) * 200
            else:
                remaining = (pricing["A"][1] % 5) * 50
            total_price += offers + remaining

        if pricing["B"][1] > 0:
            offers = (pricing["B"][1] // 2) * 45

            if pricing["B"][1] % 2 != 0:
                remaining = (pricing["B"][1] % 2) * 30
            total_price += offers + remaining

        if pricing["E"][1] > 0:
            offers = ((pricing["E"][1] // 2) * 40) + 30

            if pricing["E"][1] % 2 != 0:
                remaining = (pricing["E"][1] % 2) * 30
            total_price += offers + remaining

        return total_price


