import io

if __name__ == '__main__':
    Output = open("HELLO WORLD", 'w+')
    for idx, lines in enumerate(open("links-anon.txt")):
        Output.write(list(str(lines).split(' '))[0] + "\n" + list(str(lines).split(' '))[1] + "\n")
        print((idx/1963263821)*100,"%")
    Output.close()

