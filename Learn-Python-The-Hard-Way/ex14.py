from sys import argv

script, username = argv
prompt = "> "

print "Hello, %s. I'm the %s script." % (username, script)
print "I'd like to ask some questions."
print "Do you like me, %s?" % (username)
likes = raw_input(prompt)

print "Where do you live, %s?" % (username)
lives = raw_input(prompt)

print "What kind of cellphone do you have?"
cellphone = raw_input(prompt)

print """
OK, now I know you said %s about liking me,
You live in %s, and you have a %s cellphone.
""" % (likes, lives, cellphone)
