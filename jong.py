#!/usr/bin/env python
# coding: utf-8

# In[ ]:


o=[]
while True:
    print("Menu")
    print("A. Add Bookmarks")
    print("B. Edit Bookmarks")
    print("C. Delete Bookmarks")
    print("D. View Bookmarks")
    print("E. EXIT")
    x=input("Transaction: ( USE UPPERCASE LETTERS ONLY )")
    
    if x=='A':
        a=input("Add Bookmark: ")
        o.append(a)
        print("  ")
    if x=='B':
        print("Bookmarks: ",o)
        b=input("Edit Bookmark: ")
        o.remove(b)
        d=input("New Bookmark: ")
        o.append(d)
        print("  ")
    if x=='C':
        c=input("Delete Bookmark: ")
        o.remove(c)
        print("  ")
    if x=='D':
        print(o)
        print("  ")
    if x=='E':
        print("Thankyou For Everything Godbless")
        break
    


# In[ ]:




