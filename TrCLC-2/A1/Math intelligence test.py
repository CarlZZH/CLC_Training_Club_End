# -*- coding:UTF-8 -*-
import random

ques_answer = 'QA.txt'
ques_no_answer = 'QNA.txt'

m1 = open(ques_answer, 'w')
m2 = open(ques_no_answer, 'w')

for row in range(20):
    for col in range(5):
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        op = (random.randint(1, 20180805)) % 4
        if op == 0:
            c = a + b
            op_str = '+'
        elif op == 1:
            c = a - b
            op_str = '-'
        elif op == 2:
            c = a * b
            op_str = 'x'
        elif op == 3:
            c = a / b
            op_str = '/'

        questions = '%2d %s %2d=\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' % (a, op_str, b)
        questions_a = '%2d %s %2d=%0.2f\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' % (a, op_str, b, c)
        m1.write(questions_a)
        m2.write(questions)
    m1.write('\n')
    m2.write('\n')
    #print('%s\t' % question,end='')
    # print('\n')

m1.close()
m2.close()
