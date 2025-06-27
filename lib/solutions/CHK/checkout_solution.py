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
            "A": [50, 0],  # offer /
            "B": [30, 0],  # offer /
            "C": [20, 0],
            "D": [15, 0],
            "E": [40, 0],  # offer
            "F": [10, 0],  # offer
            "G": [20, 0],
            "H": [10, 0],  # offer /
            "I": [35, 0],
            "J": [60, 0],
            "K": [80, 0],  # offer /
            "L": [90, 0],
            "M": [15, 0],
            "N": [40, 0],  # offer
            "O": [10, 0],
            "P": [50, 0],  # offer /
            "Q": [30, 0],  # offer /
            "R": [50, 0],  # offer
            "S": [30, 0],
            "T": [20, 0],
            "U": [40, 0],  # offer
            "V": [50, 0],  # offer /
            "W": [20, 0],
            "X": [90, 0],
            "Y": [10, 0],
            "Z": [50, 0],
        }

        total_price = 0
        for sku in skus:
            if sku not in pricing:
                return -1  # Returning -1 as it's our base case
            pricing[sku] = [pricing[sku][0], 1 + pricing[sku][1]]
        total_price += self.buy_n_amount_and_get_free_skus(pricing)
        for sku_id, pricing_quantity in pricing.items():
            if (
                sku_id in ["A", "B", "H", "K", "P", "Q", "V"]
                and pricing_quantity[1] > 0
            ):
                sku_price = pricing_quantity[0]
                sku_quantity = pricing_quantity[1]
                total_price += self.offer_price_reduction(
                    sku_id, sku_quantity, sku_price
                )

            if sku_id not in skus_on_offer and pricing_quantity[1] > 0:
                total_price += pricing_quantity[0]

        return total_price

    def buy_n_amount_and_get_free_skus(
        self,
        pricing: dict[str, list[int, int]],
    ) -> int:
        total_price = 0
        if pricing["E"][1] > 0:
            sku_price = pricing["E"][0]
            sku_quantity = pricing["E"][1]

            deducted_sku = self.offer_for_free_skus(pricing["E"][1], 2)
            total_price += sku_price * sku_quantity
            pricing["B"][1] -= deducted_sku

        if pricing["F"][1] > 0:
            sku_price = pricing["F"][0]
            sku_quantity = pricing["F"][1]

            deducted_sku = self.offer_for_free_skus(sku_quantity, 2)
            pricing["F"][1] -= deducted_sku
            total_price += sku_price * sku_quantity  # Check here

        if pricing["N"][1] > 0:
            sku_price = pricing["N"][0]
            sku_quantity = pricing["N"][1]
            deducted_sku = self.offer_for_free_skus(sku_quantity, 4)
            pricing["M"][1] -= deducted_sku
            total_price += (sku_price * sku_quantity)

        if pricing["R"][1] > 0:
            sku_price = pricing["R"][0]
            sku_quantity = pricing["R"][1]
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            pricing["Q"][1] -= deducted_sku
            total_price += sku_price * sku_quantity

        if pricing["U"][1] > 0:
            sku_price = pricing["U"][0]
            sku_quantity = pricing["U"][1]
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            pricing["U"][1] -= deducted_sku
            total_price += sku_price * pricing["U"][1]
        return total_price

    def offer_price_reduction(
        self, sku_id: str, sku_quantity: int, sku_price: int
    ) -> int:
        total = 0
        if sku_id == "A":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(3, 5),
                discount_amount=(130, 200),
            )
            return total

        if sku_id == "B":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(2, 0),
                discount_amount=(45, 0),
            )
            return total
        
        if sku_id == "H":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(5, 10),
                discount_amount=(45, 80),
            )
            return total

        if sku_id == "K":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(2, 0),
                discount_amount=(150, 0),
            )
            return total

        if sku_id == "P":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(5, 0),
                discount_amount=(200, 0),
            )
            return total

        if sku_id == "Q":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(3, 0),
                discount_amount=(80, 0),
            )
            return total

        if sku_id == "V":
            total += self.offer_for_sku_give_n_total(
                skus=sku_quantity,
                price=sku_price,
                offer=(2, 3),
                discount_amount=(90, 130),
            )
            return total

    def offer_for_free_skus(self, sku_count, offer: int) -> int:
        return sku_count // offer

    def offer_for_sku_give_n_total(
        self,
        skus: int,
        price: int,
        offer: list[int, int],
        discount_amount: list[int, int],
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



