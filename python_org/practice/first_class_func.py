def html_tag(tag):
    def wrap_text(msg):
        print('<{0}><{1}><{0}>'.format(tag, msg))
    return wrap_text


h1 = html_tag('h1')
h1('Some Text')
h1('Some more Text')
p1 = 50

print(h1.__name__)
print(p1.__doc__)
