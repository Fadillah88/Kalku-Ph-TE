def calculate():
    operation = input('''
Simbol buat:
+ for penambahan
- for pengurangan
* for perkalian
/ for pembagian
''')

    nomor_1 = int(input('Masukan nomor pertama: '))
    nomor_2 = int(input('Masuka nomor kedua: '))

    if operation == '+':
        print('{} + {} = '.format(nomor_1, nomor_2))
        print(nomor_1 + nomor_2)

    elif operation == '-':
        print('{} - {} = '.format(nomor_1, nomor_2))
        print(nomor_1 - nomor_2)

    elif operation == '*':
        print('{} * {} = '.format(nomor_1, nomor_2))
        print(nomor_1 * nomor_2)

    elif operation == '/':
        print('{} / {} = '.format(nomor_1, nomor_2))
        print(nomor_1 / nomor_2)

    else:
        print('Tak valid, mohon input kembali.')

    again()

def again():
    calc_again = input('''
Ketik Y untuk melanjutkan, ketik N untuk membatalkan.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Sampai Jumpa.')
    else:
        again()

calculate()
