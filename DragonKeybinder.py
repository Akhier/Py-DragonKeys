import DragonKeys
from Panel import Panel
from Console import Console


binding = DragonKeys.KeyHandler()
binding.load('Keybindings/test.csv')
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TEXT_WIDTH = SCREEN_WIDTH - 1
TEXT_HEIGHT = SCREEN_HEIGHT - 6
con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'DragonKeybinder')
filepanel = Panel(0, 0, SCREEN_WIDTH, 3)
textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT)
workpanel = Panel(1, 1, TEXT_WIDTH - 2, TEXT_HEIGHT - 2)
bindingspanel = Panel(0, 0, TEXT_WIDTH - 2, 1)
buttonpanel = Panel(0, SCREEN_HEIGHT - 3, SCREEN_WIDTH, 3)
scrollpanel = Panel(SCREEN_WIDTH - 1, 3, 1, SCREEN_HEIGHT - 6)
while not con.is_window_closed:
    con.clear
    filepanel.clear
    workpanel.clear
    textpanel.clear
    buttonpanel.clear
    scrollpanel.clear
    filestr = '\n New  Load'
    if binding.active:
        filestr += '  Save  Save As  ' + binding.active_bindings
        filepanel.write(0, 0, filestr)
        filepanel.rect(11, 0, 6, 3, False)
        filepanel.rect(17, 0, 9, 3, False)
        filepanel.rect(26, 0, SCREEN_WIDTH - 26, 3, False)
    else:
        filepanel.write(0, 0, filestr)
        filepanel.rect(11, 0, SCREEN_WIDTH - 11, 3, False)
    filepanel.rect(0, 0, 5, 3, False)
    filepanel.rect(5, 0, 6, 3, False)
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
    filepanel.blit()
    workpanel.blit(dst=textpanel.body)
    textpanel.blit()
    buttonpanel.blit()
    scrollpanel.blit()
    con.flush
    binding.wait_keypress()
