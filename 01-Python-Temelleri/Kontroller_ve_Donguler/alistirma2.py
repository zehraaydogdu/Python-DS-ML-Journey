# 1) Aşağıdaki kodun çıktısı ne olacaktır?
x = 5
y = 3
z = 6
x > y and z > x

#True olacaktır
print(x > y and z > x)

# 2) Aynı değerlerle kod şu şekilde değiştilirse çıktı ne olacaktır?
x < y or z > y

#True olacaktır
print(x < y or z > y)

# 3) Aşağıdaki kodun çıktısı ne olacaktır?

yas = 20

if yas < 18:
    print("18 yasindan küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasinda bir gencsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasina gelmissiniz")
else:
    print("40 yasindan daha büyüksünüz")

#18 ile 30 yaş arasında bir gençsiniz

#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

if "c" in my_dictionary.values():
    print("Evet")

#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}

if "a" in my_other_dictionary.keys():
    print("Evet")

#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

for i in my_numbers:
    if i % 2 == 0:
        print(i)

#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir. 
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.
r_list = [3,2,5,8,4,6,9,12]

pi = 3.14
cevre_listesi = []

for r in r_list:
    cevre_listesi.append(2 * pi * r)

print(cevre_listesi)

#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.
# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]

yas_listesi = []
for (isim, yas) in age_name_list:
    yas_listesi.append(yas)

print(yas_listesi)

#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]

from random import randint

print(metal_list[randint(0, len(metal_list)-1)])

#10) Aşağıdaki kodun çıktısı ne olacaktır?
number_list = [5,7,18,21,20,10,405,24]
[num % 2 == 0 for num in number_list]

print([num % 2 == 0 for num in number_list])