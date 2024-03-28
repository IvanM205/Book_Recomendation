# The main file
from category import Category
from book import Book
import csv
# Setting categories
# Extraction of categories from the dataset
def extract_categories_from_csv(filename):
    categories = set()

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract category string from the 'Category' column
            category_string = row['Category']
            # Split the category string by comma and strip whitespace
            category_list = [category.strip() for category in category_string.split(',')]
            # Add each category to the set
            categories.update(category_list)
    return categories

# Path to the CSV file
data_set_filename = "/Volumes/Ivan1TB/Codecademy projects/Computer Science Career path/Recomendation software/data_set/BooksDatasetClean.csv"

# Extract categories
all_categories = extract_categories_from_csv(data_set_filename)

# Sort all categories
sorted_categories = sorted(all_categories)

# Store all unique categories in categories.csv
csv_filename = "data/categories.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Name'])
    # Write data
    for category in sorted_categories:
        category_instance = Category(category)
        writer.writerow([category_instance.name])
    
# Set category dictionnary
category_dict = {}
for each in sorted_categories:
    category_dict[each] = None
    
# Setting books
books_dict = {}
# Extraction of books from the dataset
def extract_books_from_csv(filename):
    books = set()
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract title string from the 'Title' column
            title = row['Title']
            # Extract authors from the 'Authors' column
            authors = row['Authors']
            authors = authors.replace("By ", "")
            # Extract description from the 'Description' column
            description = row['Description'] 
            # Extract category string from the 'Category' column
            category_of_book = row['Category']
            # Split the category string by comma and strip whitespace
            category_book_list = [category.strip() for category in category_of_book.split(',')]
            book_instance = Book(title, authors, description)
            book_instance.category = category_book_list
            books_dict[book_instance.get_title()] = book_instance
            for category in category_book_list:
                if category_dict[category] is None:
                    category_dict[category] = [book_instance]
                else:
                    category_dict[category] += [book_instance]
    return books_dict

extract_books_from_csv(data_set_filename)

# Store all the books in books.csv
csv_filename = "data/books.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Title', 'Authors', 'Description', 'Categories'])
    # Write data
    for title in books_dict.keys():
        writer.writerow([books_dict[title].title, books_dict[title].authors, books_dict[title].description, ', '.join(books_dict[title].category)])
    
# Store all authors in authors.csv
csv_filename = "data/authors.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Authors'])
    # Write data
    for key in books_dict.keys():
        writer.writerow([books_dict[key].authors])

# Set authors dictionnary
        
authors_dict = {}
for key in books_dict.keys():
    current_authors = books_dict[key].get_authors()
    authors_dict[current_authors] = None
for key in books_dict.keys():
    current_authors = books_dict[key].get_authors()
    if authors_dict[current_authors] is None:
        authors_dict[current_authors] = [books_dict[key]]
    else:
        authors_dict[current_authors] += [books_dict[key]]

# Initialise the console
welcome_string = """
                                                                                             
 ,-----.,--.  ,--. ,-----.  ,-----.  ,---.  ,------.    ,-----.   ,-----.  ,-----. ,--. ,--. 
'  .--./|  '--'  |'  .-.  ''  .-.  ''   .-' |  .---'    |  |) /_ '  .-.  ''  .-.  '|  .'   / 
|  |    |  .--.  ||  | |  ||  | |  |`.  `-. |  `--,     |  .-.  \|  | |  ||  | |  ||  .   '  
'  '--'\|  |  |  |'  '-'  ''  '-'  '.-'    ||  `---.    |  '--' /'  '-'  ''  '-'  '|  |\   \ 
 `-----'`--'  `--' `-----'  `-----' `-----' `------'    `------'  `-----'  `-----' `--' '--'                                                                   
"""
print(welcome_string)

# Choose by title, category or author
def set_choice_parameter():
    print("Do you want to choose your book by its title, its category or its author?")
    answering = True
    choice_parameter = None
    while answering:
        answer = input("For title input \"T\", for category input \"C\", for author input \"A\": ")
        if answer == "T":
            choice_parameter = "Title"
            print("You will choose your book by its title.")
            answering = False
            return choice_parameter
        elif answer == "C":
            choice_parameter = "Category"
            print("You will choose your book by its categroy.")
            answering = False
            return choice_parameter
        elif answer == "A":
            choice_parameter = "Authors"
            print("You will choose your book by its authors.")
            answering = False
            return choice_parameter
        else:
            print("Invalid input! Choose from these: (T/C/A)")

def search_by_title(input_text):
    to_show = []
    for key in books_dict.keys():
        title_text = books_dict[key].get_title()
        if title_text[:len(input_text)] == input_text:
            to_show.append(title_text)
    if len(to_show) == 0:
        print("No such a title found !")
    else:
        for each in range(len(to_show)):
            print(f"{each+1}) {to_show[each]}")
        answering = True
        book_number = None 
        while answering:
            answer = input("Input the number of your book: ")
            answer = int(answer)
            if isinstance(answer, int) and answer >= 1 and answer <= len(to_show):
                print(f"You chose the book number {answer}")
                book_number = answer - 1
                answering = False
            else:
                print(f"Invalid input! Write an integer from 1 to {len(to_show)}")
        chosen_title = to_show[book_number]
        return books_dict[chosen_title]

