#module = a file containing python code. May contain functions, classes, etc
# used with modular prograaming, which is to seperate a program into parts

import message as msg #as msg lets us short hand it to msg instead of message. Wont be able to use message. though
from message import hello, bye #makes it so that we no longer need a module name. Can use import* = imports all functions. Not recommended due to naming conflicts

msg.hello()
msg.bye()
bye()
hello()

help("modules") #gives us a list of the modules we have access to