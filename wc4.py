def sed(string_pattern, string_replacement, input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        jaygzin = text.replace(string_pattern, string_replacement)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(jaygzin)
        print("عملیات با موفقیت انجام شد ")
    except FileNotFoundError:
        print("فایل وجود ندارد ")
    except IOError:
        print("خطا ورودی خروجی")
    except Exception:
        print("خطا")