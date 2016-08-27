import libtcodpy


if __name__ == '__main__':
    SCREEN_WIDTH = 50
    SCREEN_HEIGHT = 50
    libtcodpy.console_set_custom_font('terminal12x12_gs_ro.png',
                                      libtcodpy.FONT_TYPE_GREYSCALE |
                                      libtcodpy.FONT_LAYOUT_ASCII_INROW)
    libtcodpy.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,
                                'basicroguelike', False)
    libtcodpy.sys_set_fps(60)
    con = libtcodpy.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    testkey = getattr(libtcodpy, 'KEY_UP')
    print(testkey)
    if testkey == libtcodpy.KEY_UP:
        print('true')

    key = libtcodpy.Key()
    mouse = libtcodpy.Mouse()
    while not libtcodpy.console_is_window_closed():
        libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                      libtcodpy.EVENT_MOUSE, key, mouse)
        if key.vk != libtcodpy.KEY_NONE:
            if key.vk != libtcodpy.KEY_CHAR:
                print('not a char')
            else:
                print(chr(key.c))
