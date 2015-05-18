tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backplash_cat = "I'm \\ a \\ cat."

fat_cat = """
That's my todo list:
\t* Learn python
\t* Play Kancolle
\t* Do homework
"""

print tabby_cat
print persian_cat
print backplash_cat
print fat_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
