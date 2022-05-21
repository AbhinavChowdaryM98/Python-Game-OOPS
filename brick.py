from colorama import Back

c = [Back.GREEN, Back.YELLOW, Back.RED, Back.WHITE]


class brick:
    def __init__(duck, score, x, y):
        duck.x = x
        duck.y = y
        duck.score = score

    def render(duck):
        if duck.score:
            return [c[duck.score-1]+'#', '#' ,'#' +Back.RESET]
        return 3*[' ']