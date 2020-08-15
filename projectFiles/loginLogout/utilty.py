import random
import uuid
from models import User

def choes(gender):
    men = list(range(1, 24))
    women = list(range(1, 30))
    if gender == "زول":
        image = random.choice(men)
        return image
    if gender == "زولة":
        image = random.choice(women)
        return image


def newLink():
    newLink = uuid.uuid1().hex
    query = User.query.filter_by(proLink=newLink).first()
    if query:
        newLink = uuid.uuid1().hex
        return newLink
    return newLink