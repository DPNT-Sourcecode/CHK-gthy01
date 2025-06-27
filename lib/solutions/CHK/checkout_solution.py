from typing import Any


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

    def checkout(self, skus):
        """
        - param[0] = a string containing the SKUs of all the products in the basket
        - @return = an integer representing the total checkout value of the items
        """
        if skus == "":
            return 0
        skus_on_offer = ["A", "B", "E", "F", "H", "K", "N", "P", "Q", "R", "U", "V"]
        pricing: dict[str, list[int, int]] = {
            "A": [50, 0],
            "B": [30, 0],
            "C": [20, 0],
            "D": [15, 0],
            "E": [40, 0],
            "F": [10, 0],
        }
        total_price = 0
        for sku in skus:
            if sku not in pricing:
                return -1  # Returning -1 as it's our base case
            if sku not in skus_on_offer:
                total_price += pricing[sku][0]

            pricing[sku] = [pricing[sku][0], 1 + pricing[sku][1]]


        if pricing["E"][1] > 0:
            deducted_sku = self.offer_for_free_skus(pricing["E"][1], 2)
            total += s * sku_quantity
            pricing["B"][1] -= deducted_sku

        if sku_id == "F":
            deducted_sku = self.offer_for_free_skus(sku_quantity, 2)
            pricing["F"][1] -= deducted_sku
            total += sku_price * sku_quantity

        if sku_id == "N":
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            pricing["M"][1] -= deducted_sku
            total += sku_price * sku_quantity

        if sku_id == "R":
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            pricing["Q"][1] -= deducted_sku
            total += sku_price * sku_quantity

        if sku_id == "U":
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            pricing["U"][1] -= deducted_sku
            total += sku_price * sku_quantity

        for sku_id, pricing_quantity in pricing.items():
            if sku_id in skus_on_offer:
                total_price += self.translate_skus_to_offers(
                    sku_id=sku_id,
                    sku_price=pricing_quantity[0],
                    sku_quantity=pricing_quantity[1],
                    pricing=pricing,
                )

        return total_price


    def offer_check_B(
        self, sku_B: tuple[int, int], sku_E: tuple[int, int] = (40, 0)
    ) -> int:
        b_count = sku_B[1]
        e_count = sku_E[1]

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
        f_count -= f_offer
        total = f_count * price
        return total

    def translate_skus_to_offers(
        self,
        sku_id: str,
        sku_quantity: int,
        sku_price: int,
        pricing: dict[str, list[int, int]],
    ) -> int:
        total = 0

        

        if sku_id in ["A", "B", "H", "P", "Q", "V"]:
            total += self.offers_for_skus_give_n_total(sku_id, sku_quantity, sku_price)
        return total

    def offers_for_skus_give_n_total(
        self, sku_id: str, sku_quantity: int, sku_price: int
    ) -> int:
        if sku_id == "A":
            return self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(3, 5),
                discount_amount=(130, 200),
            )

        if sku_id == "B":
            return self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(2, 0),
                discount_amount=(45, 0),
            )

        if sku_id == "H":
            return self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(5, 10),
                discount_amount=(45, 80),
            )

        if sku_id == "P":
            return self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(5, 0),
                discount_amount=(200, 0),
            )

        if sku_id == "Q":
            return self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(3, 0),
                discount_amount=(80, 0),
            )

        if sku_id == "V":
            return self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(2, 3),
                discount_amount=(90, 130),
            )

    def offer_for_free_skus(self, sku_count, offer: int) -> int:
        return sku_count // offer


    def offer_for_sku_give_n_total(
        self,
        skus: int,
        price: int,
        offer: tuple[int, int],
        discount_amount: tuple[int, int],
    ) -> int:
        total = 0

        # Apply 5 deal first
        if offer[1] > 0:
            group_5 = skus // offer[1]
            skus %= offer[1]
            total += group_5 * discount_amount[1]

        # Apply 3 deal afterwards
        group_3 = skus // offer[0]
        skus %= offer[0]
        total += group_3 * discount_amount[0]

        # Add the remainder to the total pricing
        total += skus * price
        return total



