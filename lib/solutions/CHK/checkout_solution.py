
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


        total_price_A = self.offer_check_A(sku=pricing["A"], total_price=total_price)
        total_price_B = self.offer_check_B(sku=pricing["B"], total_price=total_price)
        total_price_E =self.offer_check_E(sku=pricing["E"], total_price=total_price)

        # if pricing["A"][1] > 0:
        #     # TODO: Need to isolate the offers vs a mix
        #     # Checking different offers before adding
            # if pricing["A"][1] % 3 == 0 and pricing["A"][1] % 5 == 0: 
            #     offers += (pricing["A"][1] // 3) * 130
            #     offers += (pricing["A"][1] // 5) * 200
            # elif pricing["A"][1] % 3 == 0:
            #     offers += (pricing["A"][1] // 3) * 130
            # elif pricing["A"][1] % 5 == 0:
            #     offers = (pricing["A"][1] // 5) * 200
            # else:
            #     remaining = (pricing["A"][1] % 5) * 50
            # total_price += offers + remaining


        # if pricing["B"][1] > 0:
        #     offers = (pricing["B"][1] // 2) * 45

        #     if pricing["B"][1] % 2 != 0:
        #         remaining = (pricing["B"][1] % 2) * 30
        #     total_price += offers + remaining

        # if pricing["E"][1] > 0:
        #     offers = ((pricing["E"][1] // 2) * 40) + 30

        #     if pricing["E"][1] % 2 != 0:
        #         remaining = (pricing["E"][1] % 2) * 30
        #     total_price += offers + remaining
        breakpoint()
        return total_price + total_price_A + total_price_B + total_price_E

    def offer_check_A(self, sku: tuple[int, int], total_price: int):
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

    def offer_check_B(self, sku: tuple[int, int], total_price: int):
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
            offer += sku_frequency + sku_price

        return offer

    def offer_check_E(self, sku: tuple[int, int], total_price: int):
        offer = 0
        remaining = 0

        sku_price = sku[0]
        sku_frequency = sku[1]
        if sku_frequency >= 2:
            group_2 = sku_frequency // 2
            remaining = sku_frequency % 2

            offer += group_2 * 30
            offer += remaining * sku_price
        else:
            offer += sku_frequency + sku_price
        return total_price