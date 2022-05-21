from colorama import Back

class paddle:
    def __init__(duck):
        duck.size = 10
        duck.x = 46

    def render(duck):
        block = duck.x * [" "] + [Back.WHITE + "-"] + \
            (duck.size-1) * ["-"] + [Back.RESET + " "] + \
                (101 - duck.size - duck.x) * [" "]
        #color = duck.x * [Back.RESET] + duck.size * [Back.WHITE] + \
                #(102 - duck.size - duck.x) * [Back.RESET]
        return block #, color
