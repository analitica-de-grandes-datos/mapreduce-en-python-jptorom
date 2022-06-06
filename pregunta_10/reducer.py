import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        numero,letra =line.split()
        letrica = letra.split(",")
        for i in letrica:
            sys.stdout.write("{}\t{}\n".format(i, numero))#