from smartphone import Smartphone


catalog = [
    Smartphone("Самсунг", "S21", "+7903665439"),
    Smartphone("Apple", "iPhone 17", "+79215557788"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79123456789"),
    Smartphone("Huawei", "P60 Pro", "+79231234567"),
    Smartphone("Realme", "GT Neo 5", "+79189898989")
]

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.mobile_number}")
