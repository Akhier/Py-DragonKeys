import libtcodpy


def wait_key(self, flush=True):
    return libtcodpy.console_wait_for_keypress(flush)


def check_key(self):
    return libtcodpy.console_check_for_keypress()
