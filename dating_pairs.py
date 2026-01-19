def main(boys, girls):
    if len(boys) != len(girls):
        print('Внимание, кто-то может остаться без пары!')
    else:
        boys_sorted = sorted(boys)
        girls_sorted = sorted(girls)
        print('Идеальные пары:')
        for boy, girl in zip(boys_sorted, girls_sorted):
            print(f'{boy} и {girl}')

if __name__ == "__main__":
    boys_input = input("Введите имена мальчиков через пробел: ")
    girls_input = input("Введите имена девочек через пробел: ")
    boys = boys_input.split()
    girls = girls_input.split()
    main(boys, girls)