import signal

class AlarmException(Exception):
    """This class executes the alarmexception."""
    pass


class _getChUnix:

    def __init__(duck):
        """init def to take input"""
        import tty
        import sys

    def __call__(duck):
        """def to call function"""
        import sys
        import tty
        import termios
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return charvar


def alarmhandler(signum, frame):
    """ input method """
    raise AlarmException


def user_input(timeout=0.15):
    """ input method """
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)

    try:
        text = _getChUnix()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return '.'