def search_by_category(input_text):
    to_show = []
    for key in category_dict.keys():
        category_name = key
        if category_name[:len(input_text)] == input_text:
            to_show.append(category_name)
    if len(to_show) == 0:
        print("No such a title found !")
    else:
        for each in range(len(to_show)):
            print(f"{each+1}) {to_show[each]}")
        answering = True
        category_number = None 
        while answering:
            answer = input("Input the number of your category: ")
            answer = int(answer)
            if isinstance(answer, int) and answer >= 1 and answer <= len(to_show):
                print(f"You chose the category number {answer}")
                category_number = answer - 1
                answering = False
            else:
                print(f"Invalid input! Write an integer from 1 to {len(to_show)}")
        chosen_category = to_show[category_number]
        books_to_show = [each.get_title() for each in category_dict[chosen_category]]
        print(f"The following books were found in {chosen_category}: ")
        for each in range(len(books_to_show)):
            print(f"{each+1}) {books_to_show[each]}")
        answering = True
        book_number = None 
        while answering:
            answer = input("Input the number of your book: ")
            answer = int(answer)
            if isinstance(answer, int) and answer >= 1 and answer <= len(books_to_show):
                print(f"You chose the book number {answer}")
                book_number = answer - 1
                answering = False
            else:
                print(f"Invalid input! Write an integer from 1 to {len(books_to_show)}")
        chosen_book = books_to_show[book_number]
        return books_dict[chosen_book]     

def search_by_author(input_text):
    to_show = []
    for key in authors_dict.keys():
        authors_name = key
        if authors_name[:len(input_text)] == input_text:
            to_show.append(authors_name)
    if len(to_show) == 0:
        print("No such a title found !")
    else:
        for each in range(len(to_show)):
            print(f"{each+1}) {to_show[each]}")
        answering = True
        authors_number = None 
        while answering:
            answer = input("Input the number of your author: ")
            answer = int(answer)
            if isinstance(answer, int) and answer >= 1 and answer <= len(to_show):
                print(f"You chose the category number {answer}")
                authors_number = answer - 1
                answering = False
            else:
                print(f"Invalid input! Write an integer from 1 to {len(to_show)}")
        chosen_author = to_show[authors_number]
        books_to_show = [each.get_title() for each in authors_dict[chosen_author]]
        print(f"The following books were found that are written by {chosen_author}: ")
        for each in range(len(books_to_show)):
            print(f"{each+1}) {books_to_show[each]}")
        answering = True
        book_number = None 
        while answering:
            answer = input("Input the number of your book: ")
            answer = int(answer)
            if isinstance(answer, int) and answer >= 1 and answer <= len(books_to_show):
                print(f"You chose the book number {answer}")
                book_number = answer - 1
                answering = False
            else:
                print(f"Invalid input! Write an integer from 1 to {len(books_to_show)}")
        chosen_book = books_to_show[book_number]
        return books_dict[chosen_book]

def main_function():
    choice_parameter = set_choice_parameter()
    if choice_parameter == "Title":
        print("You will type the tilte of the desired book or its beginning")
        input_text = input("Input here: ")
        result = search_by_title(input_text)
        print("\n")
        print(result)
        print("\n")
    elif choice_parameter == "Category":
        print("You will type the category of your desired book or its beginning")
        input_text = input("Input here: ")
        result = search_by_category(input_text)
        print("\n")
        print(result)
        print("\n")
    elif choice_parameter == "Authors":
        print("You will type the authors of your desired book or its beginning")
        input_text = input("Input here: ")
        result = search_by_author(input_text)
        print("\n")
        print(result)
        print("\n")
    
user_active = True
while user_active:
    main_function()
    asking = True
    while asking:
        print("Do you want to continue? (Y/N) ")
        answer = input("Input here: ")
        if answer == "Y":
            break
        elif answer == "N":
            user_active = False
            break
        else:
            print("Invalid input! Input \"Y\" for YES or input \"N\" for No")
        
bye_string = """
                                                             ,---. 
 ,----.                    ,--.    ,-----.                    |   | 
'  .-./    ,---.  ,---.  ,-|  |    |  |) /_,--. ,--.,---.     |  .' 
|  | .---.| .-. || .-. |' .-. |    |  .-.  \\  '  /| .-. :    |  |  
'  '--'  |' '-' '' '-' '\ `-' |    |  '--' / \   ' \   --.    `--'  
 `------'  `---'  `---'  `---'     `------'.-'  /   `----'    .--.  
                                           `---'              '--' 
"""
print(bye_string)
