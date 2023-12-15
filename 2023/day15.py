# from collections import deque

line = open('input.txt').read().split(',')


def hasher(step):
    current = 0
    for letter in step:
        current += ord(letter)

        current = current*17

        current = current%256

        
    return current

def generate_boxes():
    boxes = dict()
    for i in range(256):
        boxes[i] = []
    return boxes

boxes = generate_boxes()


def dash(step, boxes):
    label = step[:-1]
    box = hasher(label)
    for i,item in enumerate(boxes[box]):
        if item.split()[0] == label:
            boxes[box].pop(i)
            return boxes
    return boxes


def equal(step, boxes):
    label, focal_len = step.split('=')
    box = hasher(label)
    lens = f'{label} {focal_len}'
    for i,item in enumerate(boxes[box]):
        if item.split()[0] == label:
            boxes[box].pop(i)
            boxes[box].insert(i, lens)
            return boxes
    boxes[box].append(lens)
    return boxes



def arrange(line,boxes):
    for step in line:
        if '=' in step:
            boxes = equal(step, boxes)
        elif '-' in step:
            boxes = dash(step, boxes)
    return boxes

def calc(boxes):
    foc_pow = 0
    for box in boxes:
        for i,lens in enumerate(boxes[box]):
            foc_pow += (box+1) * ((i+1)*int(lens.split()[1]))
            # print(lens,foc_pow)
    return foc_pow

boxes = arrange(line, boxes)
print(calc(boxes))
