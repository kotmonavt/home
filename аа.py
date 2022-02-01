s = str(input())
numb = str()
for i in s:
    if (i == "0") or (i == "1") or (i == "2") or (i == "3") or (i == "4") or (i == "5") or (i == "6") or (i == "7") or (i == "8") or (i == "9"):
        numb = numb + i
new_numb = sorted(numb)
number = ''.join(new_numb)
print(number)



#принимаем две строки. вывод одной строки, которая состоит из общих элементов двух строк
#f_name = str(input())
#s_name = str(input())
#full = str()
#for i in f_name:
#    if i in s_name:
#        full = full + i
#print(full)


