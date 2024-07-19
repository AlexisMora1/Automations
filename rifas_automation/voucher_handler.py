import re
import pywhatkit
import time


def info_extractor(file, ticket_cost):
    # Finding the amount from the Voucher
        for x in file:
            monto = re.search('[$][0-9]{'+str(len(str(ticket_cost)))+'}', x)
            if monto != None:
                break
        # Finding the Concept (Name and number)
        for x in file:
            client = re.search('[a-zA-Z]+.*[a-zA-Z]*.*[0-9]{10}', x)
            if client != None:
                break
        
        amount = int(re.split('[$]', monto.group())[1])

        # Here we proccess the client match objects, the first list returns name, the second one returns a list of phone number matches
        client_list = re.split('[0-9]{10}', client.group())
        client_list1 = re.split('[a-zA-Z]+', client.group())

        name = client_list[0]

        # Here we deal with the possible errors in the match
        for x in client_list1:
            phone = x
            if phone == ' ' or phone == '':
                continue
            elif len(phone)<10: 
                continue
            else: break


        phone_split = re.split(' ',phone)
        if phone_split[0] == '':
            phone = phone_split[1]

        if int(phone[0])==0:
            phone = phone[1:]

        return [name, amount, phone]

class Voucher():

    def __init__(self, ticket_cost : int, file) -> None:
        data = info_extractor(file,ticket_cost)
        self.name = data[0]
        self.phone = data[2]
        self.amount = data[1]
        self.ticket_count = int(self.amount)/25
        self.ticket_cost = ticket_cost

    def send_voucher_confirmation(self, clients_file, clients_amount):
        actual_register = clients_amount + 1
        for i in range(0,int(self.ticket_count)):
            clients_file.write(self.name)
            clients_file.write(',')
            clients_file.write(self.phone)
            clients_file.write(',')
            clients_file.write(str(actual_register+i))
            clients_file.write('\n')
            # pywhatkit.sendwhatmsg_instantly('+52'+self.phone,'Hola ' + self.name + ', muchas gracias por apoyarnos comprando un boleto, su numero es: '+str(actual_register+i),tab_close=True,close_time=10)
            # time.sleep(20)

