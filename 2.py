import math
def pecahanKembalian(Total, Dibayar):

    PECAHAN_UANG = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    #constant isi pecahan uang untuk dicek
    Kembalian = []

    Total_rounded = math.floor((Dibayar-Total)/100) * 100
    #pembulatan kebawah ke 100an terdekat 

    if(Total_rounded < 0):
        print("False, kurang bayar")
        return False
    else:
        print("Kembalian yang harus diberikan kasir: "+ str(Dibayar - Total))
        print("Dibulatkan menjadi " + str(Total_rounded))

    #cek kelipatan dan kurangi total jumlah setiap loop.
    for i, pecahan in enumerate(PECAHAN_UANG):
        Kembalian.append(int(Total_rounded/pecahan))
        Total_rounded = Total_rounded % pecahan

        #code to print out result, eksekusi jika total=0
        if(Total_rounded<=0):
            for j, pecahan_kembalian in enumerate(Kembalian):
                if(pecahan_kembalian>0):
                    print("{} {} {}".format(pecahan_kembalian, "lembar" if PECAHAN_UANG[j]>=1000 else "koin", PECAHAN_UANG[j]))

pecahanKembalian(700649, 800000)
pecahanKembalian(575650, 580000)
pecahanKembalian(657600, 600000)