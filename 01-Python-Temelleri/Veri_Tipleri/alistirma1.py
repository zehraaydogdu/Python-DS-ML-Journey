# 1) Asagidaki string'in 5. harfini bir degiskene atayiniz
my_string = "Python Ogreniyorum"

x = my_string[4]
print(x)

# 2) Asagidaki String'in 5. ve 8. karakteri arasindaki tum harflerini yazdiriniz (5 ve 8 dahil)
my_new_string = "ProgramlamayaMerhabaDedik"

print(my_new_string[4:8:])

# 3) Asagidaki String'i kod ile tersten yazin
my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"

print(my_last_string[::-1])

# 4) Asagidaki islemin sonucu hangi veri tipinde olacaktir?
4 + 12.2 + 48

#Float olacaktır. Python bunu algılar.

sonuc = (4 + 12.2 + 48)
print(type(sonuc))

# 5) Asagidaki islemin sonucu kactir?
5 + 7 * 12

#89dur
sonuc2 = 5 + 7 * 12
print(sonuc2)

# 6) Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]

listem = [1, 3, "a"]
print(listem)

listem = list()
listem.append(1)
listem.append(3)
listem.append("a")
print(listem)

# 7) Asagidaki "b"'yi tek satirda aliniz:
my_list = [3.14,4,[2,3,"b"],True]

print(my_list[2][2])

# 8) Asagidaki "a"'yi tek satirda aliniz:
my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}

print(my_dictionary["kk2"][1]["k21"])

# 9) Asagidaki liste set'e cevirilince hangi degerler icinde kalacaktir?
my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]

#3,4,9,21,22,10 kalır
print(set(my_list_to_be_set))

# 10) Asagidaki ifadenin sonucu ne olacaktir?
x = 30 * 5 + 3
y = 108 - 2 * 4
x > y

#True döner
print(x > y)