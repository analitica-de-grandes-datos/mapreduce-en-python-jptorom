#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0
    date = None

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, date, val = line.split("\t")
        val = int(val)

        if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
            sys.stdout.write("{}   {}   {}\n".format(curkey, date, total))

        curkey = key
        total = val
        date = date

    sys.stdout.write("{}   {}   {}\n".format(curkey, date, total))