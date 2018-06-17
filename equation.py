

import re


# 计算乘法
def mul(source_string):
    if '*' in source_string:

        only_mul_string = re.search('\d*\*\d*', source_string)  # 只匹配出一个乘法算式
        only_mul_string = only_mul_string.group()  # 得到匹配出的乘法算式

        result_mul = 1  # 乘法结果变量的初始值
        mul_num_list = re.split('\*', only_mul_string)

        for num in mul_num_list:
            result_mul *= int(num)  # 乘法算式得出结果
        result_mul = str(result_mul)  # 将整形的结果转化为字符串

        source_string = source_string.replace(only_mul_string, result_mul)  # 将原来的算式替换成算式的结果

    return source_string

# 计算除法
def div(source_string):
    if '/' in source_string:

        only_div_string = re.search('\d*/\d*', source_string)  # 只匹配出一个除法算式
        only_div_string = only_div_string.group()  # 得到匹配出的乘法算式

        div_num_list = re.split('/', only_div_string)

        result_div = int(div_num_list[0]) / int(div_num_list[1])  # 计算结果

        result_div = str(result_div)  # 将整形的结果转化为字符串

        source_string = source_string.replace(only_div_string, result_div)  # 将原来的算式替换成算式的结果

    return source_string


# 计算加法
def add(source_string):
    if '+' in source_string:
        only_add_string = re.search('\d*\+\d*', source_string)  # 只匹配出一个加法算式,如果是外层的括号也是要进行替换的
        only_add_string = only_add_string.group()  # 得到匹配出的加法算式

        add_num_list = re.split('\+', only_add_string)

        result_add = int(add_num_list[0]) + int(add_num_list[1])  # 计算结果

        result_add = str(result_add)  # 将整形的结果转化为字符串

        source_string = source_string.replace(only_add_string, result_add)  # 将原来的算式替换成算式的结果

    return source_string

# 计算减法
def sub(source_string):
    if '-' in source_string:
        only_sub_string = re.search('\d*\-\d*', source_string)  # 只匹配出一个减法算式
        only_sub_string = only_sub_string.group()  # 得到匹配出的减法算式

        sub_num_list = re.split('\-', only_sub_string)

        result_sub = int(sub_num_list[0]) - int(sub_num_list[1])  # 计算结果

        result_sub = str(result_sub)  # 将整形的结果转化为字符串

        source_string = source_string.replace(only_sub_string, result_sub)  # 将原来的算式替换成算式的结果

    return source_string


# 整个计算机程序，将会从这里开始执行

test_string = input('please input you need counting equation:')   # 用户输入算式


if len(re.findall('\(', test_string)) != len(re.findall('\)', test_string)):
    print('error')      # 判断括号的数量是否相等



# 因为在计算完毕括号中的内容后，会出现两个数字之间有两个符号，这个函数就是处理这个问题的
def format(source_string):
    format_dic = {'+-': '-', '-+': '-'}
    for i in format_dic:
        if i in source_string:
            source_string = source_string.replace(i, format_dic[i])
    return source_string


while '(' in test_string:         # 如果算式中还有括号，就继续循环计算
    ret = re.search('\([^\(\)]+\)', test_string).group()  # 取到有括号的式子
    # print(ret)
    counting_mul = mul(ret)
    counting_div = div(counting_mul)
    counting_add = add(counting_div)
    counting_sub = sub(counting_add)

    counting_sub = counting_sub.replace('(', '')  # 如果计算完毕括号中的内容后，将取消已经计算完的括号
    counting_sub = counting_sub.replace(')', '')

    test_string = test_string.replace(ret, counting_sub)

    test_string = format(test_string)      # 检查格式，经过循环的对括号的处理，最后剩下的数据都是没有括号的低级运算

for i in range(10):                     #  因为没能找到合适的控制循环的条件，所以就指定十次循环，一般情况下够用
    if len(re.findall('\b', test_string)) == 2: # 匹配有特殊边界的字符串，所以当只有数字的时候就只有指定的两个特殊边界
        pass
        # print(test_string)
    else:
        counting_mul = mul(test_string)      # 对之前的低级运算可以进行再计算，最后得到正确的答案
        counting_div = div(counting_mul)
        counting_add = add(counting_div)
        counting_sub = sub(counting_add)
        test_string = counting_sub


print('answer : %s' % test_string)   # 最后输出最终的答案

