# with open(r'calorie.csv','r',encoding='utf-8') as calorie:
#     with open(r'caloriecount.csv','a',encoding='utf-8') as greeting_file:
#         for i in calorie:
#             i = i.split(' ')
#             i = i.pop(1)
#             calorie = int(i.pop(1))
#             for x in calorie:
#                 x = x.split(' ')
#                 x = x.pop(0)
#                 count = x.pop(0)
#                 if (calorie >= 500):
#                     caloriecount.write(f"{count}")
# s_list = []
# with open('your_file.txt', 'r') as f:
#     s_list = list(file)
# calorie = []
# count = []
# for i in calories:
#    calorie.append(i.split(' '))
# for x in range(len(calorie)):
#    if (int(calorie[x].pop(1))>=500):
#        count.append(str(calorie[x].pop(0)))
# count = sorted(count)
# for x in range(len(count)):
#    print(count[x], end="\n")
open('your_file.txt', 'w').write(''.join(sorted(open('infile.txt', 'r'))))
