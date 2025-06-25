
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
        if pricing["B"][1] > 0:
            total_price_B = self.offer_check_B(sku=pricing["B"])
        if pricing["E"][1] > 0:
            total_price_E =self.offer_check_E(sku=pricing["E"])

        return total_price + total_price_A + total_price_B + total_price_E

    def offer_check_A(self, sku: tuple[int, int]) -> int:
        offer = 0
        remaining = 0
        sku_price = sku[0]
        sku_frequency = sku[1]
        if sku_frequency >= 5:
            group_5 = sku_frequency // 5
            remaining = sku_frequency % 5

            offer += group_5 * 200
            offer += remaining * sku_price
        elif sku_frequency >= 3:
            group_3 = sku_frequency // 3
            remaining = sku_frequency % 3

            offer += group_3 * 130
            offer += remaining * sku_price
        else:
            offer += sku_frequency * sku_price
        return offer

    def offer_check_B(self, sku: tuple[int, int]) -> int:
        offer = 0
        remaining = 0

        sku_price = sku[0]
        sku_frequency = sku[1]
        if sku_frequency >= 2:
            group_2 = sku_frequency // 2
            remaining = sku_frequency % 2

            offer += group_2 * 45
            offer += remaining * sku_price
        else:
            offer += sku_frequency * sku_price

        return offer

    def offer_check_E(self, sku: tuple[int, int]) -> int:
        offer = 0
        remaining = 0

        sku_price = sku[0]
        sku_frequency = sku[1]
        if sku_frequency >= 2:
            group_2 = sku_frequency // 2
            remaining = sku_frequency % 2

            offer += sku_frequency * 40
            # offer += remaining * sku_price + (group_2 * 30)
        else:
            offer += sku_frequency * sku_price

        return offer




