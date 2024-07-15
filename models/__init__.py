'''
author: tianshirui
time: 20240714 20:45
'''



def get_model(name):
    model = globals()[name.lower()].__getattribute__(name.upper())
    return model
