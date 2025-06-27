class CheckoutSolution:
#  Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
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

        temp_price = 0
        for sku_id, pricing_quantity in pricing.items():
            breakpoint()
            if sku_id == "A":
                temp_price += self.offer_for_sku_give_n_total(sku_quantity=pricing_quantity[1], offer_quantity=(3, 5), discount_amount=(130, 200))

        # breakpoint()
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

        f_offer = f_count // 3
        # breakpoint()
        f_count -= f_offer
        total = f_count * price
        return total


    def offer_for_sku_give_n_total(self, sku_quantity: int, sku_price: int, offer_quantity: tuple[int, int], discount_amount: tuple[int, int]) -> int:
        total = 0
        # price = sku[0]
        # freq = sku[1]

        # Apply 5 deal first
        group_5 = sku_quantity // offer_quantity[1]
        sku_quantity %= offer_quantity[1]
        total += group_5 * 200

        # Apply 3 deal afterwards
        group_3 = sku_quantity // offer_quantity[0]
        sku_quantity %= 3
        total += group_3 * 130

        # Add the remainder to the total pricing
        total += sku_quantity * sku_price
        return total

        return 0