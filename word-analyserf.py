import operator
my_file= open("glossary.txt", "r", encoding = 'utf-8').read()
list_count={

}
list=my_file.replace(".", "").replace("'", "").replace("?", "").replace(":", "").replace("\"", "").replace("\n", " ").replace(",", "").split(" ")
for element in list:
    if element in list_count.keys():
        list_count[element]+= 1
    else:
        list_count[element]=1
sorted_list_count=sorted(list_count.items(), key=operator.itemgetter(1))
final=sorted_list_count[::-1]
for word in final:
    print (f'{word[0]} : {word[1]}')
#end
