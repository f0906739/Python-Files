# try:
#     test = open("demo.txt", "w")
#     test.write("I remember now!")
# except Exception as e:
#     print("[EXCEPTION]", e)
# finally:
#     test.close()


import csv


def log(func):
    def wrapper(*args, **kwargs):
        no_args = len(args) == 0
        no_kwargs = len(kwargs) == 0

        if no_args and no_kwargs:
            print(func.__name__)
        elif no_args == False and no_kwargs == False:
            print(func.__name__, args, kwargs)
        elif no_args:
            print(func.__name__, kwargs)
        elif no_kwargs:
            print(func.__name__, args)
        return func(*args, **kwargs)
    return wrapper


# Note: column number starts at 0.
with open("names.csv", "r") as c:
    reader = csv.reader(c)
    next(reader)

    @log
    def after_fieldnames():
        c.seek(0)
        next(reader)

    @log
    def find_max_length(column):
        after_fieldnames()

        column_lengths = [len(line[column]) for line in reader]
        return max(column_lengths)

    FIRSTLENGTH = find_max_length(column=0)
    SECONDLENGTH = find_max_length(column=1)

    @log
    def separate_cell(column, text):
        if column == 0:
            max_length = FIRSTLENGTH
        if column == 1:
            max_length = SECONDLENGTH

        text_length = len(text)
        MIN_NUM_SPACES = 3
        num_of_spaces = max_length-text_length+MIN_NUM_SPACES

        spaces = " "*num_of_spaces
        text_then_spaces = text+spaces
        return text_then_spaces

    @log
    def formatted_csv():
        after_fieldnames()

        for line in reader:
            first_name, last_name, email = line
            new_line = separate_cell(0, first_name) + separate_cell(1, last_name)+email+"\n"
            yield new_line

    with open("randomtxtfile.txt", "w") as w:
        for line in formatted_csv():
            w.write(line)

    # c.seek(0)
    # next(reader)
    # with open("newNames.csv", "w", newline="") as w:
    #     writer = csv.writer(w, delimiter=",")
    #     for line in reader:
    #         writer.writerow(line)
