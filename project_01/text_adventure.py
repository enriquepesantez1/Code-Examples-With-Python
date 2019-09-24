# Title of the game Function
def title():
  print("Crazy Nights\u00A9")
  print("You are the sheriff in the town of Alstead: a small town where") 
  print("everyone knows each other. You are sent to investigate the ")
  print("murder of your next door neighbor, Victoria Tim, age 34.")
  print("You only have one night to solve this case. Good luck Sheriff", player_name,"!")


# Ending of the Game Function
def ending():
  print("With my evidence in hand, I went back to the station and arrested Mike. He testified that he didn't mean to kill her, only intimidate her as she had been cheating on him. Even if that were the case, murder is a terrible crime and Mike deserves to be punished. The End")
  print("Created by Enrique Pesantez & Gabriel Schaerf\u00A9")
  print("Email: enrique.pesantez1 or gabriel.schaerf1")


# Name of the Player
player_name = input("What is your name:", )
# Location of the player
player_location = ['Crime Scene', 'Police Station', 'Police Car', 'Mikes House', 'Mikes Basement' ]
# Story of what is happening at each location
story = ['The crime scene is on the corner of 5th and 6th street. You see the corpse of Victoria laid out on the ground, along with a chalk out surrounding her. There is a stab wound in her back. Her case file stated that a knife was stabbed into her back, just barely missing her heart. She died of blood loss. The knife is no where to be seen. Everyone who had been at the crime scene at the time of the murder was taken to the police station.','At the station, there are three suspects who could have possibly committed the murder: Alexander Danes, son of the mayor, Mike Macdonnely, Victorias boyfriend, and Claire Stanford, the local librarian. They each gave their testimonies. I was going to need a bit more evidence to figure out who the murder was.','In my police car, I needed to decide whose house I should investigate.','After arriving at Mikes house, I opened the door. The guy is a bit of a slob. Theres dirty laundry thrown everywhere and theres a large stain on the wall behind the tv, as if he mounted the tv just to hide the stain. The house was a ranch style, so it was only one floor. I noticed five rooms: a bedroom, a bathroom, a kitchen, a living room, and a basement which appeared to be locked. There was also a front yard with a lot of bushes.', 'After finding the key to the basement, I made my way down the stairs. The floor was made of rotting wood. There was a pool table and a fridge filled with beer. Strapped to the underside of the pool table was a knife stained red with blood.']
# Declaring the Score of the Player
score = 0
# running the game
title()


for i in range(5):
    print(player_location[i])
    print(story[i])
    score = score + 5
    print("Your score: ", score)
    input('Press Enter To Continue:', )


ending()
