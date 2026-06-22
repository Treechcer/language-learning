import basic

while True:
    text = input("basic > ")
    # Found it annoying to press ctrl c, so I've made this
    if text == "q":
        exit()
    result, err = basic.run("<stdin>", text)

    if err: print(err.as_string())
    else: print(result)