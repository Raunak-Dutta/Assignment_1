"""
Name: Raunak Dutta
JCU_ID: 13662643
Date: Dec 6, 2018
Psudo-Code:

main():
load song;
print list of menu
call menu options
repeat menu
write changes to file
close file

menu options():
 if L
    open list():
 else if A
    open Append():
 else if C
    open Complete():
 else
    tell main to quit

    L():
    list the songs

    A:
    add song title
    add song year
    add song artist
    add new entry

    C:
    list the songs L()
    complete a song
"""
import csv

song_list_file = open("songs.csv", mode='r+')
song_list = []
for e in song_list_file:
    if e != "":
        song_list.append(e)


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
            song_list_file.truncate()  # truncate the file that is empty it for the new list to be written
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
        print_table("all")
    elif ch == "A":
        add_song()
    elif ch == "C":
        learn_song()
    elif ch == "Q":
        print("Have a nice day :)")
        continue_loop = False
    else:
        print("Invalid input")
    return continue_loop


def add_song():
    song_title = str(input("Please enter the title of the song"))
    song_artist = str(input("Please enter the artist of the song"))
    song_year = str(input("Please enter the year of the song's release"))
    file_format = song_title + "," + song_artist + "," + song_year + "," + "y" + "\n"
    song_list.append(file_format)


def print_table(which_print):
    count = 0
    print("%-5s %-35s %-35s %-35s %s" % ("No.", "Title", "Artist", "Year", "Songs Learned"))
    print(
        "================================================================"
        "===============================================================")
    for line in song_list:
        count += 1
        str_part_indicator = 1
        song_title_learned = ""
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
                song_title_learned = song_title_learned + words
                if "y" in song_title_learned:
                    song_title_learned1 = "✕"
                else:
                    song_title_learned1 = "✓"
        if which_print == "all":
            print("%-5s %-35s %-35s %-35s %s" % (count, song_title, song_artist, song_year, song_title_learned1))
        elif which_print == "inc" and song_title_learned1 == "✕":
            print("%-5s %-35s %-35s %-35s %s" % (count, song_title, song_artist, song_year, song_title_learned1))


def learn_song():
    print("Which song would you like to learn?")
    count = 0
    for song in song_list:
        if song[(len(song) - 2)] == "y":
            count = count + 1
    if count == 0:
        print("No more songs to learn, please add some new ones.")
    else:
        print_table("inc")
        num_learn = int(input())
        num_learn = num_learn - 1
        song_list[num_learn] = (song_list[num_learn])[:-2] + "n\n"


if __name__ == '__main__':
    main()
