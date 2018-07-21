#/*****************************
# Trabalho PAA - 2017.2 - parse para o Lindo Linear Programming 
# Tratando a entrada bugada
#******************************

def funcao_objetiva(nc):
    charsert = '%s+'
    fo = ''
    for i in range(1,nc+1):
        fo += 'k'+str(i)+'+'
    return 'max '+fo[:-1]

def line_generator(l,a):
    minus_count = 0
    charset_minus = '-x%s'
    charset_plus = 'x%s'
    k = '-k%d >= '

    newline = ''
    for i in l[2:]:
        if int(i) > 0:
            newline += '+' + charset_plus %i
        else:
            minus_count -= 1
            newline += charset_minus %(i.replace('-', ''))
    return newline + k%a + str(minus_count)+'\n'


f = open('Teste2.txt')#instancia ----- mude aqui
#f = open('teste.txt')

novo = open('saida22.txt','w+')#nome do arquivo de saida ---- mude aqui
nc = f.readline().split()[1]
novo.write(funcao_objetiva(int(nc))+'\n')
novo.write('st\n')

#f.next()
a = 1

for i in f:
    l = i.split()

    if int(l[0]) > 4 and int(l[0]) <= 10:
        down = f.next().split()
        new_line = l + down
        novo.write(line_generator(new_line,a))

    elif int(l[0]) > 10:
        down = f.next().split()
        down2 = f.next().split()

        new_line = l + down + down2
        novo.write(line_generator(new_line,a))

    else:
        new_line = l
        novo.write(line_generator(new_line,a))
    a += 1

novo.write('end')
novo.close()
f.close()
