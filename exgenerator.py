
train = input("Welcome to the random JAZZ exercise generator.\nWhat would you like to practice; arpeggios or scales? ")
level = input("Easy, medium or hard? ").lower()

print(" ")


import random


key_c = ['C','D','E','F','G','A','B','C#','Db','Eb','F#','G#','Ab','Bb']  
modes = ['Ionian','Dorian','Phrygian','Lydian','Mixolydian','Aeolian','Locrian']

triads = [' Triad', '- Triad', 'dim Triad', 'Aug Triad'] 
seventh = ['7 Arpeggio', '-7 Arpeggio', 'maj7 Arpeggio', '-maj7 Arpeggio', '-7b5 Arpeggio', ]


inversions = ['1st inv.', '2nd inv.', '3rd inv.',]
direction = ['ascending','descending']
interval = ['in 3rds', 'in 4ths','in 5ths','in 6ths', 'in 7ths']


#def structure (key, structure, level):



should_repeat = True  

while should_repeat:
    
    a = random.randint(0, len(key_c)-1) 
    b = random.randint(0, len(modes)-1)
    c = random.randint(0, len(triads)-1)
    d = random.randint(0, len(seventh)-1)
    e = random.randint(0, len(inversions)-1)
    f = random.randint(0, len(direction)-1)
    g = random.randint(0, len(interval)-1)
    key_center = key_c [a]
    
    if train == "scales" and level == "easy":
        print(key_center, modes[b])

    if train == "scales" and level == "medium":
        print(key_center, modes[b], direction[f])

    if train == "scales" and level == "hard":
        print(key_center, modes[b], direction[f], interval[g])

    if train == "arpeggios" and level == "easy":
        print(key_center, triads[c], direction[f])

    if train == "arpeggios" and level == "medium":
        print(key_center, seventh[d], direction[f])

    if train == "arpeggios" and level == "hard":
        print(key_center, seventh[d], direction[f], inversions[e])

    
    
    answer = input("\nPress ENTER to generate new. Otherwise type 'no'\n")
    if answer == "no":
        should_repeat = False
        print("Thank you for practicing, fluency is very important!\nGoodbye :)-")



