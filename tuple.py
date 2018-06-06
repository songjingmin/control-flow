# 使用元组
zoo = ('wolf', 'elephant', 'penguin')
print('number of animals in the zoo is', len(zoo))
new_zoo = ('monkey', 'dolphin', zoo)
print('number of animals in the new zoo is', len(new_zoo))
print('all animals in new zoo are', new_zoo)
print('animals brought from old zoo are', new_zoo[2])
print('last animal brought from old zoo is', new_zoo[2][2])

age = 22
name = 'Becken'
print('%s is %d years old' % (name,age))