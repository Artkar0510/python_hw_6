def main():
    word = input("Введите слово из латинских букв: ")
    length = len(word)
    if length % 2 == 0:
        # Если четное число букв - две средние буквы
        mid = length // 2
        result = word[mid-1:mid+1]
    else:
        # Если нечетное число букв - одна средняя буква
        mid = length // 2
        result = word[mid]
    print(result)

if __name__ == "__main__":
    main()