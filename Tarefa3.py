# -*- coding: cp1252 -*-
TAM = 10 
 
lista = []
for i in range(TAM):
    lista.append(i) 

def leLista(lista):
    try:
        print 'Entrando no try'
        ent = open('numeros.txt')
        while True:
            arqLidoAux = ent.readline()
            arqLido = arqLidoAux.splitlines()
            for ch in arqLido:
                num= ''
                if ch.isdigit():
                    num += ch
            if arqLidoAux == '':break
            else:
                lista.append(int (num))
    except IndexError as e:
        print "Erro no índice: " + e.message
    except IOError as e:
        print "Erro de entrada/saída: " + e.message
    except UnboundLocalError as e:
        print "Erro de atribuição: " + e.message
    finally:
        print 'Fechando o arquivo de entrada'
        ent.close()

def imprimeLista(lista):
    try:
        leLista(lista)
        print 'Entrando no try'
        out = open('arqSai.txt', 'w')
        for i in range(len(lista)):
            out.write('Valor na posição %d: %d\n' %(i, lista[i]))
    except IndexError as e:
        print "Erro no índice: " + e.message
    except IOError as e:
        print "Erro de entrada/saída: " + e.message
    except UnboundLocalError as e:
        print "Erro de atribuição: " + e.message
    except Exception as e:
        print "Erro: " + e.message
    finally:
        print 'Fechando o arquivo de saída'
        
        out.close()


imprimeLista(lista)

'''
lê o valor e põe no final da lista
'''
