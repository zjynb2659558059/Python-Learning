"""
1，函数的创建和调用
    1）函数的创建:
    def 函数名（[输入参数]）:
        函数体
        [return xxx]
    2)函数的调用:
    函数名([实际参数])
2,函数的参数传递:
    1)位置实参:根据形参对应的位置进行实参传递
    2）关键字实参：根据形参名称进行实参传递
注意： 在函数调用过程中，进行参数的传递，如果是不可变对象，在函数体的修改不会影响实参的值，
        如果是可变对象，在函数体的修改会影响到实参的值
3,函数的返回值：
    1)如果函数没有返回值(函数执行完毕之后，不需要给调用处提供数据) return可以省略不写
    2）函数的返回值如果是1个，直接返回类型
    3）函数的返回值如果是多个，返回的结果为元组
3,函数的参数定义:
    函数定义默认值参数：函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
    1)个数可变的位置参数:
    ①定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
    ②使用*定义个数可变的位置形参
    ③结果为一个元组
    ④可变的位置参数只能是1个   ：e.g: def fun2(*args,*a):
                                    pass
                                    以上代码，程序会报错，可变的位置参数只能是1个
    3）个数可变的关键字形参：
    ①定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
    ②使用**定义个数可变的关键字形参
    ③结果为一个字典
    ④个数可变的关键字参数只能是1个  :e.g: def fun2(**args,**a):
                                        pass
                                        以上代码，程序会报错，可变的关键字参数只能是1个
    4)小技巧：在一个函数定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求：个数可变的位置形参放在个数可变的关键字形参之前
    在位置形参和关键字形参之间可用*分割，即：
    e.g:
    def fun(a,b,*,c,d,**args):
    pass
    即*之前的为位置形参，*之后的只能采用关键字形参
    def fun(*args,**args2)
    def fun(a,b,*,c,d,**args)
    def fun (a,b=10,*args,**args)
    都是可行的
4，变量的作用域：
    1）局部变量： 在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会变成全局变量
    2）全局变量: 函数体外定义的变量，可作用于函数内外
5,递归函数
    e.g:
    def fac(n):
    if n==1:
    return 1
    else:
    res=n*fac(n-1)
    return res



"""

#函数的参数定义
def fun1(*a):
    print(a)
    print(a[0])
    return a
f1=fun1(10)
f2=fun1(10,20)
f3=fun1(10,20,30)
print(f1,type(f1),'$1',f2,type(f2),'$2',f3,type(f3),'$3')

#def fun1(a,b=10):
#    print(a,b)
#def fun2(a,b):
#    print(a,b)
#ax=fun1(1)
#print(ax)
#ax=fun1(1,20)
#print(ax)
#ab=fun2(1,2)
#print(ab)


#函数的返回值
#def fun1():
#    print('hello')
#print(fun1(),type(fun1()))
#
#def fun2():
#    return 'hello'
#print(fun2(),type(fun2()))
#
#def fun3():
#    return 'hello','world'
#print(fun3(),type(fun3()))

