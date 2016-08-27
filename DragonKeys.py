import libtcodpy


if __name__ == '__main__':
    from Panel import Panel
    from Console import Console
    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 25
    con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'test')
    pan = Panel(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    testkey = getattr(libtcodpy, 'KEY_UP')
    print(testkey)
    if testkey == libtcodpy.KEY_UP:
        print('true')
    while not con.is_window_closed:
        con.clear
        key = libtcodpy.console_check_for_keypress(True)
        if key.vk != libtcodpy.KEY_NONE:
            if key.vk != libtcodpy.KEY_CHAR:
                pan.clear
                pan.write(0, 0, str(key.vk))
            else:
                pan.clear
                pan.write(0, 0, chr(key.c))
        if key.vk == libtcodpy.KEY_ESCAPE:
            break
        pan.blit()
        con.flush
