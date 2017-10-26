actual_user_feedback = [ -100, 4, 90, 32, -10, -3, 0, 17, 67 ]
print('We’re very proud having only positive feedback:')
for score in actual_user_feedback:
    if score > 50:
        print(score)
