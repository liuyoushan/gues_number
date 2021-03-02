import random, os

file_path = os.path.join(os.path.dirname(__file__), 'log.txt')
files = open(file_path, 'w', encoding='utf-8')


def guess_fcnction():
    sta_end_number = check_start_end_num()
    # print_write(type(sta_end_number))
    items = 0
    while True:
        number = int(input('请继续输入猜测的数字：'))
        files.write('请继续输入猜测的数字：' + str(number) + '\n')
        # 判断需要猜测的数字是否在数值区间里面
        if number in sta_end_number:
            items += 1
            # 生成随机数
            random_number_te = random.randint(sta_end_number[0], sta_end_number[-1])
            # 判断猜测的数字和随机数进行对比判断，相等则退出循环
            if random_number_te == number:
                print_write('恭喜你，只用了{}次就猜对了'.format(items), file=files)
                break
        else:
            print_write('你输入的猜测数字不在指定数字区间！', file=files)
            continue


# 判断起始值和终止值，且生成range序列进行返回
def check_start_end_num():
    while True:
        print_write(text='*' * 30 + '欢迎进入数字猜猜猜小游戏' + '*' * 30, file=files)
        start = input('数字区间起始值:')
        stop = input('数字区间终止值:')
        files.write('数字区间起始值：' + start + '\n')
        files.write('数字区间终止值：' + stop + '\n')

        if not start.isdigit() or not stop.isdigit():
            print_write('你输入的为非数字字符，请重新输入！', file=files)
            continue
        elif start > stop:
            print_write('你输入的数字区间大小有误！请重新输入。', file=files)
            continue
        elif start == stop:
            print_write('你输入的区间数字相同！！请重新输入。', file=files)
            continue
        break
    sections_int = range(int(start), int(stop) + 1)
    return sections_int


def print_write(text, file):
    print(text)
    file.write(text + '\n')


if __name__ == '__main__':
    guess_fcnction()
    files.close()

