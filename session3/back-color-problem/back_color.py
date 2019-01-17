import random 

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    t = random.randint(0,3)
    a = random.randint(0,3)
    return  [shapes[t]['text'].upper(),shapes[a]['color'],random.randint(0, 1)]

import sys
sys.path.append(r'E:\python\Labs\session3\homework')

from is_inside_game import is_inside
def mouse_press(x, y, text, color, quiz_type):
    for  check in shapes:
        if quiz_type == 0:
            if check['text'] == text.lower():
                click = is_inside([x, y], check['rect'])
        else:
            if check['color'] == color:
                click = is_inside([x, y], check['rect'])
    return click
