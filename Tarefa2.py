def jogaMoedas(arq):
    while True:
        CARA = COROA = 0
        linha = arq.readline().upper()
        
        if linha == '': break
        else:
            for ch in linha:
                if ch == 'H':
                    CARA +=1
                elif ch == 'T':
                    COROA +=1
            total = CARA + COROA
            porcentagem = int((float(CARA)/total)*100)
            if(porcentagem > 50):
                print '%d cara(s)   (%d%%)' %(CARA, porcentagem)
                print 'Mais caras que coroas!'
            else:
                print '%d cara(s)   (%d%%)' %(CARA, porcentagem)
 
arq = open('jogaMoedas.txt')
jogaMoedas(arq)
arq.close()
