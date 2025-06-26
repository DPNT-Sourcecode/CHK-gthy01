class CheckoutSolution:
    # +------+-------+------------------------+
    # | Item | Price | Special offers         |
    # +------+-------+------------------------+
    # | A    | 50    | 3A for 130, 5A for 200 |
    # | B    | 30    | 2B for 45              |
    # | C    | 20    |                        |
    # | D    | 15    |                        |
    # | E    | 40    | 2E get one B free      |
    # | F    | 10    | 2F get one F free      |
    # +------+-------+------------------------+

    # skus = unicode string
    def checkout(self, skus):
        """
        - param[0] = a string containing the SKUs of all the products in the basket
        - @return = an integer representing the total checkout value of the items
        """
        if skus == "":
            return 0
        skus_on_offer = ["A", "B", "E", "F"]
        pricing: dict[str, tuple[int, int]] = {
            "A": (50, 0),
            "B": (30, 0),
            "C": (20, 0),
            "D": (15, 0),
            "E": (40, 0),
            "F": (10, 0),
        }
        total_price = 0
        for sku in skus:
            if sku not in pricing:
                return -1  # Returning -1 as it's our base case
            if sku not in skus_on_offer:
                total_price += pricing[sku][0]

            pricing[sku] = (pricing[sku][0], 1 + pricing[sku][1])

        if pricing["A"][1] > 0:
            total_price += self.offer_check_A(sku=pricing["A"])
        if pricing["B"][1] > 0:
            total_price += self.offer_check_B(sku_B=pricing["B"], sku_E=pricing["E"])
        if pricing["E"][1] > 0:
            total_price += self.offer_check_E(sku=pricing["E"])
        if pricing["F"][1] > 0:
            total_price += self.offer_check_F(sku=pricing["F"])

        return total_price

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

    def offer_check_B(
        self, sku_B: tuple[int, int], sku_E: tuple[int, int] = (40, 0)
    ) -> int:
        b_count = sku_B[1]
        e_count = sku_E[1]

        # Calculate E offer and remove Bs from total before calculating
        e_offer = e_count // 2
        b_count -= e_offer

        total = 0
        price = sku_B[0]

        b_pair_count = b_count // 2
        leftover_b = b_count % 2
        total = b_pair_count * 45 + leftover_b * price
        return total

    def offer_check_E(self, sku: tuple[int, int]) -> int:
        return sku[1] * sku[0]

    def offer_check_F(self, sku: tuple[int, int]) -> int:
        f_count = sku[1]
        price = sku[0]

        f_offer = f_count // 2

        # TODO: Add division based on offer amount
        breakpoint()
        f_count -= f_offer

        total = f_count * price
        return total
