import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

 # ls arquivos
print(c.listar())

# get >>> posicao no array 
print(c.get('teste0.txt'))

# return conteudo
print(c.print('Teste.java'))

# deleta arquivo - INSERIR NOME DO ARQUIVO...
c.delete('nome_do_arquivo')
# nova lista
print(c.listar()) 

#cria arquivo txt e adiciona conteudo
print(c.createArq('nome-do-arquivo.txt', 'conteudo'))
