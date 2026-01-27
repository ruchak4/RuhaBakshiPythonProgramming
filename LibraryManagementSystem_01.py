# Simple Library Management System #
# Show Menu to the user (User input)
# Show user all the available books
# User can borrow a book at a time
# User can return a book at a time

book1 = 'Harry Potter and The Chamber of Secrets'
book2 = 'Matilda'
book3 = 'Polar Express'

isAvailable_book1 = True
isAvailable_book2 = True
isAvailable_book3 = True

def show_books():
    print('Available books are: ')
    print('Book No.', 'Book Name')
    if isAvailable_book1:
        print('1. ', book1)
        
    if isAvailable_book2:    
        print('2. ', book2)
        
    if isAvailable_book3:
        print('3. ', book3)
    

def borrow_book():
    global isAvailable_book1, isAvailable_book2, isAvailable_book3
    
    choice = input('Enter book number to borrow: ')
    
    if choice == '1' and isAvailable_book1:
        print('You have borrowed', book1)
        isAvailable_book1 = False
        
    elif choice == '2' and isAvailable_book2:
        print('You have borrowed', book2)
        isAvailable_book2 = False
        
    elif choice == '3' and isAvailable_book3:
        print('You have borrowed', book3)
        isAvailable_book3 = False
        
    else:
        print('Sorry, this book is not available')
        
        
def return_book():
    global isAvailable_book1, isAvailable_book2, isAvailable_book3
    
    print('Below are the books which are borrowed')
    print('book number book name')
    
    borrowed = False
    
    if isAvailable_book1 == False:
        print('1.', book1)
        borrowed = True
        
    if isAvailable_book2 == False:
        print('2.', book2)
        borrowed = True
    
    if isAvailable_book3 == False:
        print('3.', book3)
        borrowed = True
        
    if borrowed == False:
        print('You have not borrowed any book!')
        return
        
    return_choice = input('Enter book number to return: ')
    
    if return_choice == '1' and isAvailable_book1 == False:
       print(book1,' has been returned')
       isAvailable_book1 = True
    
    elif return_choice == '2' and isAvailable_book2 == False:
       print(book2,' has been returned')
       isAvailable_book2 = True
    
    elif return_choice == '3' and isAvailable_book3 == False:
       print(book3,' has been returned')
       isAvailable_book3 = True
    
    else:
        print('Invalid return choice OR the book is not borrowed!!')

while True:
    print('\n------This is the Library Menu------')
    print('1. Show books')
    print('2. Borrow book')
    print('3. Return book')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        show_books()
        
    elif choice == '2':
        borrow_book()
        
    elif choice == '3':
        return_book()
        
    elif choice == '4':
        print('GoodBye!!')
        break


        
    
    




  
    
         