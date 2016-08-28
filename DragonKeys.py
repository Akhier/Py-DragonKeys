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
                for binding, output in self._bindingdict.iteritems():
                    writer.writerow(binding, output)
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


if __name__ == '__main__':
    from Panel import Panel
    from Console import Console
    testbinding = KeyHandler()
    testbinding.load('test.csv')
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
        pan.clear
        pan.write(0, 0, testbinding.wait_keypress())
        pan.blit()
        con.flush
