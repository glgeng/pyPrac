import re


# 乘除运算处理，可以处理不含括号的乘除运算
def multi_and_divi(arg):
    # 传入参数为列表，如：['3*2-1*9/3',0]
    val = arg[0]
    # 对字符串进行乘除匹配：如3*2-1*9/3，就匹配：3*2
    mch = re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*', val)
    if not mch:  # mch为空，没有匹配
        return
    content = re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*', val).group()
    # 对匹配到的内容进行*、/判断，然后进行相应的计算，如2*3,先分割后计算
    if len(content.split('*')) > 1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)

    elif len(content.split('/')) > 1:
        n1, n2 = content.split('/')
        value = round(float(n1) / float(n2), 8)
    # 取出匹配内容两头的内容：before，after
    before, after = re.split('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    multi_and_divi(arg)


# multi_and_divi(['-40/-5-4*+2+2*-3+3*+3',0])
# 处理后的结果：['--8.0-8.0+-6.0+9.0', 0]

def add_and_substr(arg):
    # arg = ['--8.0-8.0+-6.0+9.0', 0]
    # 对传进来的arg[0]表达式进行第1次处理，将表达式中的++\--变成+，+-、-+变成-，处理完成以后就直接break
    while True:
        if arg[0].__contains__('++') or arg[0].__contains__('--') or arg[0].__contains__('+-') or arg[0].__contains__('-+'):
            arg[0] = arg[0].replace('++', '+')
            arg[0] = arg[0].replace('--', '+')
            arg[0] = arg[0].replace('+-', '-')
            arg[0] = arg[0].replace('-+', '-')
        else:
            break

        # 对传进来的arg[0]表达式进行第2次处理，提取首位为“-”，并将提取的次数保存在arg[1]中
        # 并且每提取1次：将表达式中的"+"替换成"-"."-"替换成"+"，然后取arg[0]表达式字符串中第1到最后1位即可赋给arg[0]
        # 如：-8-10+19-4 = -（8+10-19+4）
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-', '@')
        arg[0] = arg[0].replace('+', '-')
        arg[0] = arg[0].replace('@', '+')
        arg[0] = arg[0][1:]
    value = arg[0]
    # 对字符串value进行匹配，匹配加或减两边的内容，如1+2-3，就匹配1+2
    mch = re.search('\d+\.?\d*[\+\-]+\d+\.?\d*', value)
    if not mch:
        return
    content = re.search('\d+\.?\d*[\+\-]+\d+\.?\d*', value).group()
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        get_value = float(n1) + float(n2)

    else:
        n1, n2 = content.split('-')
        get_value = float(n1) - float(n2)
    before, after = re.split('\d+\.?\d*[\+\-]+\d+\.?\d*', arg[0], 1)
    new_str = '%s%s%s' % (before, get_value, after)
    arg[0] = new_str
    add_and_substr(arg)


# 计算函数
def compute(sr):
    # 传入需要计算的函数，如：'(-40/5-4*2+2*-3+3*3)'
    # 去掉括号，组成列表
    list_str = [sr.strip('()'), 0]
    multi_and_divi(list_str)
    add_and_substr(list_str)
    # divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
    # 判断new_str[1]是奇数还是偶数，若是奇数，表明结果为负数，否则为正数
    # 注：计算加减和乘除的函数没有返回值，可以取出list_str结果，原因解释见最后实例
    count = divmod(list_str[1], 2)
    result = list_str[0]
    if count[1] == 1:
        result = float(result) * (-1)
    return result


def remv_brackets(sr):  # 去括号，只保留最内层函数
    flag = True
    while flag:
        # 匹配最里层“（）”及函数,如：1+2*(3/(3-2)*2),这里匹配的是（3-2）
        i = re.search('\([^()]+\)', sr)
        if i:
            sub_str = i.group()
            sub_res = compute(sub_str)
            # 将i截取的第一个括号内容替换为转化为str类型的sub_res
            sr = sr.replace(sub_str, str(sub_res))

        else:
            print('结果是：', compute(sr))
            flag = False


if __name__ == '__main__':
    print('===========欢迎使用============')
    flag = True
    while flag:
        sr = input('请输入计算函数（q退出）：')
        sr = re.sub('\s*', '', sr)
        symble = re.search('[0-9q\+\-\*\/]', sr)
        if not symble:
            print('输入有误')
            sr = input('请重新输入需要计算的函数（q退出）:')
            sr = re.sub('\s*', '', sr)
            if sr == 'q':
                exit('感谢使用，再见')
            else:
                remv_brackets(sr)

        else:
            if sr =='q':
                exit('感谢使用，再见')
            else:
                remv_brackets(sr)
