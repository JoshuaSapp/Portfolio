"""
 CSE212
 (c) BYU-Idaho
 03-Teach - Problem 2

 It is a violation of BYU-Idaho Honor Code to post or share this code with others or
 to post it online. Storage into a personal and private repository (e.g. private
 GitHub repository, unshared Google Drive folder) is acceptable.
"""

def do_something_complicated(line):
    stack = []
    for item in line:
        if item == '(' or item == '[' or item == '{':
            stack.append(item)
        elif item == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif item == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif item == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
    return len(stack) == 0

print(do_something_complicated('(a == 3 or (b == 5 and c == 6))'))
print(do_something_complicated('(students]i].grade > 80 and students[i].grade < 90)'))
print(do_something_complicated('(robot[id + 1].execute(.pass() or (not robot[id * (2 + i)].alive and stormy) or (robot[id - 1].alive and lava_flowing))'))

#true
#false
#false