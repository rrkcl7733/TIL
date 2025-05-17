def is_valid_car_number(car):
    if len(car) != 8:
        return False

    if not (car[0] in '123456789' and car[1] in '123456789' and car[0] == car[1]):
        return False

    if not (car[2] in '123456789' and car[3] in '123456789'):
        return False

    if not ('A' <= car[4] <= 'Z'):
        return False

    if not (car[5] in '123456789' and car[6] in '123456789' and car[7] in '123456789'):
        return False

    return True


for _ in range(int(input())):
    car_number = input()
    if is_valid_car_number(car_number):
        print(car_number)
