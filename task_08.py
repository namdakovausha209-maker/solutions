def century_message(name, age, current_year):
    a = current_year + (100 - age)
    return (f"{name}, тебе исполнится 100 лет в {a} году")

if __name__ == "__main__":
    print(century_message("Аня", 20, 2025))
