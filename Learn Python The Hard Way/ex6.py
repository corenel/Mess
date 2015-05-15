x = "There are %d kinds of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I've said: %r." % x
print "I've also said: %r." % y

answer = False
joke_evaluation = "Isn't this joke fun? %r"

print joke_evaluation % answer

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
