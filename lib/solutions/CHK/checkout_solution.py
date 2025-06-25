
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

        total_price_A= 0
        total_price_B= 0
        total_price_E= 0

        if pricing["A"][1] > 0:
            total_price_A = self.offer_check_A(sku=pricing["A"])
        if pricing["B"][1] > 0 and pricing["E"][1] > 0:
            total_price_B = self.offer_check_B(sku_B=pricing["B"], sku_E=pricing["E"])
        elif pricing["B"][1] > 0:
            total_price_B = self.offer_check_B(sku_B=pricing["B"])
        if pricing["E"][1] > 0:
            total_price_E =self.offer_check_E(sku=pricing["E"])

        return total_price + total_price_A + total_price_B + total_price_E

    def offer_check_A(self, sku: tuple[int, int]) -> int:
        total = 0
        price = sku[0]
        freq = sku[1]
        
        # Apply 5 deal first
        group_5 = freq // 5
        freq %= 5
        total += group_5 * 200

        # Apply 3 deal afterwards
        group_3 = freq // 3
        freq %= 3
        total += group_3 * 130

        # Add the remainder to the total pricing
        total += freq * price
        return total

    def offer_check_B(self, sku_B: tuple[int, int], sku_E: tuple[int, int] = (40, 0)) -> int:
        total = 0
        price = sku_B[0]
        freq = sku_B[1]
        breakpoint()
        # Apply 2 deal afterwards
        group_2 = freq // 2
        freq %= 2
        total += group_2 * 45

        # Add the remainder to the total pricing
        total += freq * price

        group_E = sku_E[1] // 2
        if (group_E * 30) >= total:
            total = 0
        else:
            total -= (group_E * 30)
        return total


    def offer_check_E(self, sku: tuple[int, int]) -> int:
        return sku[1] * sku[0]



