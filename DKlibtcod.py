import libtcodpy


def wait_key(self, flush=True):
    key = libtcodpy.console_wait_for_keypress(flush)
    return _interpret_key(key)


def check_key(self):
    key = libtcodpy.console_check_for_keypress()
    return _interpret_key(key)


def _interpret_key(self, key):
    if key.vk == libtcodpy.KEY_CHAR:
        return chr(key.c)
    else:
        return str(key.vk)
