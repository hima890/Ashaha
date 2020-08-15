import random

def choce():
    images = list(range(1, 30))
    image = random.choice(images)
    print(image)
    return image