import operator

my_file= open("text.txt", "r").read()
#print my_file

#_count the number of times a word has been used

list_count={

}

list=my_file.replace(".", "").replace("'", "").replace("?", "").replace(":", "").replace("\"", "").replace("\n", " ").replace(",", "").split(" ")

# print list

for element in list:
    if element in list_count.keys():
        list_count[element]+= 1
    else:
        list_count[element]=1

#print list_count

#Make a function to sort the keys in order from biggest number of iteration
#
sorted_list_count=sorted(list_count.items(), key=operator.itemgetter(1))
final=sorted_list_count[::-1]

for word in final:
    print "%s : %s" % (word[0], word[1])
