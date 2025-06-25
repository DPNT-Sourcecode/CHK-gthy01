
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name: str) -> str:
        """
         - param[0] = a String containing a name
         - @return = a String containing a message
        """
        # Could add some handling around if str is empty
        if not self.valid_name(friend_name):
            # TODO: Handle valid names
            raise(ValueError)


        return f"Hello, {friend_name}!"

    def 

