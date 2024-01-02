import os

list = ['Human.faces', 'roads', 'trees']

for i in list:
    for photo in os.listdir(f'training/n/{i}'):
        right_name = os.getcwd().replace(r'\\', r"\"")
        photo_new = f'{photo.split(".")[0]}_{i}.jpg'
        directory = os.rename(os.path.abspath(os.path.join(right_name, f'training/n/{i}', photo)), os.path.abspath((os.path.join(right_name, 'training/n', photo_new))))
        print(os.path.join(right_name, 'n', photo_new), ' OK')
