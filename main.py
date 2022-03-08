import ScientificCalc
import SimpCalcClass

class main():
    print("\tCALCULATOR\n---------------")
    while True:
        calcChoice = int(input("\n--Hesap Makinesi Seçimi--\n1.Basit Hesap Makinesi\n2.Bilimsel Hesap Makinesi\n3.Çıkış\nSeçim :"))
        if calcChoice == 1:
            print("\n-BASİT HESAP MAKİNESİ-\n----")
            x = float(input("\n1. Sayıyı Giriniz : "))
            y = float(input("2. Sayıyı Giriniz : "))

            basicCalc = ScientificCalc.ScientificCalcClass(x,y)


            print("\n1. Toplama\t2. Çıkarma\t3. Çarpma\t4. Bölme\t5. Çıkış")
            secim = int(input("\nSeçiminiz : "))
            print("---")

            if secim == 1:
                basicCalc.toplama()
            elif secim == 2:
                basicCalc.cikarma()
            elif secim == 3:
                basicCalc.carpma()
            elif secim == 4:
                basicCalc.bolme()
            elif secim == 5:
                print("Çıkış yapılıyor...")
                continue
            else:
                print("Geçerli bir seçim giriniz")

        elif calcChoice == 2:
            print("\n-BİLİMSEL HESAP MAKİNESİ-\n----\n1. Üs Alma\n2. Kare Alma\n3. Faktöriyel\n4. Log\n5. Sin Rad\n6. Cos Rad\n7. Tan Rad\n8. Cot Rad\n9. Cosec Rad\n10. Sec Rad\n",
                "11. Sinalpha\n12. Cosalpha\n13. Tanalpha\n14. Cotalpha\n15. Cosecalpha\n16. Secalpha\n17. Çıkış")
            scChoice = int(input("Seçiminiz : "))
            if scChoice == 1: #Üs Alma
                x = float(input("Taban Sayı : "))
                y = float(input("Üs sayısı : "))
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.usAl()#
            if scChoice == 2:#Kare alma
                x = float(input("Karesi alınacak sayı : "))
                scCalc = ScientificCalc.ScientificCalcClass(x,float(2))
                scCalc.kareAl()
            if scChoice == 3:#Faktoriyel
                x = int(input("Faktöriyeli alınacak sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.faktoriyel()
            if scChoice == 4:#Logaritma
                x = int(input("Log taban : "))
                y = int(input("Log üs : "))
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.log()
            if scChoice == 5:# Sin
                x = float(input("Sin Rad için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.sin()
            if scChoice == 6:#Cos
                x = float(input("Cos Rad için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.cos()
            if scChoice == 7:# Tan
                x = float(input("Tan Rad için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.tan()
            if scChoice == 8:# Cot
                x = float(input("Cot Rad için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.cot()
            if scChoice == 9:# Cosec
                x = float(input("Cosec Rad için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.cosec()
            if scChoice == 10:# Sec
                x = float(input("Sec Rad için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.sec()
            if scChoice == 11: #sin-1
                x = float(input("Sinalpha için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.sin1()
            if scChoice == 12: #cos-1
                x = float(input("Cosalpha için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.cos1()
            if scChoice == 13:#tan-1
                x = float(input("Tanalpha için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.tan1()
            if scChoice == 14:#cot-1
                x = float(input("Cotalpha için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.cot1()
            if scChoice == 15:#cosec-1
                x = float(input("Cosecalpha için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.cosec1()
            if scChoice == 16:#sec-1
                x = float(input("Secalpha için sayı : "))
                y = 0
                scCalc = ScientificCalc.ScientificCalcClass(x,y)
                scCalc.sec1()
            if scChoice == 17:#cikis
                print("Çıkış yapılıyor...")
                continue
            else:
                print("Geçerli bir seçim giriniz")






        elif calcChoice == 3:
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçerli bir sayı giriniz")
