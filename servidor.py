import glob
import os
import zerorpc


class ServidorRPC(object):
    def listar(self):
        arqs = []
        for f in glob.iglob('*.*'):
            arqs.append(f)
        return str(arqs)

    def get(self, elemento):
        arqs = []
        for f in glob.iglob('*.*'):
            arqs.append(f)
            str(arqs)
            if elemento in arqs:
                pass
        return arqs.index(elemento)

    def print(self, elemento):
        arqs = []
        for f in glob.iglob('*.*'):
            arqs.append(f)
            if elemento in arqs:
                conteudo = open(elemento, 'r')
        return conteudo.read()

    def delete(self, elemento):
        arqs = []
        for f in glob.iglob('*.*'):
            arqs.append(f)
            if elemento in arqs:
                pass
        return os.remove(elemento)

    def createArq(self, nome, texto):
        arqs = []
        for f in glob.iglob('*.*'):
            arqs.append(f)
            arquivo = open(nome, 'w')
            arquivo.write(texto)
            arquivo.close()
        return nome + " criado!" 

s = zerorpc.Server(ServidorRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
