"""
WARNING: NEVER TERMINATE THE CODE, DOING THAT WILL RESULT IN THE CSV FILE BEING DELETED.
"""
import csv

song_list_file = open("songs.csv", mode='r+')
song_list = []
for e in song_list_file:
    if e != "":
        song_list.append(e)

song_list_file.truncate(0)


def main():
    print("Songs To Learn 1.16 - by Raunak Dutta")

    song_counter = 0
    for _ in song_list:
        song_counter += 1

    print(str(song_counter) + " Songs loaded")
    continue_loop = True
    while continue_loop:
        continue_loop = execute_choice()

        if not continue_loop:
            print("Saving File...")
            song_list_file.seek(0)
            song_list_file.truncate()  # turncate the file that is enpty it for the new list to be written
            for eliment in song_list:
                if eliment != " ":
                    song_list_file.writelines(eliment)

    song_list_file.close()


def execute_choice():
    print("Menu:\nL - List songs \nA - Add new song \nC - Complete a song \nQ - Quit ")
    ch_in = str(input())
    ch = ch_in.upper()
    continue_loop = True
    if ch == "L":
        print_table()
    elif ch == "A":
        song_title = str(input("Please enter the title of the song"))
        song_artist = str(input("Please enter the artist of the song"))
        song_year = str(input("Please enter the year of the song's release"))
        file_format = song_title + "," + song_artist + "," + song_year + "," + "y" + "\n"
        song_list.append(file_format)

    elif ch == "C":
        learn_song()
    elif ch == "Q":
        print("Have a nice day :)")
        continue_loop = False
    else:
        print("Invalid input")
    return continue_loop


def print_table():
    print("%-35s %-35s %-35s %s" % ("Title", "Artist", "Year", "Songs Not Learned"))
    print("=============================================================================================================================")
    for line in song_list:
        str_part_indicator = 1
        song_titlelearned = ""
        song_year = ""
        song_artist = ""
        song_title = ""
        for words in line:
            if words == ",":
                str_part_indicator += 1
            elif str_part_indicator == 1:
                song_title = song_title + words
            elif str_part_indicator == 2:
                song_artist = song_artist + words
            elif str_part_indicator == 3:
                song_year = song_year + words
            elif str_part_indicator == 4:
                song_titlelearned = song_titlelearned + words
                if "y" in song_titlelearned:
                    song_titlelearned1 = "✕"
                else:
                    song_titlelearned1 = "✓"
        print("%-35s %-35s %-35s %s" % (song_title, song_artist, song_year, song_titlelearned1))

def learn_song():
    print("Which song would you like to learn from 1-" + str(len(song_list) + 1)+"?")
    num_learn = int(input())
    num_learn = num_learn - 1
    song_list[num_learn]=(song_list[num_learn])[:-2] + "n\n"


if __name__ == '__main__':
    main()
