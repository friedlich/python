N=2
student = []
for i in range(N):
    student.append(['','',[]])
print(student)

def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('Please input student num:\n')
        stu[i][1] = input('Please input student name:\n')
        print(student)
        for j in range(3):
            stu[i][2].append(int(input('Please input student score:\n')))
            print(stu)
    print(student)

def output_stu(stu):
    for i in range(N):
        print('{}: {}'.format(stu[i][0],stu[i][1]),end='')  
        print('成绩为：')   
        # print('成绩为：\n{}\n{}\n{}'.format(stu[i][2][0],stu[i][2][1],stu[i][2][2]))
        for j in range(3):
            print('{}'.format(stu[i][2][j]))

if __name__=='__main__':
    input_stu(student)
    print(student)
    output_stu(student)