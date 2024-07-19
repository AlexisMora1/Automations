Hello! Welcome to our raffle automation project, this file will explain you how make use of this
little project to enable you waste less time when managing raffles. 

The original idea its to use a power automate flow to extract the text from the voucher jpeg or 
png, then write that information in the Nombres.txt file and execute rifa_script.py with the
Power Automate CMD Session option, so if youre a new member of COMEMAT FCFM you can access to the 
flow structure by the One Drive service.

Lets take a look trhough the project files:

- voucher_handler.py

    This file store the Voucher class object wich enable extract your client information of a
    file-like-object, it has only one method named "send_voucher_confirmation" with allows you to
    send a whatsapp message to your client and registering the buy in the clients.csv file.

- rifa_script.py

    This file create the Voucher object and exectutes the send_voucher_confirmation method.

- Nombres.txt

    Here is supposed to be your scanned voucher, I include an example with wich I created all
    the project.

- clients.csv

    This is the final file, here the "send_voucher_confirmation" method store the information of 
    yout clients and tickets.

