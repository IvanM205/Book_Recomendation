# Book class

class Book:
    def __init__(self, title, authors, description):
        self.title = title # string - the title of the book
        self.authors = authors # string - the author or the authors of the book
        self.description = description # string - the description of the book
        self.category = [] # list of categories to which the book belongs
    '''
    The category of the book is defined in the graph data stracture. The edge from the vertex representing 
    the category to the vertex representing the book defines the book's belonging to that category.
    Each book can belong to several categories.
    '''
    def __repr__(self):
        return(
            f"The book entitled {self.title} that was written by {self.authors} "
            f"has the following description: {self.description}"
        )
    # Helpers functions
    def get_title(self): 
        return self.title
    
    def get_authors(self):
        return self.authors
    
    def get_description(self):
        return self.description
    
    def get_category(self):
        return self.category
