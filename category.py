# Category class

class Category:
    def __init__(self, name):
        self.name = name
        """
        self.description = description
        self.similar_categories = []
        """

    def __repr__(self) -> str:
        return(
            f"The category is called {self.name}"
            """
            f"has the following description: {self.description}"
            f"the similar categories are these: {self.similar_categories}"
            """
        )
    def get_category_name(self):
        return self.name
    
    """
    def get_category_description(self):
        return self.description
    
    def get_similar(self):
        return self.similar_categories
    """
