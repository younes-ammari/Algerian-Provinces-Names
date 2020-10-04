
print()
wilayas = {
    1:	"Adrar",
    2:	"Chlef",
    3:	"Laghouat",
    4:	"Oum el-Bouaghi",
    5:	"Batna",
    6:	"Béjaïa",
    7:	"Biskra",
    8:	"Béchar",
    9:	"Blida",
    10:	"Bouïra",
    11:	"Tamanghasset",
    12:	"Tébessa",
    13:	"Tlemcen",
    14:	"Tiaret",
    15:	"Tizi Ouzou",
    16:	"Algiers",
    17:	"Djelfa",
    18:	"Jijel",
    19:	"Sétif",
    20:	"Saïda",
    21:	"Skikda",
    22:	"Sidi Bel Abbès",
    23:	"Annaba",
    24:	"Guelma",
    25:	"Constantine",
    26:	"Médéa",
    27:	"Mostaganem",
    28:	"M'sila",
    29:	"Mascara",
    30:	"Ouargla",
    31:	"Oran",
    32:	"El Bayadh",
    33:	"Illizi",
    34:	"Bordj Bou Arréridj",
    35:	"Boumerdès",
    36:	"El Taref",
    37:	"Tindouf",
    38:	"Tissemsilt",
    39:	"El Oued",
    40:	"Khenchela",
    41:	"Souk Ahras",
    42:	"Tipaza",
    43:	"Mila",
    44:	"Aïn Defla",
    45:	"Naâma",
    46:	"Aïn Témouchent",
    47:	"Ghardaïa",
    48:	"Relizane",
    49:	"El M'ghair",
    50:	"El Menia",
    51:	"Ouled Djellal",
    52:	"Bordj Baji Mokhtar",
    53:	"Béni Abbès",
    54:	"Timimoun",
    55:	"Touggourt",
    56:	"Djanet",
    57:	"In Salah",
    58:	"In Guezzam"
    }

    
def wilaya_name(number):
    print('The Wilaya is '+ wilayas[number])

while True:
    try:
        number = input('Enter wilaya number to see its name : ')
        if number == 'exit' or number == '':
            exit
        elif int(number) in wilayas:
            wilaya_name(int(number))
        else:
            print('Wilaya number not icluded .... the numbers are between [1-58] \nenter a valid number')
        pass
    except :
        print('Wilaya number not icluded .... the numbers are between [1-58] \nenter a valid number')
        pass


