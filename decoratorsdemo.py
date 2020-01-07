def warn_3_strikes(question_func, count=None):
    is_4 = None
    not_4 = None

    def update_with_count():
        nonlocal count, is_4, not_4
        count += 1
        is_4 = count == 4
        not_4 = count != 4

    update_with_count()
    if not_4:
        print("Error, answer inputted does not follow the directions given.")
        print(f"STRIKE {count}")
        question_func(count)
    if is_4:
        raise ValueError()


def ask_if_eiffel_tall(repeats=0):
    QUESTION = "Is the Eiffel Tower tall? "
    answer = str(input(QUESTION)).lower()
    is_yes = answer == "y"
    is_no = answer == "n"
    unanswered = is_yes == False and is_no == False

    if unanswered:
        warn_3_strikes(ask_if_eiffel_tall, count=repeats)
    if is_yes:
        return "CORRECT!!! the Eiffel Tower is in fact very tall!"
    if is_no:
        return "wrong, it's FACT that the Eiffel Tower is tall. Sorry, scrub."


print(ask_if_eiffel_tall())