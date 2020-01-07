# stops program if user fails more than 3 times
def WarnThreeStrikes(question_func, count=None):

    ERROR_MSG = "Error, answer inputted does not follow the directions given."

    def update_with_count():

        nonlocal update_with_count
        count += 1

    update_with_count()
    if count != 4:
        print(ERROR_MSG)
        print(f"STRIKE {count}")
        return question_func(count)
    if count == 4:
        raise ValueError()

# asks yes or no question
def ask_if_eiffel_tall(repeats=0):

    QUESTION = "Is the Eiffel Tower tall? ('y' or 'n'): "
    INSULT_MSG = "wrong, it's FACT that the Eiffel Tower is tall. Sorry, scrub."
    CONGRATULATE_MSG = "CORRECT!!! the Eiffel Tower is in fact VERY tall!"
    answer = str(input(QUESTION)).lower()
    unanswered = answer != "n" and answer != "y"

    if unanswered:
        return WarnThreeStrikes(ask_if_eiffel_tall, count=repeats)
    if answer == "y":
        return CONGRATULATE_MSG
    if answer == "n":
        return INSULT_MSG


print(ask_if_eiffel_tall())
