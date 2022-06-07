#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
   
    for line in sys.stdin:

        par=[]
        line=line.replace('\n','')
        num,letras = line.split('\t')
        letras=letras.split(',')
        for letra in letras:
            par.append([num,letra])
        for par in par:
            sys.stdout.write(str(par[1])+'\t'+str(par[0])+'\n')