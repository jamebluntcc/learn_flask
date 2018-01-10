# coding=utf-8
from werkzeug.utils import secure_filename
# cached_property

class Foo(object):
    @cached_property
    def bar(self):
        return 1

# secure_filename

if __name__ == '__main__':
    foo = Foo()
    foo.bar
    print foo.bar
    print secure_filename('haha name.py')
