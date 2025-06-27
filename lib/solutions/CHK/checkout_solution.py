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


    # +------+-------+---------------------------------+
    # | Item | Price | Special offers                  |
    # +------+-------+---------------------------------+
    # | A    | 50    | 3A for 130, 5A for 200          | x
    # | B    | 30    | 2B for 45                       | x
    # | C    | 20    |                                 |
    # | D    | 15    |                                 |
    # | E    | 40    | 2E get one B free               | x
    # | F    | 10    | 2F get one F free               | x
    # | G    | 20    |                                 |
    # | H    | 10    | 5H for 45, 10H for 80           | x
    # | I    | 35    |                                 |
    # | J    | 60    |                                 |
    # | K    | 70    | 2K for 120                      | x
    # | L    | 90    |                                 |
    # | M    | 15    |                                 |
    # | N    | 40    | 3N get one M free               | x
    # | O    | 10    |                                 |
    # | P    | 50    | 5P for 200                      | x
    # | Q    | 30    | 3Q for 80                       | x
    # | R    | 50    | 3R get one Q free               | x
    # | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 | n
    # | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 | n
    # | U    | 40    | 3U get one U free               | x
    # | V    | 50    | 2V for 90, 3V for 130           | x
    # | W    | 20    |                                 |
    # | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 | n
    # | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 | n
    # | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 | n
    # +------+-------+---------------------------------+

    def checkout(self, skus):
        """
        - param[0] = a string containing the SKUs of all the products in the basket
        - @return = an integer representing the total checkout value of the items
        """
        if skus == "":
            return 0
        skus_on_offer = [
            "A",
            "B",
            "E",
            "F",
            "H",
            "K",
            "N",
            "M",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "X",
            "Y",
            "Z"
        ]

        skus_on_direct_discount = ["A", "B", "H", "K", "P", "Q", "S", "T", "V", "X", "Y", "Z"]

        basket: dict[str, list[int, int]] = {
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
            "K": [70, 0],  # offer /
            "L": [90, 0],
            "M": [15, 0],
            "N": [40, 0],  # offer
            "O": [10, 0],
            "P": [50, 0],  # offer /
            "Q": [30, 0],  # offer /
            "R": [50, 0],  # offer
            "S": [20, 0],
            "T": [20, 0],
            "U": [40, 0],  # offer
            "V": [50, 0],  # offer /
            "W": [20, 0],
            "X": [17, 0],
            "Y": [20, 0],
            "Z": [21, 0],
        }

        total_price = 0
        temp_price = 0
        for sku in skus:
            if sku not in basket:
                return -1  # Returning -1 as it's our base case
            if sku not in skus_on_offer:
                total_price += basket[sku][0]
            basket[sku] = [basket[sku][0], 1 + basket[sku][1]]

        total_price += self.buy_n_amount_and_get_free_skus(basket)


        combo_offer = ["S", "T", "X", "Y", "Z"]
        combo_count = []
        # Iterate through every SKU ID
        # Track for when SKU ID is in combo offer
        # Add SKU ID to tracking list
        # compare all values within tracking list
        for sku_id, pricing_quantity in basket.items():
            price = pricing_quantity[0]
            quantity = pricing_quantity[1]

            if (
                sku_id in skus_on_direct_discount
                and pricing_quantity[1] > 0
            ):
                if sku_id in combo_offer:
                    combo_count.append(quantity)
                    continue
                else:
                    temp_price += self.offer_price_reduction(
                        sku_id, quantity, price
                    )

            if sku_id == "M":
                total_price += pricing_quantity[0] * pricing_quantity[1]

        if combo_count:
            total_price += self.offer_for_sku_give_n_total(
                skus=sum(combo_count),
                price=price,
                offer=(3, 0),
                discount_amount=(45, 0),
            )

        return total_price + temp_price

    def buy_n_amount_and_get_free_skus(
        self,
        basket: dict[str, list[int, int]],
    ) -> int:
        total_price = 0
        if basket["E"][1] > 0:
            sku_price = basket["E"][0]
            sku_quantity = basket["E"][1]

            deducted_sku = self.offer_for_free_skus(sku_quantity, 2)
            total_price += sku_price * sku_quantity
            if basket["B"][1] > 0:
                basket["B"][1] -= deducted_sku

        if basket["F"][1] > 0:
            sku_price = basket["F"][0]
            sku_quantity = basket["F"][1]

            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            basket["F"][1] -= deducted_sku
            total_price += sku_price *  basket["F"][1]

        if basket["N"][1] > 0:
            sku_price = basket["N"][0]
            sku_quantity = basket["N"][1]
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            if basket["M"][1] > 0:
                basket["M"][1] -= deducted_sku
            total_price += sku_price * sku_quantity

        if basket["R"][1] > 0:
            sku_price = basket["R"][0]
            sku_quantity = basket["R"][1]
            deducted_sku = self.offer_for_free_skus(sku_quantity, 3)
            if basket["R"][1] > 0:
                basket["Q"][1] -= deducted_sku
            total_price += sku_price * sku_quantity

        if basket["U"][1] > 0:
            sku_price = basket["U"][0]
            sku_quantity = basket["U"][1]
            deducted_sku = self.offer_for_free_skus(sku_quantity, 4)
            basket["U"][1] -= deducted_sku
            total_price += sku_price * basket["U"][1]
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
                discount_amount=(120, 0),
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

