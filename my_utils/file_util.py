def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("123.txt")
    append_to_file("123.txt","12345")