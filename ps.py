def continue_to_main( strname ):
    user_reply = input("would you like to load project Android 3? (Type yes or no)")
    if user_reply == "yes":
       print("Loading...")
    elif user_reply == "no":
       print("Program ended")
    user_reply = input("Loaded...How are you today sir?")
    if user_reply == "great how are you?": 
        print()
        print("Good sir a little slow but otherwise things are working well...I am loading HOME MENU now.")
        print("Loading...")
        print()
        print("WELCOME TO THE HOME MENU")
        print()
    user_reply = input("Would you like to load story mode? (Type yes or no)") 
#    if user_reply == "yes":
       #print("Still working on Story mode")
  #  if user_reply == "no";
   
      #`print("Have a nice day")
    
    woman = ["A sientist", "A queen", "A pirate", "A canibale", "A giant pink rabbit"]
    man = ["A policek officer", "an artist", "Your great great grand father","a killer robot"]
    place = ["on Mars."," at the supermarket.", "in a sunken pirate ship."]
    sheWore = ["scuba diving gear.", "dragon wings.", " a paper bag."]
    heWore = ["a purple penguin suit", "a shark costume.", "a beach towl."]
    womanSays = ["'Who are you?'", "'How many beans make five?'","'Why?'","'Are you the king of France'"]
    manSays = ["'Beep boop!'", "'Don't eat frogs!'", "'What time do you call this?'","'Did you just fart?'"]
    onsequence = ["world destroyed.", "chaos.", "a giant squashed them.", "rainclouds."]
    worldSaid = ["'Utter nonsense!'", "'Cheese is trending now.'","'I'ma a farter'"]
    import random
    while True:
            
            print(random.choice(woman), "met", random.choice(man), random.choice(place))
            print("She was wearing", random.choice(sheWore))
            print("He was wearing", random.choice(heWore))
            print("She said,", random.choice(womanSays))
            print("He said,", random.choice(manSays))
            print("The consequence was", random.choice(consequence))
            print("The world said,", random.choice(worldSaid))
            print()
        user_reply = input("Press enter to play again. or no if you want to stop.")
            #print()
        if user_reply == "no":
            print ("Have a nice day.")
         
    
       # print("Yes sir you haven't entered any more code for my computer intelligence so...by.")

    return

password = "password"
while password != "Macgyverps":    
    password = input("Enter password.")
    guessnumber = input("Enter the correct number.")
    if password == "Macgyverps" and guessnumber == "2005":
         print("Correct!")
    else:
        print("Wrong! Try Again.")

name = "name"
name = input("PLEASE ENTER YOUR NAME.")
if name == "scott davis":
    print("WELCOME.")
    continue_to_main(name)
else:
    print("YOU ARE NOT PERMITTED TO ENTER YOU ARE NOW LOCKED OUT")

#Project Android one will act like a android, only it will be a bot that uses line after line of code to make it seem like it is a real android.
#"Android 1" will be devoleped into Android 1 through 10 like windows.

  
