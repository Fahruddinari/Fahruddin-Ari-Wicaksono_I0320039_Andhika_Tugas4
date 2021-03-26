#Batas Usia
batas_usia = 21
#input data
umur_sekarang = int(input("Berapa usia kamu: "))
if umur_sekarang>=batas_usia:
    lulus_ujian = input("Apakah anda lulus ujian kualifikasi (Y/T): ")
    if lulus_ujian.upper() == "Y":
        print("Anda dapat mendaftar kursus")
    else:
        print("Anda tidak dapat mendaftar kursus")
else:
    print("Anda tidak dapat mendaftar kursus")