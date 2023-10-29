#menghitung luas bangun datar
print("==================================")
print("program penghitung luas bangun datar")
print(''' 
pilih salah satu bangun datar:
1=luas persegi
2=luas lingkaran
3=luas segitiga
''')

pilihan= int(input("masukan pilihan:"))
match pilihan:
     case 1:
         sisi= int(input("masukan sisi:"))
         luas= sisi*sisi
         print("luas persegi dengan sisi","adalah",luas)
     case 2:
        jari= int(input("masukan jari-jari: "))   
        luas= 3.14*jari**2
        print("luas lingkaran dengan jari-jari",jari,"adalah:",luas)
     case 3:
        alas=int(input("masukan alas"))   
        tinggi=int(input("masukan tinggi:"))
        luas=1/2*alas*tinggi
        print("luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah:",luas)
     case _:
        print("pilihan salah.")  