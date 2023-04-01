FINAL_MY_ADDRESS_BOOK={}

#CREATING THE ADDRESS BOOK DESIRE BY THE USER//
def MY_ADDRESS_BOOK():
    no_of_contacts = int(input("enter the number of contacts you want to add:"))
    for x in range(no_of_contacts):
        name_of_address_book=input("enter name of address book:")
        if name_of_address_book not in FINAL_MY_ADDRESS_BOOK :
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]={}
            NAME=input("1.ENTER YOUR  FIRST NAME:")
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["FRIST_NAME"]=NAME
            LAST_NAME=input("2.ENTER YOUR LAST NAME:")
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["LAST_NAME"]=LAST_NAME
            PHONE_NUMBER=int(input("3.ENTER YOUR MOBILE NUMBER:"))
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["PHONE_NUMBER"]=PHONE_NUMBER
            E_MAIL=str(input("4.ENTER YOUR E-MAIL:"))
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["E_MAIL"]=E_MAIL
            ZIP_CODE=int(input("5.ENTER THE ZIP CODE OF YOUR CITY:"))
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["ZIP_CODE"]=ZIP_CODE
            CITY=input("6.ENTER YOUR CITY NAME:")
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["CITY_NAME"]=CITY
            STATE=input("7.ENTER YOUR STATE:")
            FINAL_MY_ADDRESS_BOOK[name_of_address_book]["STATE"]=STATE
        else:
            print("contact already exist enter a different name!")
    print(FINAL_MY_ADDRESS_BOOK)
# MY_ADDRESS_BOOK()

#EDITING THE EXISTING ADDRESSBOOK//
def EDIT_MY_ADDRESS_BOOK():
    edit_book=input("ENTER THE NAME OF ADDRESS BOOK TO BE UPDATED:")
    if edit_book not in FINAL_MY_ADDRESS_BOOK:
        print("ADDRESS BOOK DOES NOT EXIST IN FINAL ADDRESS BOOK!")
    else:
        print("address book present in the final address book")
        OPTIONS=('''SELECT THE VLAUES YOU WANT TO DELETE:-
        1.FIRST NAME
        2.LAST NAME
        3.PHONE NUMBER
        4.E_mail
        5.ZIP_CODE
        6.CITY
        7.STATE''')
        print(OPTIONS)
        # ENTER_THE_OF_UPDATES_REQUIRED=int(input("ENTER THE TOTAL NUMBER OF UPDATES YOU WAANT TO MAKE:"))
        # if ENTER_THE_OF_UPDATES_REQUIRED==1:
        #     print("EDIT CAN ONLY BE 1 AT A TIME!")
        # elif ENTER_THE_OF_UPDATES_REQUIRED==20:
        #     print("EDIT CAN ONLY BE 2 AT A TIME!")
        # elif ENTER_THE_OF_UPDATES_REQUIRED==30:
        #     print("EDIT CAN ONLY BE 3 AT A TIME!")
        # elif ENTER_THE_OF_UPDATES_REQUIRED==40:
        #     print("EDIT CAN ONLY BE 4 AT A TIME!")
        # elif ENTER_THE_OF_UPDATES_REQUIRED==50:
        #     print("EDIT CAN ONLY BE 5 AT A TIME!")
        ENTER_KEY_TO_BE_EDITED=int(input("ENTER YOUR DESIRED KEY TO BE UPDATED:"))
        print(ENTER_KEY_TO_BE_EDITED)
        if ENTER_KEY_TO_BE_EDITED==1:
            print("You cannot change the first name in address book. ")
        elif ENTER_KEY_TO_BE_EDITED == 2:
            print("You cannot change the last name in address book. ")    
        elif ENTER_KEY_TO_BE_EDITED == 3:
            PHONE_N0=int(input("ENTER THE NEW PHONE NUMBER:"))
            FINAL_MY_ADDRESS_BOOK[edit_book]["PHONE_NUMBER"]=PHONE_N0
        elif ENTER_KEY_TO_BE_EDITED == 4:
            E_MAIL=input("ENTER THE NEW E_MAIL ADDRESS:")
            FINAL_MY_ADDRESS_BOOK[edit_book]["E_MAIL"] = E_MAIL
        elif ENTER_KEY_TO_BE_EDITED ==5:
            ZIP_CODE=int(input("ENTER THE ZIP CODE OF CITY: "))
            FINAL_MY_ADDRESS_BOOK[edit_book]["ZIP CODE"]=ZIP_CODE
        elif ENTER_KEY_TO_BE_EDITED ==6:
            CITY=input("ENTER THE NEW CURRENT CITY:")
            FINAL_MY_ADDRESS_BOOK[edit_book]["CITY"]=CITY
        elif ENTER_KEY_TO_BE_EDITED==7:
            STATE=input("ENTER THE CURRENT STATE:")
            FINAL_MY_ADDRESS_BOOK[edit_book]["STATE"]=STATE
        # elif ENTER_KEY_TO_BE_EDITED==20:
        #     PHONE_N0=int(input("ENTER THE NEW PHONE NUMBER:"))
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["PHONE_NUMBER"]=PHONE_N0
        #     E_MAIL=input("ENTER THE NEW E_MAIL ADDRESS:")
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["E_MAIL"] = E_MAIL
        # elif ENTER_KEY_TO_BE_EDITED==30:
        #     PHONE_N0=int(input("ENTER THE NEW PHONE NUMBER:"))
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["PHONE_NUMBER"]=PHONE_N0
        #     E_MAIL=input("ENTER THE NEW E_MAIL ADDRESS:")
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["E_MAIL"] = E_MAIL
        #     ZIP_CODE=int(input("ENTER THE ZIP CODE OF CITY: "))
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["ZIP CODE"]=ZIP_CODE
        # elif ENTER_KEY_TO_BE_EDITED==40:
        #     PHONE_N0=int(input("ENTER THE NEW PHONE NUMBER:"))
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["PHONE_NUMBER"]=PHONE_N0
        #     E_MAIL=input("ENTER THE NEW E_MAIL ADDRESS:")
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["E_MAIL"] = E_MAIL
        #     ZIP_CODE=int(input("ENTER THE ZIP CODE OF CITY: "))
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["ZIP CODE"]=ZIP_CODE
        #     STATE=input("ENTER THE CURRENT STATE:")
        #     FINAL_MY_ADDRESS_BOOK[edit_book]["STATE"]=STATE
        else:
            print("ENTER A VALID INPUT!")
    print(FINAL_MY_ADDRESS_BOOK)

