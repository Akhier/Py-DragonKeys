import libtcodpy
from Panel import Panel
from Console import Console


if __name__ == '__main__':
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'test')
    pan = Panel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    testkey = getattr(libtcodpy, 'KEY_UP')
    print(testkey)
    if testkey == libtcodpy.KEY_UP:
        print('true')

    key = libtcodpy.Key()
    mouse = libtcodpy.Mouse()
    while not con.is_window_closed:
        con.clear
        libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                      libtcodpy.EVENT_MOUSE, key, mouse)
        if key.vk != libtcodpy.KEY_NONE:
            if key.vk != libtcodpy.KEY_CHAR:
                pan.clear
                pan.write(0, 0, 'test')
            else:
                pan.clear
                pan.write(0, 0, chr(key.c))
        pan.blit()
        con.flush
