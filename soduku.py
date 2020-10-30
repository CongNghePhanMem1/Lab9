import random
random.seed(51801019)
random.randint(1, 4)
class ClassCuaTao:
    def __init__(self):
        self.th = list()
    def toHop(self, a, l, r):
        if l == r: 
            print(a)
            a = list(a)
            self.th.append(a)
        else: 
            for i in range(l, r + 1): 
                a[l], a[i] = a[i], a[l] 
                self.toHop(a, l+1, r) 
                a[l], a[i] = a[i], a[l]
th = ClassCuaTao()
mang = [0, 1, 2] 
th.toHop(mang, 0, len(mang) - 1)
arr = [[], [], []]
prev_square = []
for z in range(9):
    run = True
    while run:
        tmp = []
        for i in range(3):
            isStack = 1
            while (isStack == 1):
                isStack = 0 # Bien co hieu
                choice = random.choice(th.th) 
                if len(tmp) > 0: # Check xem arr co phan tu nao khong
                    for ele in tmp:
                        if choice[0] == ele[0] or choice[1] == ele[1] or choice[2] == ele[2]: # Kiem tra hang va cot
                            isStack = 1
                            continue

            tmp.append(choice)
        run = False
        if prev_square == []:
            prev_square.append(tmp)
        else:
            for e in prev_square:
                if tmp == e:
                    run = True
                    break
            prev_square.append(tmp)
                    
    arr[0] += tmp[0]
    arr[1] += tmp[1]
    arr[2] += tmp[2]
len(arr[0]), len(arr[1]), len(arr[2])
# Change from shape 27 27 27 to 9 9 9
new_arr = []
for i in range(1, 4):
    new_arr.append(arr[0][(i-1)*9:i*9])
    new_arr.append(arr[1][(i-1)*9:i*9])
    new_arr.append(arr[2][(i-1)*9:i*9])

# 3x3
outer = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]
for i in range(3):
    for j in range(3):
        # First three element in 3 x 3
        new_arr[i*3][j*3] = outer[i][j]*3+new_arr[i*3][j*3]+1
        new_arr[i*3][1 + j*3] = outer[i][j]*3+new_arr[i*3][1 + j*3]+1
        new_arr[i*3][2 + j*3] = outer[i][j]*3+new_arr[i*3][2 + j*3]+1
        # Second three element in 3 x 3
        new_arr[i*3 + 1][j*3] = outer[i][j]*3+new_arr[i*3 + 1][j*3]+1
        new_arr[i*3 + 1][1 + j*3] = outer[i][j]*3+new_arr[i*3 + 1][1 + j*3]+1
        new_arr[i*3 + 1][2 + j*3] = outer[i][j]*3+new_arr[i*3 + 1][2 + j*3]+1
        # Third three element in 3 x 3
        new_arr[i*3 + 2][j*3] = outer[i][j]*3+new_arr[i*3 + 2][j*3]+1
        new_arr[i*3 + 2][1 + j*3] = outer[i][j]*3+new_arr[i*3 + 2][1 + j*3]+1
        new_arr[i*3 + 2][2 + j*3] = outer[i][j]*3+new_arr[i*3 + 2][2 + j*3]+1
# Swap the rows
# Row 2nd and 4th
new_arr[1], new_arr[3] = new_arr[3], new_arr[1]
# Row 3rd and 7th
new_arr[2], new_arr[6] = new_arr[6], new_arr[2]
# Row 6th and 8th
new_arr[5], new_arr[7] = new_arr[7], new_arr[5]
holes = 9
def dig_hole(num_hole):
    digged_holes = [] # Init the digged holes
    hole_prob_row = [0, 1, 2]
    hole_prob_col = [0, 1, 2]
    while len(digged_holes) < holes:
        hole = [int(random.choice(hole_prob_row)),
                int(random.choice(hole_prob_col))]
        if not hole in digged_holes:
            digged_holes.append(hole)
    return digged_holes

print(dig_hole(9))
for i in range(3):
    for j in range(3):
        for hole in dig_hole(holes):
            new_arr[i*3 + hole[0]][j*3 + hole[1]] = 0