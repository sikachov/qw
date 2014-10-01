__author__ = 'evgeny'

i=open("inp")
o=open("out",'w')

def count_char():
    count=0
    for l in i.readlines():
        count+=len(l)
    return count

it=iter(range(count_char()))

def fun():
    c=i.read(it.next())
    o.write(c)

fun()
print count_char()

i.close()
o.close()