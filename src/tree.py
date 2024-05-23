
def create_tree(levels, path):
    max_symbols = 1 + levels * 4

    def centered_line(string):
        count_of_spaces = (max_symbols - len(string)) // 2
        return f"{' ' * count_of_spaces}{string}\n"

    with open(path, 'w') as file:
        file.write(centered_line('W'))
        file.write(centered_line('*'))  # Better than i != 0

        for i in range(1, levels):
            string = '*' + '*' * 4 * i
            if i % 2 == 0:
                string = f' {string}@'
            else:
                string = f'@{string}'

            file.write(centered_line(string))

        file.write(centered_line('TTTTT'))
        file.write(centered_line('TTTTT'))

def interface():
    print("Введите количество 'этажей' у ёлки")
    levels = int(input())
    print("Введите path и filename.txt")
    path = str(input())
    create_tree(levels, path)

if __name__ == '__main__':
    interface()