calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return(calls)

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    res = False
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower():
            res = True
    return res
print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))
print(is_contains("cycle", ["recycling", "cyclic"]))
print(calls)