# EDIT_MY_ADDRESS_BOOK()    

#DELETING VALUES OF ADDRESS BOOK//
def DELETING_VALUES_FROM_ADDRESS_BOOK():
    DELETE_BOOK=(input("ENETER THE ADDRESS BOOK YOU WANT TO DELETE:"))
    if DELETE_BOOK not in FINAL_MY_ADDRESS_BOOK:
        print("ENTER A VALID NAME OF ADDRESS BOOK!")
    else:
        print(("ADDRESS BOOK PRESENT IN THE FINAL ADDRESS BOOK."))
        OPTIONS=('''SELECT THE VLAUES YOU WANT TO DELETE:-
        1.FIRST NAME
        2.LAST NAME
        3.PHONE NUMBER
        4.E_mail
        5.ZIP_CODE
        6.CITY
        7.STATE''')
        print(OPTIONS)
    # DELETE_BOOK=(int(input("ENTER WHAT YOU WANT TO DELETE?")))
    # print("1.KEY OF THE ADDRESS BOOK/n2.VALUES OF ADDRESS BOOK")
        DELETE_BOOK=int(input("ENTER THE SPECIFIED VALUE YOU WANT TO DELETE:"))
        if DELETE_BOOK==1:
            FINAL_MY_ADDRESS_BOOK.popitem#("FIRST NAME")
        # elif DELETE_BOOK==2:
        #     FINAL_MY_ADDRESS_BOOK.pop("LAST NAME")
            
        # # elif DELETE_BOOK==3:
        #         FINAL_MY_ADDRESS_BOOK.popitem("PHONE_NUMBER")
        # elif DELETE_BOOK==4:
        #         FINAL_MY_ADDRESS_BOOK.popitem("E_MAIL")
        # elif DELETE_BOOK==5:
        #         FINAL_MY_ADDRESS_BOOK.popitem("ZIP_CODE")
        
        # elif DELETE_BOOK==6:
        #         FINAL_MY_ADDRESS_BOOK.popitem("CITY")
        
        elif DELETE_BOOK==7:
                FINAL_MY_ADDRESS_BOOK.popitem("STATE")
        
        print(FINAL_MY_ADDRESS_BOOK)

def exit():
    print("GOOD BYE$$")


if __name__ == "__main__":

    while(True):
        BEGINING='''WELCOME TO THE ADRRESS BOOK SELECT THE OPERATION TO BE PERFORMED
        1. SHOW THE EXISTING ADDRESS BOOK.
        2.CREATE A NEW ADDRESS BOOK.
        3.EDIT THE EXISTING ADDRESS BOOK.
        4.DELETE VALUES FROM EXISTING ADDRESS BOOK
        5.exit'''
        print(BEGINING)
        YOUR_CHOICE=int(input("ENTER YOUR CHOICE FOR THE PHONE BOOK:"))
        if YOUR_CHOICE==1:
            print(FINAL_MY_ADDRESS_BOOK)
        elif YOUR_CHOICE==2:
            MY_ADDRESS_BOOK()
        elif YOUR_CHOICE==3:
            EDIT_MY_ADDRESS_BOOK()
        elif YOUR_CHOICE==4:
            DELETING_VALUES_FROM_ADDRESS_BOOK()   
        elif YOUR_CHOICE==5:
            exit() 
            break
        else:
            print('''PLEASE TRY AGAIN!
            WITH A VALID CHOICE.''')
        
            break