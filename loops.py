#Katryn Munoz
#October 21, 2023
#Description: Kat's Snack Bar Menu will display a menu option
#where the user can choose from and receive a grand total plus tax.

def main():
    # constants
    MENU_OPTION_1= 2.50
    MENU_OPTION_2=1.00
    MENU_OPTION_3= 2.00
    MENU_OPTION_4=0.50
    MENU_OPTION_5=3.00
    TAX=0.07
    SUBTOTAL=0.00

    # declare variable
    name=""
    newOrder = ""
    selection=0
    total_tax=0.0
    grand_total=0.0

    # display intro
    print("Hello! Welcome to Kat's Snack Bar Menu!")
    
    # as long as newOrder is NOT equal to "no": continue, when newOrder is EQUAL to "no", don't continue, skip
    while newOrder != "no" or newOrder != "n" or newOrder != "No" or newOrder != "N":

        # reset selection, subtotal for new order
        selection=0
        SUBTOTAL=0.00
        # ask for name, welcome user
        name=(input("\nPlease tell us your name to get started: "))
        print(f"Welcome {name}!\n")
    
        #Display menu options

        # while selection is not 6, do this
        while selection != 6:
            # menu
            print("*"*20)
            print("Please select from our menu options:\n")
            print(f"1) Fries ${MENU_OPTION_1:,.2f} \n2) Chips ${MENU_OPTION_2:,.2f} \n3) Soda ${MENU_OPTION_3:,.2f} \n4) Candy Bar ${MENU_OPTION_4:,.2f} \n5) Mini Sandwich ${MENU_OPTION_5:,.2f} \n6) I'm done\n")
            print("*"*20)
            #subtotal
            print(f"Subtotal: ${SUBTOTAL:,.2f}")
            print("*"*20)

            #ask for selection
            selection=int(input("\nSelection: "))
            
            #selection menu and math
            # if user puts anything that's not an option
            if selection not in range(1, 6):
                print("*"*20)
                print("PLEASE CHOOSE CORRECTLY.")
            if selection==1:
                SUBTOTAL = SUBTOTAL + MENU_OPTION_1
            if selection==2:
                SUBTOTAL = SUBTOTAL + MENU_OPTION_2
            if selection==3:
                SUBTOTAL = SUBTOTAL + MENU_OPTION_3
            if selection==4:
                SUBTOTAL = SUBTOTAL + MENU_OPTION_4
            if selection==5:
                SUBTOTAL = SUBTOTAL + MENU_OPTION_5

        # math for calculating tax and grand total
        total_tax = SUBTOTAL * TAX
        grand_total = total_tax+SUBTOTAL
        print(f"Subtotal: ${SUBTOTAL:,.2f}")
        print(f"Tax: ${total_tax:,.2f} ")
        print(f"Grand Total: ${grand_total:,.2f}")

        # ask for additional order
        newOrder = input("Additional order? (y or n): ")
main()