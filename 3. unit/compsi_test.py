The_playlist = []
Music_history = []

#while loop for continues running

while True:
    print("Welcome tho the music app")
    print("1. add song to the queue")
    print("2. Play the next song in the queue")
    print("3. What year is this hit from")
    print("4.Return to your previous song")
    print('5.quit')
    decision = input("What do you chose? ")
    # Start with asking the user what he wants do do 

    if decision == "1":
        name_song = input("what is the name of the song ")
        date_song = input("what is the date ")
        The_playlist.append((name_song,date_song))
    
        print(f"Your song:{name_song} has benen added to the queue")
        print(The_playlist)
    # asking about the name and date of the song seperatly and storing them into a list as two seperate strings
    #In the rest of the code i managed to think of a system that SHOULD work bu doesn't
    elif decision == "2":
        if not The_playlist:
            print("no song in queue")
        else:
            to_history = The_playlist.pop(0)
            Music_history.append(to_history)
    
            print(f"{Music_history[0]} now playing")

    #here i wanted to add songs from one playlist to the other, i have two variables per song so i had to pop twice
    # I know i should do them as one list value but i didn't think of it at the time
    elif decision == "3":
        if not Music_history:
            print("Nothing is playing")
        else:
            print(f"your hit is from the year {Music_history[-1][1]}")

    # Checking from what year the song is from, it is always the second value in a stack

    elif decision == "4":
        if not Music_history:
            print("Dummy nothing is playing")
        else :
            to_playlist = Music_history.pop(1)
            The_playlist.insert(0, to_playlist)
            
   # Used the sam logic as in the 2 point
    elif decision == "5":
        print("Thank you for using our services")
        break
    #break if somebody wants to quit

    else:
        print("invalid input")
    # Invalid inputs are not tolerated 

            
        


