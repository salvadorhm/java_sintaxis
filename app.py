from rule_00 import OpenClose
from rule_01 import ReservedWords

file = open('bye.java','r')

text = file.readlines()
file.close()

openClose = OpenClose()
openClose.validate(text)

reserved = ReservedWords()
reserved.validate(text)
