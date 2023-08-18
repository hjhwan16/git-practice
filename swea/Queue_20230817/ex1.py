# 선형 큐

def enQ(data):
    global rear
    if rear == Qsize-1:
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data

def deQ():
    global front
    if front == rear:
        print('Q is Empty')
        return -1
    else:
        front += 1
        return Q[front]



Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

enQ(1)
enQ(2)