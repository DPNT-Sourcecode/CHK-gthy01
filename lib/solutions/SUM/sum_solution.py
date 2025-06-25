
class SumSolution:

    def compute(self, x, y):
        """
        Sum recieves inputs num_1 and num_2 and returns addition
        Sum does not accept values outside the bounds of 0-100
        """

        if (x < 0 or y < 0) or (x > 100 or y > 100):
            raise(ValueError) 

        return x + y
