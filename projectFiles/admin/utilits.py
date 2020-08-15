from models import User, Vister


def count1():
    i = 0
    mens = User.query.filter_by(gender="زول").all()
    if mens:
        for man in mens:
            i = i + 1
        return i
    else:
        return 0

def count2():
    y = 0
    womens = User.query.filter_by(gender="زولة").all()
    if womens:
        for women in womens:
            y = y + 1
        return y
    else:
        return 0


def cont3():
    users = User.query.order_by(User.name).all()
    i = 0
    if users:
        for user in users:
            i = i + 1
        return i
    else:
        return 0


def cont4():
    ips = Vister.query.order_by(Vister.ip).all()
    i = 0
    if ips:
        for ip in ips:
            i = i + 1
        return i
    else:
        return 0