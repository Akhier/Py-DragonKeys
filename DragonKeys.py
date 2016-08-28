import libtcodpy
import os.path
import csv


class KeyHandler:
    def __init__(self):
        self._bindingname = ''
        self._bindingpath = ''
        self._bindingdict = {}
        self._active = False

    @property
    def active_bindings(self):
        return self._bindingname

    def _clear(self):
        self._bindingname = ''
        self._bindingpath = ''
        self._bindingdict = {}

    def load(self, csvpath):
        if not os.path.isfile(csvpath):
            return False
        else:
            self._clear()
            outputdict = {}
            with open(csvpath) as file:
                reader = csv.reader(file)
                for entry in reader:
                    outputdict[entry[0]] = entry[1]
            self._bindingdict = outputdict
            self._bindingpath = csvpath
            csvpath = csvpath.replace('/', '.').replace('\\', '.')
            temp = csvpath.lower().split('.')
            self._bindingname = csvpath.split('.')[temp.index('csv') - 1]
            self._active = True

    def save_as(self, name):
        if self._active:
            path = name + '.csv'
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                for key, output in self._bindingdict.iteritems():
                    writer.writerow(key, output)
                self._bindingname = name
                self._bindingpath = path

    def save(self):
        self.save_as(self._bindingname)

    def new(self, name, defaultouptut):
        self._clear()
        self._bindingdict['DEFAULT'] = defaultouptut
        self.save_as(name)
        self._active = True

    def check_keypress(self):
        key = libtcodpy.console_check_for_keypress(True)
        if key.vk == libtcodpy.KEY_NONE:
            return self._bindingdict['DEFAULT']
        else:
            if key.vk == libtcodpy.KEY_CHAR:
                keychar = chr(key.c)
                if keychar in self._bindingdict:
                    return self._bindingdict[keychar]
                else:
                    return self._bindingdict['DEFAULT']
            else:
                keystr = str(key.vk)
                if keystr in self._bindingdict:
                    return self._bindingdict[keystr]
                else:
                    return self._bindingdict['DEFAULT']

    def wait_keypress(self):
        key = libtcodpy.console_wait_for_keypress(True)
        if key.vk == libtcodpy.KEY_CHAR:
            keychar = chr(key.c)
            if keychar in self._bindingdict:
                return self._bindingdict[keychar]
            else:
                return self._bindingdict['DEFAULT']
        else:
            keystr = str(key.vk)
            if keystr in self._bindingdict:
                return self._bindingdict[keystr]
            else:
                return self._bindingdict['DEFAULT']

    def add_specified_binding(self, key, output):
        self._bindingdict[key] = output

    def add_binding(self, output):
        key = libtcodpy.console_wait_for_keypress(True)
        if key.vk == libtcodpy.KEY_CHAR:
            keychar = chr(key.c)
            self.add_specified_binding(keychar, output)
        else:
            keystr = str(key.vk)
            self.add_specified_binding(keystr, output)

    def remove_specified_binding(self, key):
        self._bindingdict.pop(key, None)

    def remove_binding(self):
        key = libtcodpy.console_wait_for_keypress(True)
        if key.vk == libtcodpy.KEY_CHAR:
            keychar = chr(key.c)
            self.remove_specified_binding(keychar)
        else:
            keystr = str(key.vk)
            self.remove_specified_binding(keystr)


if __name__ == '__main__':
    from Panel import Panel
    from Console import Console
    testbinding = KeyHandler()
    testbinding.load('test.csv')
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    TEXT_WIDTH = SCREEN_WIDTH - 1
    TEXT_HEIGHT = SCREEN_HEIGHT - 6
    con = Console(SCREEN_WIDTH, SCREEN_HEIGHT, 'test')
    filepanel = Panel(0, 0, SCREEN_WIDTH, 3)
    textpanel = Panel(0, 3, TEXT_WIDTH, TEXT_HEIGHT)
    buttonpanel = Panel(0, SCREEN_HEIGHT - 3, SCREEN_WIDTH, 3)
    scrollpanel = Panel(SCREEN_WIDTH - 1, 3, 1, SCREEN_HEIGHT - 4)
    while not con.is_window_closed:
        con.clear
        filepanel.clear
        textpanel.clear
        buttonpanel.clear
        scrollpanel.clear
        filepanel.rect(0, 0, SCREEN_WIDTH, 3, False)
        filepanel.write(1, 1, 'New')
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
        scrollpanel.write(0, 0, '^')
        scrollpanel.write(0, TEXT_HEIGHT - 1, 'v')
        filepanel.blit()
        textpanel.blit()
        buttonpanel.blit()
        scrollpanel.blit()
        con.flush
        testbinding.wait_keypress()
