
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name: str) -> str:
        """
         - param[0] = a String containing a name
         - @return = a String containing a message
        """
        # Could add some handling around if str is empty
        if friend_name == "":
            # Ideally better to handle this Error more appropriately 
                # - e.g. custom exceptions and error messaging which then would be asserted
            # But for this simple test I think it's maybe overkill
            raise(ValueError)

        # TODO: Handle valid names
        
        return f"Hello, {friend_name}"

