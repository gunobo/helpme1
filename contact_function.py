def set_contact():
  name = input("Name :")
  phone_number = input("Phone Number :")
  e_mail = input("E-mail :")
  addr = input("Address :")
  print("{} / {} / {} / {}".format(name, phone_number, e_mail, addr))
  return Contact(name, phone_number, e-mail, addr)

def print_menu():
  import os
  print("연락처 프로그램")
  print("1. 연락처 입력")
  print("2. 연락처 출력")
  print("3. 연락처 삭제")
  print("4. 종료")
  print(" # 기능은 번호를 입력해야 합니다 #")
  menu = input("기능을 선택하세요: ")
  os.system('cls')
  return int(menu)

def input_contact(contact_list):
  print("연락처 정보를 입력해주세요.")
  contact = set_contact()
  contact_list.append(contact)
  input("엔터를 입력하여 메뉴화면으로 넘어가세요.")
  
def print_contact(contact_list):
  for contact in contact_list:
    contact.print_info()
    print("====================")
  input("엔터를 입력하여 메뉴 화면으로 넘어가세요")
  
def delete_contac(contact_list):
  name = input("삭제할 연락처의 이름을 입력해주세요 :")
  for i, contact in enumerate(contact_list):
    if contact.name == name:
      del contactlist[i]
  print("{}의 연락처를 삭제했습니다.".format(name))
  input("엔터를 입력하여 메뉴화면으로 넘어가세요.")
