import string

class OpenClose:

    def n__init__(self):
        pass

    def validate(self,file):
        open=('{','[','(')
        close=('}',']',')')

        signs=[]

        for line in file:
            for letter in line:
                if letter in open:
                    signs.append(letter)
                elif letter in close:
                    try:
                        char = signs.pop()
                    except :
                        print "Error en sintaxis 001: se cerro {} sin abrirse previamente".format(letter)
                        print line
                        exit()
                    if char == chr(ord(letter) - 1) or char == chr(ord(letter) - 2):
                        char
                    else:
                        print "Error en sintaxis 002: se debe cerrar {}".format(char)
                        print line
                        exit()

        if len(signs) > 0:
            print "Error de sintaxis 003: falta cerrar {}".format(signs[0])
            exit()
