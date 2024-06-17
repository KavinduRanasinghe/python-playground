class MyFirstClass:
    print("“Who wrote this?”.")
    index = "Author-Book"
    
    def hand_list(self,philosopher,book):
        print(MyFirstClass.index)
        print("{} wrote the book: {}".format(philosopher,book))
        
        
        
        
    
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu","The Art of War")