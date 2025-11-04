row_length = 20
file1_name="TF11_1.txt"
file2_name="TF11_2.txt"
def creat_file(file_name,length):
    print(f"Створення файлу'{file_name}'")
    try:
        # Символьні рядки різної довжини
        data=[
            "ряядокзцифрами123",
            "я люблю пайтон 31",
            "text_11111",
            "1234567890abcdefghijK",
            "42"
        ]
        # with ддя атоматичного відкриття та закриття файла
        with open(file_name,"w",encoding="utf-8") as f:
            for line in data:
                formatted_line=line.ljust(length)[:length]# ljust(length) доповнює пробілами до length, [:length] обрізає, якщо рядок занадто довгий
                f.write(formatted_line+'\n')
        print(f"Файл '{file_name}' створено з {len(data)} рядками")
    except IOError as e:
        print(f"Помилка при створенні файлу '{file_name}': {e}")
    except Exception as e:
        print(f"Виникла несподівана помилка:{e}")
def process_files(file_in, file_out, length):
    print(f"Обробка файлу {file_in} та запис у {file_out}")
    try:
        with open(file_in,"r",encoding="utf-8") as f_in:
            lines=f_in.readlines()
        process_lines=[]
        for line in lines:
            # line.strip() видаляє пробіли та \n
            # "".join(...) збирає символи, якщо char.isdigit() повертає True
            digits_only="".join(char for char in line.strip() if char.isdigit())
            formatted_line=digits_only.ljust(length)[:length]# Доповнюємо рядок пробілами до заданої довжини
            process_lines.append(formatted_line)
        with open(file_out,"w",encoding="utf-8") as f_out:
            for line in process_lines:
                f_out.write(line+'\n')
        print(f"Файл '{file_out}' створено та оброблено")

    except FileNotFoundError:
        print(f"Помилка: Файл '{file_in}' не знайдено.")
    except IOError as e:
        print(f"Помилка читання/запису файлів: {e}")
    except Exception as e:
        print(f"Виникла помилка при обробці: {e}")

def print_file_content(filename):
    print(f"Друкує вміст файлу {filename}")
    try:
        with open(filename,"r",encoding="utf-8") as f:
            content=f.read()
            print(content.strip())# strip() видаляє зайві пробіли/нові рядки на кінцях
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено")
    except IOError as e:
        print(f"Помилка читання файлу: {e}")
def main():
    creat_file(file1_name,row_length)
    process_files(file1_name,file2_name,row_length)
    print_file_content(file2_name)
main()