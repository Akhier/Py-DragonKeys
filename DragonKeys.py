# By Akhier Dragonheart
from DKlibtcod import *
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

    @property
    def active(self):
        return self._active

    @property
    def dict(self):
        return self._bindingdict

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
            path = 'Keybindings/' + name + '.csv'
            with open(path, 'w') as file:
                writer = csv.writer(file, lineterminator='\n')
                for key, output in self._bindingdict.iteritems():
                    writer.writerow((key, output))
                self._bindingname = name
                self._bindingpath = path

    def save(self):
        self.save_as(self._bindingname)

    def new(self, name, defaultouptut):
        self._clear()
        self._bindingdict['DEFAULT'] = defaultouptut
        self._active = True
        self.save_as(name)

    def check_key(self, key):
        if key in self._bindingdict:
            return self._bindingdict[key]
        else:
            return self._bindingdict['DEFAULT']

    def check_keypress(self):
        key = check_key()
        return self.check_key(key)

    def wait_keypress(self):
        key = wait_key()
        if key in self._bindingdict:
            return self._bindingdict[key]
        else:
            return self._bindingdict['DEFAULT']

    def add_specified_binding(self, key, output):
        self._bindingdict[key] = output

    def add_binding(self, output):
        key = wait_key()
        self.add_specified_binding(key, output)

    def remove_specified_binding(self, key):
        self._bindingdict.pop(key, None)

    def remove_binding(self):
        key = wait_key()
        self.remove_specified_binding(key)
