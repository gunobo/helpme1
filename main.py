import os
import contact_class
import contact_function


if __name__ == "__main__":
  os.system('cls')
  contact_list = []
  whitel True:
  menu = print_menu()
  if menu == 1:
    input_contact(contact_list)
  elif menu == 2:
    print_contact(contact_list)
  elif menu == 3:
    delete_contact(contact_list)
  elif menu == 4:
    print("프로그램을 종료합니다.")
    break
    
