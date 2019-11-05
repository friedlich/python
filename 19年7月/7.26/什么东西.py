import sys
def main(args):
    print(args)
if __name__ == '__main__':
    print('执行如下代码__name__==\'__main__\'')
    main(sys.argv[1:])