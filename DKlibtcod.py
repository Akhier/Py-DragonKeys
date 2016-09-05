# By Akhier Dragonheart
import libtcodpy


def wait_keypress(flush=True):
    key = libtcodpy.console_wait_for_keypress(flush)
    return _interpret_key(key)


def check_keypress():
    key = libtcodpy.Key()
    mouse = libtcodpy.Mouse()
    libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                  libtcodpy.EVENT_MOUSE,
                                  key, mouse)
    return _interpret_key(key)


def _interpret_key(key):
    if key.vk == libtcodpy.KEY_CHAR:
        return chr(key.c)
    else:
        return str(key.vk)
