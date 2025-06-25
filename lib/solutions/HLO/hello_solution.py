
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name: str) -> str:
        """
         - param[0] = a String containing a name
         - @return = a String containing a message
        """
        if friend_name == "":
            # Possibly not valid as this would be considered invalid
            # Assuming, we don't want to accept null value
            raise(ValueError)

        if not self.valid_name(friend_name):
            return "Hello, World!"

        return f"Hello, {friend_name}!"

    def valid_name(self, name: str) -> str | None:
        """ Responsible for managing when the name provided is valid"""
        return name

