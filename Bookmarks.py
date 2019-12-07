#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
bookmarks = []
while True:    
    print("A.Add Bookmarks")
    print("B.Edit Bookmarks")
    print("C.Delete Bookmarks")
    print("D.View Bookmarks")
    print("E.Exit")
    i = input("TRANSACTIONS......")
   
    if i == 'A':
        print(""" ---->> ENTER THE SITE YOU WANT TO ADD
              """ )
        z= input("")
        bookmarks.append(z)        
        
    elif i =='B':
        print(""" ---->> ENTER THE SITE YOU WANT TO EDIT
        """ )
        books = input("")
        if books in bookmarks:
            print("")  
            bookmarks.remove(books)        
        else:
            print("--No bookmarks exist--")  
        
            
    elif i =='C':
        print(""" ---->> ENTER THE SITE YOU WANT TO DELETE
        """ )
        book = input("")
        if book in bookmarks:
            print("--This bookmark will be deleted--")  
            bookmarks.remove(book)
        else:
            print("--No bookmarks exist--")        
                
    elif i =='D':
        print(""" ---->> ENTER THE SITE YOU WANT TO VIEW
        """ )
        print(bookmarks)
    elif i =='E':
        sys.exit(404)


# In[ ]:




