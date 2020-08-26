import os

from command_line_arguments import check_if_update
from login_and_password_input import login_and_password_input
from handle_login_and_password_file import write_login_and_password_to_file, read_login_and_password_from_file
from login_to_amazon import login_to_amazon

args = check_if_update()
login = args.l
password = args.p

if not login or not password:
    if os.path.exists("C:/Users/Alex/PycharmProjects/amazon_login/login_data.txt"):
        login, password = read_login_and_password_from_file("C:/Users/Alex/PycharmProjects/amazon_login/login_data.txt")
    else:
        login, password = login_and_password_input()
        write_login_and_password_to_file("C:/Users/Alex/PycharmProjects/amazon_login/login_data.txt", login, password)
else:
    write_login_and_password_to_file("C:/Users/Alex/PycharmProjects/amazon_login/login_data.txt", login, password)

driver = login_to_amazon(login, password)

input("press enter to close")
driver.close()


