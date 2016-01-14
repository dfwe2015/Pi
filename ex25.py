# # # # # # # # # # """Did needs test help words? """
# # # # # # # # # #
# # # # # # # # # # # # # # # # # # # from sys import argv
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # script, user_name, likes = argv
# # # # # # # # # # # # # # # # # # # prompt = '> '
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print "Hi %s, I'm the %s script." % (user_name, script)
# # # # # # # # # # # # # # # # # # # print "I'd like to ask you a few questions."
# # # # # # # # # # # # # # # # # # # # print "Do you like me %s?" % user_name
# # # # # # # # # # # # # # # # # # # # likes = raw_input(prompt)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print "Where do you live %s?" % user_name
# # # # # # # # # # # # # # # # # # # lives = raw_input(prompt)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print "What kind of computer do you have?"
# # # # # # # # # # # # # # # # # # # computer = raw_input(prompt)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print """
# # # # # # # # # # # # # # # # # # # Alright, so you said %s about liking me.
# # # # # # # # # # # # # # # # # # # You live in %s. Not sure where that is.
# # # # # # # # # # # # # # # # # # # And you have a %s computer. Nice.
# # # # # # # # # # # # # # # # # # # """ % (likes, lives, computer)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # from sys import argv
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # script, filename = argv
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # txt = open(filename)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # print "Here is your file %r" % filename
# # # # # # # # # # # # # # # # # # print txt.read()
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # print "Type the filename again:"
# # # # # # # # # # # # # # # # # # file_again = raw_input('>')
# # # # # # # # # # # # # # # # # # txt_again = open(file_again)
# # # # # # # # # # # # # # # # # # print(txt_again.read())
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # txt.close()
# # # # # # # # # # # # # # # # # # txt_again.close()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # from sys import argv
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # script, filename = argv
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print "We're going to erase %r." % filename
# # # # # # # # # # # # # # # # # print("If you don't want that, hit CTRL-C (^c).")
# # # # # # # # # # # # # # # # # print("If you do want that, hit RETURN.")
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # raw_input("?")
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print("Opening the file...")
# # # # # # # # # # # # # # # # # target = open(filename, 'w')
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print("Truncating the file. Goodbye!")
# # # # # # # # # # # # # # # # # target.truncate()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print "Now I'm going to ask you for three lines."
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # line1 = raw_input("line 1:")
# # # # # # # # # # # # # # # # # line2 = raw_input("line 2:")
# # # # # # # # # # # # # # # # # line3 = raw_input("line 3:")
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print "I'm going to write these to the file."
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # target.write(line1)
# # # # # # # # # # # # # # # # # target.write("\n")
# # # # # # # # # # # # # # # # # target.write(line2)
# # # # # # # # # # # # # # # # # target.write("\n")
# # # # # # # # # # # # # # # # # target.write(line3)
# # # # # # # # # # # # # # # # # target.write("\n")
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print("And finally, we close it.")
# # # # # # # # # # # # # # # # # target.close()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # from sys import argv
# # # # # # # # # # # # # # # # from os.path import exists
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # scripts, from_file, to_file = argv
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print("Copying from %s to %s" % (from_file, to_file))
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # in_file = open(from_file)
# # # # # # # # # # # # # # # # indata = in_file.read()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print "The input file is %d bytes long" % len(indata)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print "Does the output file exist? %r" % exists(to_file)
# # # # # # # # # # # # # # # # print("Ready, hit RETURN to continue, CTRL-C to abort")
# # # # # # # # # # # # # # # # raw_input()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(indata)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # out_file = open(to_file, 'w')
# # # # # # # # # # # # # # # # out_file.write(indata)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print("Alright, all done.")
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # out_file.close()
# # # # # # # # # # # # # # # # in_file.close()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # def print_two(*args):
# # # # # # # # # # # # # # #     arg1, arg2 = args
# # # # # # # # # # # # # # #     print("arg1: %r, arg2: %r" % (arg1, arg2))
# # # # # # # # # # # # # # # def print_two_again(arg1, arg2):
# # # # # # # # # # # # # # #     print("arg1: %r, arg2:  %r" % (arg1, arg2))
# # # # # # # # # # # # # # # def print_one(arg1):
# # # # # # # # # # # # # # #     print("arg1: %r" % arg1)
# # # # # # # # # # # # # # # def print_none():
# # # # # # # # # # # # # # #     print("I got nothin'.")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print_two("Zed","Shaw")
# # # # # # # # # # # # # # # print_two_again("Zed","Show")
# # # # # # # # # # # # # # # print_one("First!")
# # # # # # # # # # # # # # # print_none()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # def cheese_and_crackers(cheese_count, boxes_of_crackers):
# # # # # # # # # # # # # #     print("You have %d cheeses!" % cheese_count)
# # # # # # # # # # # # # #     print("You have %d boxes of crackers!" % boxes_of_crackers)
# # # # # # # # # # # # # #     print("Man that's enough for a party!")
# # # # # # # # # # # # # #     print("Get a blanket.\n")
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print("We can just give the function numbers directly:")
# # # # # # # # # # # # # # cheese_and_crackers(20,30)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print("OR, we can use varibales form out script:")
# # # # # # # # # # # # # # amount_of_cheese = 10
# # # # # # # # # # # # # # amount_of_crackers = 50
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # cheese_and_crackers(amount_of_cheese,amount_of_crackers)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print("We can even do math inside too!")
# # # # # # # # # # # # # # cheese_and_crackers(10 + 20, 5 + 6)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print("And we can combine the two, variables and math:")
# # # # # # # # # # # # # # cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# # # # # # # # # # # # #
# # # # # # # # # # # # # from sys import argv
# # # # # # # # # # # # #
# # # # # # # # # # # # # script, input_file = argv
# # # # # # # # # # # # #
# # # # # # # # # # # # # def print_all(f):
# # # # # # # # # # # # #     print(f.read())
# # # # # # # # # # # # #
# # # # # # # # # # # # # def rewind(f):
# # # # # # # # # # # # #     f.seek(0)
# # # # # # # # # # # # #
# # # # # # # # # # # # # def print_a_line(line_count, f):
# # # # # # # # # # # # #     print(line_count, f.readline())
# # # # # # # # # # # # #
# # # # # # # # # # # # # current_file = open(input_file)
# # # # # # # # # # # # #
# # # # # # # # # # # # # print("First let's print the whole file:\n")
# # # # # # # # # # # # #
# # # # # # # # # # # # # print_all(current_file)
# # # # # # # # # # # # #
# # # # # # # # # # # # # print("Now let's rewind, kind of like a tape.")
# # # # # # # # # # # # #
# # # # # # # # # # # # # rewind(current_file)
# # # # # # # # # # # # #
# # # # # # # # # # # # # print("Let's print three lines:")
# # # # # # # # # # # # #
# # # # # # # # # # # # # current_line = 1
# # # # # # # # # # # # # print_a_line(current_line, current_file)
# # # # # # # # # # # # #
# # # # # # # # # # # # # current_line += 1
# # # # # # # # # # # # # print_a_line(current_line, current_file)
# # # # # # # # # # # # #
# # # # # # # # # # # # # current_line += 1
# # # # # # # # # # # # # print_a_line(current_line, current_file)
# # # # # # # # # # # # #
# # # # # # # # # # # # def add(a, b):
# # # # # # # # # # # #     print("ADDING %d + %d" % (a, b))
# # # # # # # # # # # #     return a + b
# # # # # # # # # # # # def subtract(a, b):
# # # # # # # # # # # #     print("SUBTRACTING %d - %d" % (a, b))
# # # # # # # # # # # #     return a - b
# # # # # # # # # # # # def multiply(a, b):
# # # # # # # # # # # #     print("MULTIPLYING %d * %d" % (a, b))
# # # # # # # # # # # #     return a * b
# # # # # # # # # # # # def divide(a, b):
# # # # # # # # # # # #     print("DIVING %d / %d" % (a, b))
# # # # # # # # # # # #     return a / b
# # # # # # # # # # # #
# # # # # # # # # # # # print("Let's do some math with just functions!")
# # # # # # # # # # # #
# # # # # # # # # # # # age = add(30, 5)
# # # # # # # # # # # # height = subtract(78, 4)
# # # # # # # # # # # # weight = multiply(90, 2)
# # # # # # # # # # # # iq = divide(100, 2)
# # # # # # # # # # # #
# # # # # # # # # # # # print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
# # # # # # # # # # # #
# # # # # # # # # # # # print("Here is a puzzle.")
# # # # # # # # # # # #
# # # # # # # # # # # # what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# # # # # # # # # # # #
# # # # # # # # # # # # print("That becomes: ", what, "Can you do it by hand?")
# # # # # # # # # # #
# # # # # # # # # # # print("Let's practice everthing.")
# # # # # # # # # # # print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# # # # # # # # # # #
# # # # # # # # # # # poem = """
# # # # # # # # # # # \t The lovely world
# # # # # # # # # # # with logic so firmly planted
# # # # # # # # # # # cannot discern \n the needs of love
# # # # # # # # # # # nor comprehend passion from intuition
# # # # # # # # # # # and requires an explanation
# # # # # # # # # # # \n\t\twhere there is none.
# # # # # # # # # # # """
# # # # # # # # # # #
# # # # # # # # # # # print("--------------------")
# # # # # # # # # # # print(poem)
# # # # # # # # # # # print("--------------------")
# # # # # # # # # # #
# # # # # # # # # # # five = 10 - 2 + 3 - 6
# # # # # # # # # # # print("This should be five: %s" % five)
# # # # # # # # # # #
# # # # # # # # # # # def secret_formula(started):
# # # # # # # # # # #     jelly_beans = started * 500
# # # # # # # # # # #     jars = jelly_beans / 1000
# # # # # # # # # # #     crates = jars / 100
# # # # # # # # # # #     return jelly_beans, jars, crates
# # # # # # # # # # #
# # # # # # # # # # # start_point = 10000
# # # # # # # # # # # beans, jars, crates = secret_formula(start_point)
# # # # # # # # # # # print("With a starting point of: %d" % start_point)
# # # # # # # # # # # print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
# # # # # # # # # # #
# # # # # # # # # # # start_point = start_point / 10
# # # # # # # # # # #
# # # # # # # # # # # print("We can also do that this way:")
# # # # # # # # # # # print("We'd have %d beans, %d jars, and %d crates.") % secret_formula(start_point)
# # # # # # # # # # def break_words(stuff):
# # # # # # # # # #     """This function will break up words for us."""
# # # # # # # # # #     words = stuff.split(' ')
# # # # # # # # # #     return words
# # # # # # # # # # def sort_words(words):
# # # # # # # # # #     """Sorts the words."""
# # # # # # # # # #     return sorted(words)
# # # # # # # # # # def print_first_word(words):
# # # # # # # # # #     word = words.pop(0)
# # # # # # # # # #     print(word)
# # # # # # # # # # def print_last_word(words):
# # # # # # # # # #     word = words.pop(-1)
# # # # # # # # # #     print(word)
# # # # # # # # # # def sort_sentence(sentence):
# # # # # # # # # #     words = break_words(sentence)
# # # # # # # # # #     return sort_words(words)
# # # # # # # # # # def print_first_and_last(sentence):
# # # # # # # # # #     words = break_words(sentence)
# # # # # # # # # #     print_first_word(words)
# # # # # # # # # #     print_last_word(words)
# # # # # # # # # # def print_first_and_last_sorted(sentence):
# # # # # # # # # #     words = sort_sentence(sentence)
# # # # # # # # # #     print_first_word(words)
# # # # # # # # # #     print_last_word(words)
# # # # # # # # #
# # # # # # # # # # print 3 ==3 and not ("testing" == "testing" or "Python" == "Fun")
# # # # # # # # #
# # # # # # # # # people = 20
# # # # # # # # # cats = 30
# # # # # # # # # dogs = 15
# # # # # # # # #
# # # # # # # # # if people < cats:
# # # # # # # # #     print("Too many cats! The world is doomed!")
# # # # # # # # # if people > cats:
# # # # # # # # #     print("Not may cats! The world is saved!")
# # # # # # # # # if people < dogs:
# # # # # # # # #     print("The world is drooled on!")
# # # # # # # # # if people > dogs:
# # # # # # # # #     print("The world is dry!")
# # # # # # # # #
# # # # # # # # # dogs += 5
# # # # # # # # # print(people)
# # # # # # # # # print(dogs)
# # # # # # # # # if people >= dogs:
# # # # # # # # #     print("People are greater than or equal to dogs.")
# # # # # # # # # if people <= dogs:
# # # # # # # # #     print("People are less than or euqal to dogs.")
# # # # # # # # #
# # # # # # # # # if people == dogs:
# # # # # # # # #     print("People are dogs.")
# # # # # # # #
# # # # # # # # print("You enter a drak room with two doors. Do you go through door #1 or door #2?")
# # # # # # # #
# # # # # # # #
# # # # # # # # door = raw_input("> ")
# # # # # # # #
# # # # # # # # if door == "1":
# # # # # # # #     print("There's a giant biar bere eating a cheese cake. What do you do?")
# # # # # # # #     print("1. Take the cake.")
# # # # # # # #     print("2. Scream at the bear.")
# # # # # # # #
# # # # # # # #     bear = raw_input("> ")
# # # # # # # #
# # # # # # # #     if bear == "1":
# # # # # # # #         print("The bear eats your face off. Good job!")
# # # # # # # #     elif bear == "2":
# # # # # # # #         print("The bear eats your legs off. Good job!")
# # # # # # # #     else:
# # # # # # # #         print("Well, doing %s is probably better. Bear runs away." % bear)
# # # # # # # # elif door == "2":
# # # # # # # #     print("You stare into the endless abyss at Cthulhu's retina.")
# # # # # # # #     print("1. Blueberries.")
# # # # # # # #     print("2. Yellow jacket clothespins.")
# # # # # # # #     print("3. Understanding revolvers yelling melodies.")
# # # # # # # #
# # # # # # # #     insanity = raw_input("> ")
# # # # # # #
# # # # # # # #
# # # # # # # #     if insanity == "1" or insanity == "2":
# # # # # # # #         print("Your body survies powered by a mind or jello. Good job!")
# # # # # # # #     else:
# # # # # # # #         print("The insanity rots your eyes into a pool of muck. Good job!")
# # # # # # # #
# # # # # # # # else:
# # # # # # # #     print("You stumble around and fall on a knife and die. good job!")
# # # # # # #
# # # # # # # the_count = [1, 2, 3, 4, 5]
# # # # # # # fruits = ['apples', 'oranges', 'pears', 'apricots']
# # # # # # # change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# # # # # # #
# # # # # # # for number in the_count:
# # # # # # #     print("This is count %d" % number)
# # # # # # #
# # # # # # # for fruit in fruits:
# # # # # # #     print("A fruit of type: %s" % fruit)
# # # # # # #
# # # # # # # for i in change:
# # # # # # #     print("I got %r" % i)
# # # # # # #
# # # # # # # elements = []
# # # # # # #
# # # # # # # # for i in range(0,6):
# # # # # # # #     print("Adding %d to the list.") % i
# # # # # # # #     elements.append(i)
# # # # # # # # elements.append(range(0, 6))
# # # # # # # # elements = elements[0]
# # # # # # # elements = range(0, 6)
# # # # # # # print(elements)
# # # # # # # for i in elements:
# # # # # # #     print("Element was: %r" % i)
# # # # # # def num(j, k):
# # # # # #     # i = 0
# # # # # #     numbers = []
# # # # # #
# # # # # #     # while i < j:
# # # # # #     #     print("At the top i is %d" % i)
# # # # # #     #     numbers.append(i)
# # # # # #     #
# # # # # #     #     i = i + k
# # # # # #     #     print("Numbers now: ", numbers)
# # # # # #     #     print("At the bottom i is %d" % i)
# # # # # #
# # # # # #     for i in range(0,j,k):
# # # # # #         print("At the top i is %d" % i)
# # # # # #         numbers.append(i)
# # # # # #
# # # # # #         i = i + k
# # # # # #         print("Numbers now: ", numbers)
# # # # # #         print("At the bottom i is %d" % i)
# # # # # # num(6,2)
# # # # #
# # # # # from sys import exit
# # # # #
# # # # # def dead(why):
# # # # #     print(why,"Good job!")
# # # # #     exit(0)
# # # # #
# # # # # def gold_room():
# # # # #     print("This room is full of gold. How much do you take?")
# # # # #
# # # # #     next = raw_input("> ")
# # # # #     if "0" in next or "1" in next:
# # # # #         how_much = int(next)
# # # # #     else:
# # # # #         dead("Man, learn to type a number.")
# # # # #
# # # # #     if how_much < 50:
# # # # #         print("Nice, you're not greedy, you win!")
# # # # #         exit(0)
# # # # #     else:
# # # # #         dead("You greedy bastard!")
# # # # #
# # # # # def bear_room():
# # # # #             print("There is a bear here.")
# # # # #             print("The bear has a bunch of honey.")
# # # # #             print("The fat bear is in front of another door.")
# # # # #             print("How are you going to move the bear?")
# # # # #             bear_moved = False
# # # # #
# # # # #             while True:
# # # # #                 next = raw_input("> ")
# # # # #
# # # # #                 if next == "take honey":
# # # # #                     dead("The bear looks at you then slaps your face off.")
# # # # #                 elif next == "taunt bear" and not bear_moved:
# # # # #                     print("The bear has moved from the door. You can go through it now.")
# # # # #                     bear_moved = True
# # # # #                 elif next == "taunt bear" and bear_moved:
# # # # #                     dead("The bear gets pissed off and chews your leg off.")
# # # # #                 elif next == "open door" and bear_moved:
# # # # #                     gold_room()
# # # # #                 else:
# # # # #                     print("I got no idea what that means.")
# # # # #
# # # # # def cthulhu_room():
# # # # #     print("Here you see the great evil Cthulhu.")
# # # # #     print("He, it, whatever stares at you and you go insane.")
# # # # #     print("Do you flee for your life or eat your head.")
# # # # #
# # # # #     next = raw_input("> ")
# # # # #
# # # # #     if "flee" in next:
# # # # #         start()
# # # # #     elif "head" in next:
# # # # #         dead("Well that was tasty!")
# # # # #     else:
# # # # #         cthulhu_room()
# # # # #
# # # # # def start():
# # # # #     print("You are in dark room.")
# # # # #     print("There is a door to your right and left.")
# # # # #     print("Which one do you take?")
# # # # #
# # # # #     next = raw_input("> ")
# # # # #
# # # # #     if next == "left":
# # # # #         bear_room()
# # # # #     elif next == "right":
# # # # #         cthulhu_room()
# # # # #     else:
# # # # #         dead("You stumble around the room until you starve.")
# # # # #
# # # # # # start()
# # # # # gold_room()
# # # #
# # # # ten_thins = "Apples Oranges Crows Telephone Light Sugar"
# # # #
# # # # print("Wait there's not 10 things in that list, let's fix that.")
# # # #
# # # # stuff = ten_thins.split(' ')
# # # # more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# # # #
# # # # while len(stuff) != 10:
# # # #     next_one = more_stuff.pop()
# # # #     print("Adding: ", next_one)
# # # #     stuff.append(next_one)
# # # #     print("There's %d items now." % len(stuff))
# # # #
# # # # print("There we go:", stuff)
# # # #
# # # # print("Let's do some things with stuff.")
# # # #
# # # # print(stuff[1])
# # # # print(stuff[-1])
# # # # print(stuff.pop())
# # # # print(' '.join(stuff))
# # # # # print('#'.join([stuff[3],stuff[4]]))
# # # # print('#'.join(stuff[3:5]))
# # #
# # # states = {
# # #     'Oregon': 'OR',
# # #     'Florida': 'FL',
# # #     'Califormia': 'CA',
# # #     'New York': 'NY',
# # #     'Michigan': 'MI'
# # # }
# # #
# # # cities = {
# # #     'CA': 'San Francisco',
# # #     'MI': 'Detroit',
# # #     'FL': 'Jacksonville'
# # # }
# # #
# # # cities['NY'] = 'New York'
# # # cities['OR'] = 'Portland'
# # #
# # # print('-' * 10)
# # # print("NY State has: ", cities['NY'])
# # # print("OR State has: ", cities['OR'])
# # #
# # # print('-' * 10)
# # # print("Michigan's abbreviation is: ", states['Michigan'])
# # # print("Florida's abbreviation is:", states['Florida'])
# # #
# # # print('-' * 10 )
# # # print("Michigan has: ", cities[states['Michigan']])
# # # print("Florida has: ", cities[states['Florida']])
# # #
# # # print('-' * 10 )
# # # # print(states.items())
# # # for state, abbrev in states.items():
# # #     print("%s is abbreviated %s " % (state, abbrev))
# # #
# # # print('-' * 10)
# # # for abbrev, city in cities.items():
# # #     print("%s has the city %s" % (abbrev, city))
# # #
# # # print('-' * 10)
# # # for state, abbrev, in states.items():
# # #     print("%s state is abbreviated %s and has city %s" % (
# # #         state, abbrev, cities[abbrev]
# # #     ))
# # #
# # # print('-' * 10)
# # # state = states.get('Text', None)
# # #
# # # if not  state:
# # #     print("Sorry, no Texts.")
# # #
# # # city = cities.get('TX', 'Does Not Exist')
# # # print("The city for the state 'TX' is : %s" % city)
# # #
# # # city = cities.get('CA')
# # # print(city)
# # #
# # # for x in states:
# # #     print(x),
# # #     print('\t'),
# # #     print(states[x])
# #
# # # import mystuff as stuff
# # #
# # # stuff.apple()
# # # print(stuff.tangerine)
# #
# # # class MyStuff(object):
# # #
# # #     def __init__(self):
# # #         self.tangerine = "And now a thousand years between"
# # #     def apple(self):
# # #         print("I AM CLASSY APPLES!")
# # #
# # # stuff = MyStuff()
# # # stuff.apple()
# # # print(stuff.tangerine)
# #
# # class Song(object):
# #
# #     def __init__(self, lyrics):
# #         self.lyrics = lyrics
# #     def sing_me_a_song(self):
# #         for line in self.lyrics:
# #             print(line)
# #
# # happy_bday = Song(["Happy birthday to you",
# #                    "I don't want to get sued",
# #                    "So I'll stop right there"])
# #
# # bulls_on_prade = Song(["They rally around the family",
# #                        "With pockets full of shells"])
# #
# # happy_bday.sing_me_a_song()
# # bulls_on_prade.sing_me_a_song()
# #
# import random
# from urllib import urlopen
# import sys
#
# WORD_URL = "http://learncodethehardway.org/word.txt"
# WORDS = []
#
# PHRASES = {
#     "class %%%(%%%):":
#         "Make a class named %%% that is-a %%%.",
#     "class %%%(object):\n\tdef __init__(self, ***)":
#         "class %%% has-a __init__ that takes self and *** paramenters.",
#     "class %%%(object):\n\tdef ***(self, @@@)":
#         "class %%% has-a function named *** that takes self and @@@ paramenters.",
#     "*** = %%%()":
#         "Set *** to an instance of class %%%.",
#     "***.***(@@@)":
#         "From *** get the *** function, and call it with paramenters self, @@@.",
#     "***.*** = '***'":
#         "From *** get the *** attribute and set it to '***'."
# }
#
# PHRASE_FIRST = False
# if len(sys.argv) == 2 and sys.argv[1] == "english":
#     PHRASE_FIRST = True
#
# for word in urlopen(WORD_URL).readlines():
#     WORDS.append(word.strip())
#
# def convert(snippet, phrase):
#     class_names = [w.capitalize() for w in
#                   random.sample(WORDS, snippet.count("%%%"))]
#     other_names = random.sample(WORDS, snippet.count("***"))
#     results = []
#     param_names = []
#
#     for i in range(0, snippet.count("@@@")):
#         param_count = random.randint(1, 3)
#         param_names.append(', '.join(random.sample(WORDS, param_count)))
#
#     for sentence in snippet, phrase:
#         results = sentence[:]
#
#         for word in class_names:
#             result = result.replace("%%%", word, 1)
#
#             for word in other_names:
#                 result = result.replace("***", word, 1)
#
#             for word in param_names:
#                 result = result.replace("@@@", word, 1)
#
#             results.append(result)
#
#         return results
#
#     try:
#         while True:
#             snippets = PHRASES.keys()
#             random.shuffle(snippets)
#
#             for snippet in snippets:
#                 phrase = PHRASES[snippet]
#                 question, answer = convert(snippet, phrase)
#                 if PHRASE_FIRST:
#                     question, answer = answer, question
#
#                 print(question)
#
#                 raw_input("> ")
#                 print("ANSWER: %s\n\n" % answer)
#
#     except EOFError:
#         print("\nBye")
#
# convert()

# import oop

