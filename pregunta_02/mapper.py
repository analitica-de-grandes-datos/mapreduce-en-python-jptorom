#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        beta=line.split(",")[3]
        alfa=line.split(",")[4]
        sys.stdout.write("{}\t{}\n".format(beta,alfa))