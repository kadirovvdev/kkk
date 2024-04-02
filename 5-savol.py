with open("name.txt", "r") as file, open("age.txt", "r") as age, open("info_user.txt", "w") as info_user, open("sort_info.txt", "w") as sort_info:

    for i in file:
        age_i = age.readline()
        info_user.write(f"{i.strip()} - {age_i}")




