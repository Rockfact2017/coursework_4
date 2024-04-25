from pprint import pprint

from providers import HH, Vacancy

def main():
    user_input = input('Введите ваш запрос')
    vacs = HH().fetch_data(user_input)
    vacs = sorted(vacs, reverse=True)
    user_input = int(input('Введите колличество для отображения'))

    pprint(vacs[:user_input])
    Vacancy.save_to_json(vacs)


if __name__ == '__main__':
    main()