# Создать репозиторий для решения задачи.
# \Для решения создать 3 ветки: в первой решение 1-3 задачи,
# \во второй 4-6, в третьей 7-10.
# отправить мне
# После одобрения вливать в main при помощи
# \пулл-реквестов.
# \1.выведите на консоль значение ключа "foo".
# \2.выведите на консоль значение ключа "b".
# \3.Добавьте в my list 44.
# bgfbggtgrterrth nnnmn



print("Home work 1 git")
my_list=[42,43]
my_dict={'foo':{
                'a':12,
                'b':(1,2,3,4,my_list)
    },
    'bar':{'c':12,
           'd':{5,6,7,8}
    },
    'moo':{'e':12,
           'f':{'lol':['L','o','l']}
    },
}
print('brunch 1')
print(my_dict['foo'])
#print(my_dict['foo']['b])
d1=my_dict['foo']['b']
print(d1)
my_list.append(44)
print(my_list)
print()
print('brunch 2')
d1=my_dict['foo']['b']
print(d1)
mn=set()
print(mn)
mn.add('9')
print()
print('brunch 3')
print(mn)
del my_dict['moo']['f']['lol'][1]
print(my_dict)
# my_dict['moo']['f']['lol']=['L','l']
# print(my_dict)
my_dict['moo']['f']['K']=['K','e','k']
print(my_dict)
my_dict.clear()
print(my_dict)


