import os

with open("bookmark", 'r+') as bookmark:
    with open("data_01", "r") as input:
        with open("output", "r+") as output:
            # User ID of last guy
            # data = input.read(end_index - input)
            pivot = int(bookmark.read())
            input.seek(0+pivot)
            firstline = input.readline()
            print(firstline)
            bookmark.
            bookmark.write(str(pivot+int(len(firstline))))

        #_userid, _firstlink = firstline[0], firstline[1]
