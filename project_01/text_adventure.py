def title():
  print("Crazy Nights\u00A9")
  print('You live in a small town where every knows each other. However, the old Hag who you live next to was murdered!! It is your job as the towns sheriff to figure out who killed her.')
def ending():
  print("The End")
  print("Created by Enrique Pesantez")
  print("Email: enrique.pesantez1")
player_name = input("What is your name:", )
player_location = ['Crime Scene', 'Police Station', 'Police Car', 'Mikes House', 'Mikes Basement' ]
story = ['1','2','3','4','5']
score = 0
#running the game
title()
for i in range(5):
    print(player_location[i])
    print(story[i])
    score = score + 5
    print("Your score: ", score)
    input('Press Enter To Continue:', )
ending()