# Bingo?
def custom_song(name, pet, animal, sound, activity, place, adjective1, adjective2):

    #This will separate your chosen name with hyphens 
    spelled_name = "-".join(name.upper())

    song = (
        f"There was a {adjective1} farmer who had a {animal},\n"
        f"And {name} was its name-o.\n\n"
        
        f"{name} loves to {activity} all day long,\n"
        f"In a {adjective2} place called {place}.\n\n"
        
        f"Oh! {name}, the {adjective1} {animal} makes a {sound} sound,\n"
        f"And everyone in {place} gathered around!\n\n"
        
        f"{name} was such a {pet} with fun to show,\n"
        f"And all the kids shouted 'Let's go!'\n\n"
        
        f"{spelled_name}, {spelled_name},\n"
        f"And {name} was its name-o!"
        )
    
    print(song)


# Enter your words in the " " below

name = (" ")
pet = (" ")
animal = (" ")
sound = (" ")
activity = (" ")
place = (" ")
adjective1 = (" ")
adjective2 = (" ")

# custom song time
custom_song(name=name, pet=pet, animal=animal, sound=sound, activity=activity, place=place, adjective1=adjective1, adjective2=adjective2)
