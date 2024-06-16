list = ['Dog','Cat','Ant']

def finder(string):
    if string[0]=='A':
        return string




map_list = map(finder,list)
print("Map\n")
for x in map_list:
    print(x)
    
    

filter_list = filter(finder,list)
print("\nFilter\n")

for x in filter_list:
    print(x)
    
        
   