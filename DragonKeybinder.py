import libtcodpy
import DragonKeys
from Panel import Panel
from Console import Console


class txtbtn:
    def __init__(self, x, y, txt):
        self.x = x
        self.y = y
        self.txt = txt
        self.h = 3

    @property
    def tx(self):
        return self.x + 1

    @property
    def ty(self):
        return self.y + 1

    @property
    def w(self):
        return len(self.txt) + 2

    @property
    def x2(self):
        return self.x + self.w - 1

    @property
    def y2(self):
        return self.y + self.h - 1


binding = DragonKeys.KeyHandler()
binding.load('Keybindings/test.csv')
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TEXT_WIDTH = SCREEN_WIDTH - 1
TEXT_HEIGHT = SCREEN_HEIGHT - 6
NEW_BTN = txtbtn(0, 0, 'New')
LOAD_BTN = txtbtn(NEW_BTN.x2 + 1, 0, 'Load')
SAVE_BTN = txtbtn(LOAD_BTN.x2 + 1, 0, 'Save')
SAVE_AS_BTN = txtbtn(SAVE_BTN.x2 + 1, 0, 'Save As')
con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'DragonKeybinder')
filepanel = Panel(0, 0, SCREEN_WIDTH, 3)
textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT)
workpanel = Panel(1, 1, TEXT_WIDTH - 2, TEXT_HEIGHT - 2)
bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, 1)
buttonpanel = Panel(0, SCREEN_HEIGHT - 3, SCREEN_WIDTH, 3)
scrollpanel = Panel(SCREEN_WIDTH - 1, 3, 1, SCREEN_HEIGHT - 6)
mouse = libtcodpy.Mouse()
key = libtcodpy.Key()
while not con.is_window_closed:
    con.clear
    filepanel.clear
    workpanel.clear
    textpanel.clear
    buttonpanel.clear
    scrollpanel.clear
    bindingspanel.clear
    filepanel.rect(NEW_BTN.x, NEW_BTN.y, NEW_BTN.w, NEW_BTN.h, False)
    filepanel.write(NEW_BTN.tx, NEW_BTN.ty, NEW_BTN.txt)
    filepanel.rect(LOAD_BTN.x, LOAD_BTN.y, LOAD_BTN.w, LOAD_BTN.h, False)
    filepanel.write(LOAD_BTN.tx, LOAD_BTN.ty, LOAD_BTN.txt)
    if binding.active:
        filepanel.rect(SAVE_BTN.x, SAVE_BTN.y, SAVE_BTN.w, SAVE_BTN.h, False)
        filepanel.write(SAVE_BTN.tx, SAVE_BTN.ty, SAVE_BTN.txt)
        filepanel.rect(
            SAVE_AS_BTN.x, SAVE_AS_BTN.y, SAVE_AS_BTN.w, SAVE_AS_BTN.h, False)
        filepanel.write(SAVE_AS_BTN.tx, SAVE_AS_BTN.ty, SAVE_AS_BTN.txt)
        filepanel.rect(
            SAVE_AS_BTN.x2 + 1, 0, SCREEN_WIDTH - SAVE_AS_BTN.x2 - 1, 3, False)
        filepanel.write(SAVE_AS_BTN.x2 + 2, 1, binding.active_bindings)
    else:
        filepanel.rect(
            LOAD_BTN.x2 + 1, 0, SCREEN_WIDTH - LOAD_BTN.x2, 3, False)
    textpanel.rect(0, 0, TEXT_WIDTH, TEXT_HEIGHT, False)
    addbtntxt = 'Add Binding'
    btntxtx = 1
    buttonpanel.rect(0, 0, len(addbtntxt) + 2, 3, False)
    buttonpanel.write(btntxtx, 1, addbtntxt)
    btntxtx = btntxtx + len(addbtntxt) + 1
    rmvbtntxt = 'Remove Binding'
    buttonpanel.rect(btntxtx, 0, len(rmvbtntxt) + 2, 3, False)
    btntxtx = btntxtx + 1
    buttonpanel.write(btntxtx, 1, rmvbtntxt)
    newbtntxt = 'New Output'
    buttonpanel.rect(SCREEN_WIDTH - len(newbtntxt) - 2, 0,
                     len(newbtntxt) + 2, 3, False)
    buttonpanel.write(SCREEN_WIDTH - len(newbtntxt) - 1, 1, newbtntxt)
    scrollpanel.write(0, 0, '^')
    scrollpanel.write(0, TEXT_HEIGHT - 1, 'v')
    libtcodpy.sys_check_for_event(libtcodpy.EVENT_KEY_PRESS |
                                  libtcodpy.EVENT_MOUSE,
                                  key, mouse)
    bindingspanel.write(0, 0, str((mouse.cx, mouse.cy)))
    filepanel.blit()
    bindingspanel.blit(dst=workpanel.body)
    workpanel.blit(dst=textpanel.body)
    textpanel.blit()
    buttonpanel.blit()
    scrollpanel.blit()
    con.flush
