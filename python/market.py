import os

client_ident=[]
client_fullname=[]
client_address=[]
client_mobile=[]
client_email=[]
client_gender=[]
client_age=[]

product_code = []
product_name = []
product_quantity = []
product_unit_vale = []

def mainMenu():
    os.system("clear")
    print(":::MARKET MAIN MENU:::")
    print(
        "[1]. Register client \n" \
        "[2]. Register product \n" \
        "[3]. list clients\n" \
        "[4]. List products \n" \
        "[5]. Search client by ident \n" \
        "[6]. Search product by code \n" \
        "[7]. Update client \n" \
        "[8]. Update product \n" \
        "[9]. Delete client \n" \
        "[10]. Delete product \n" \
        "[11]. Exi \n" \
        ".:: Press any option:" )


# Main
menu_status = True
while menu_status:
    mainMenu()
    opt = int(input())

    if opt == 1:
        os.system('clear')
        print('...................................')
        print('.............NEW CLIENTS...........')
        print('...................................')
        ident = input('Client identification: ')
        client_ident.append(ident)
        fullname= input('Client dullname: ')
        client_fullanme.append(fullname)
        print('Client has been registered successfully !!!')
        key = input('Press any option to back main menu')
    elif opt == 3:
        os.system('clear')
        print('...................................')
        print('.............LIST CLIENTS...........')
        print('...................................')
        
        i=0
        while  i < len(client_fullname):
            print('Identification      |  fullname')
            print(f'{client_ident[i]}   |    {client_fullname[i]}')
            i+=1

        key = input('Press any option to back main menu.')
    


    if opt == '11':
        print('Bye, bye')
    if opt < 1 or opt > 11:
        key = input('Invalid option. Try again. \n' \
         'Press any key to continue.')
        