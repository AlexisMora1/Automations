import voucher_handler
from voucher_handler import Voucher

file = open(r'Here your Nobres.txt path','r')

voucher = Voucher(25, file=file)

file.close()

with open(r'Here your clients.csv path') as f:
    registros = sum(1 for x in f)

clients_file = open(r'Here your clients.csv path','a')

voucher.send_voucher_confirmation(clients_file, registros)

clients_file.close()
