#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = []

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            if val not in total:
                total.append(val)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))
            total.clear()
            curkey = key
            total.append(val)

    sys.stdout.write("{}\t{}\n".format(curkey, total))