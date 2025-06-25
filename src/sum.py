def sum(num_1: int, num_2: int) -> int:
    """
    Sum recieves inputs num_1 and num_2 and returns addition
    Sum does not accept values outside the bounds of 0-100
    """

    if (num_1 < 0 or num_2 < 0) or (num_1 > 100 or num_2 > 100):
        raise(ValueError) 

    return num_1 + num_2
