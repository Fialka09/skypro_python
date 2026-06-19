from address import Address
from mailing import Mailing

to_address = Address("129090", "Москва", "Проспект Мира", "26", "1")
from_address = Address("109012", "Москва", "Театральный проезд", "5", "1")

mail = Mailing(to_address, from_address, 75, "RU123456789")


print(mail)
