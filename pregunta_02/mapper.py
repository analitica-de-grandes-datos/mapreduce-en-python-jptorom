#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        beta=line.split(",")[3]
        alfa= line.split(",")[4]
        sys.stdout.write("{}\t1\n".format(beta,alfa))
