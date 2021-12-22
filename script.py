import json
import re
import time
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Get path file input')
parser.add_argument('output', help='Get path file output')
args = parser.parse_args()


class Validator:
    """
    Объект класса Validator
    Он нужен для того, что проверить данные валидными или нет
    """
    def __init__(self):
        pass

    def check_email(email: str) -> bool:
        '''
        Выполняет проверку корректности адреса электронной почты.

        Если в строке присутствуют пробелы, запятые, двойные точки,
        а также неверно указан домен адреса, то будет возвращено False.

        Parameters
        ----------
          email : str
            Строка с проверяемым электронным адресом

        Returns
        -------
          bool:
            Булевый результат проверки на корректность
        '''
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, email):
            return True
        return False

    def check_height(height: str) -> bool:
        """
        Выполняет проверку корректности роста
        Если рост меньше '1.22' или больше '2.51' то будет ворвращено False

        Параметры
        ---------
          height : str
            Параметр для проверки корректности

        Return
        ------
          bool:
            Булевый результат на коррестность
        """
        pattern = '[1-2]\.\d{2}'
        if re.match(pattern, str(height)) is not None:
            if 1.22 < float(height) < 2.51:
                return True
        return False

    def check_inn(inn: str) -> bool:
        """
        Выполняет проверку корректности ИНН
        Если ИНН не состоит из последовательности 12 цифр то возвращено False

        Параметры
        ---------
          inn : str
            Строка для проверки корректности

        Return
        ------
          bool:
            Булевый результат на корректность
        """
        if len(inn) == 12:
            return True
        return False

    def check_passport(passport: int) -> bool:
        """
          Выполняет проверку корректности номера паспорта
          Если номер паспорта не состоит из последовательности 6 цифр то возвращено False

          Параметры
          ---------
            passport : int
              Целое число для проверки корректности

          Return
          ------
             bool:
               Булевый результат на корректность
          """
        if len(str(passport)) == 6:
            return True
        return False

    def check_address(address) -> bool:
        """
          Выполняет проверку корректности адреса
          Если адрес нет строки или указан не в формате "улица пробел номер дома" то возвращено False

          Параметры
          ---------
            address:
              Параметр для проверки корректности

          Return
          ------
            bool:
              Булевый результат на корректность
        """
        pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
        if type(address) != str:
            return False
        if re.match(pattern, address):
            return True
        return False

    def check_type_int(number) -> bool:
        """
          Выполняет проверку типа данных параметра
          Если пераметр не имеет тип данных int то возвращено False

          Параметры
          ---------
            number:
              Параметр для проверки типа данных

          Return
          ------
            bool:
              Булевый результат на корректность
        """
        if type(number) == int:
            return True
        return False

    def check_type_string(string) -> str:
        """
          Выполняет проверку типа данных параметра
          Если пераметр не имеет тип данных str возвращено False

          Параметры
          ---------
            string:
              Параметр для проверки типа данных

          Return
          ------
            bool:
              Булевый результат на корректность
        """
        if type(string) != str:
            return False
        return True


data = json.load(open(args.input, encoding='windows-1251'))

true_data = list()
email = 0
height = 0
passport = 0
address = 0
age = 0
inn = 0
occupation = 0
worldview = 0
political_view = 0
with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not Validator.check_email(person['email']):
            email += 1
            temp = False
        if not Validator.check_height(person['height']):
            height += 1
            temp = False
        if not Validator.check_inn(person['inn']):
            inn += 1
            temp = False
        if not Validator.check_passport(person['passport_number']):
            passport += 1
            temp = False
        if not Validator.check_address(person["address"]):
            address += 1
            temp = False
        if not Validator.check_type_int(person['age']):
            age += 1
            temp = False
        if not Validator.check_type_string(person['occupation']):
            occupation += 1
            temp = False
        if not Validator.check_type_string(person['political_views']):
            political_view += 1
            temp = False
        if not Validator.check_type_string(person['worldview']):
            worldview += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

out_put = open(args.output, 'w', encoding='utf-8')
valid_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out_put.write(valid_data)
out_put.close()

print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидных записей: {len(data) - len(true_data)}')
print(f'  - Число невалидных email:  {email}')
print(f'  - Число невалидного роста: {height}')
print(f'  - Число невалидных ИНН: {inn}')
print(f'  - Число невалидных номеров паспорта: {passport}')
print(f'  - Число невалидных профессий: {occupation}')
print(f'  - Число невалидных возрастов: {age}')
print(f'  - Число невалидных политических взглядов: {political_view}')
print(f'  - Число невалидных мировоззрений: {worldview}')
print(f'  - Число невалидных адресов: {address}')

#python main.py 95.txt valid.txt
