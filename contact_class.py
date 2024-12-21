class Contact:
  def __init__(self, name, phone_number, e_mail, addr):
    self.name = name
    self.phone_number = phone_number
    self.e_mail = e_mail
    self.addr = addr
  
  def print_info(self):
    print("Name :", self.name)
    print("Phone Number :", self.phone_number)
    print("E-mail :", self.self.e_mail)
    print("Address :", self.addr)

