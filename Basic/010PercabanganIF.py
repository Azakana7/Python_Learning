
#? Durasi: 01:16:44
is_Day = False
is_Night = True

# if is_Day:
#     print("Selamat siang dunia!")
# else:
#     print("Ini kapan njir")



# def mathVariable():
#     X = float(input("Masukkan Nilai Pertama: "))
#     Y = float(input("Masukkan Nilai Kedua: "))
#     D = X + Y


#     if X and Y:
#         print(f"Hasil dari X + Y = {D}")
#     else:
#         print("Tolong masukkan lagi angka anda")

# mathVariable()

print("""

        
 ▄████▄   █    ██  ▄▄▄       ▄████▄   ▄▄▄      
▒██▀ ▀█   ██  ▓██▒▒████▄    ▒██▀ ▀█  ▒████▄    
▒▓█    ▄ ▓██  ▒██░▒██  ▀█▄  ▒▓█    ▄ ▒██  ▀█▄  
▒▓▓▄ ▄██▒▓▓█  ░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒░██▄▄▄▄██ 
▒ ▓███▀ ░▒▒█████▓  ▓█   ▓██▒▒ ▓███▀ ░ ▓█   ▓██▒
░ ░▒ ▒  ░░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░ ▒▒   ▓▒█░
  ░  ▒   ░░▒░ ░ ░   ▒   ▒▒ ░  ░  ▒     ▒   ▒▒ ░
░         ░░░ ░ ░   ░   ▒   ░          ░   ▒   
░ ░         ░           ░  ░░ ░            ░  ░
░                           ░                  
By: Divo Saputra            
            1.Cerah 
            2.Gelap
            3.Panas
            4.Dingin

""")

def cuaca():
    # print("""
    #         1.Cerah 
    #         2.Gelap
    #         3.Panas
    #         4.Dingin  
    #         """)
    Cuaca = input('Cuaca Apa Hari Ini King: ')
    
    #! If Else Sederhana Untuk Menanyakan Cuaca
    if Cuaca == '1':
        print('Sungguh Hari Yang Indah!')

    elif Cuaca == '2':
        print('Langitnya ireng loh ya!')

    elif Cuaca == '3':
        print("Puanase cikkkkk!")

    elif Cuaca == '4':
        print("Thomas Slebew Abies")
cuaca()