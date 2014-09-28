##http://stackoverflow.com/questions/1057431/loading-all-modules-in-a-folder-in-python
##Automatically imports all modules in package
#import os
#import importlib

#for module in os.listdir(os.path.dirname(__file__)):
#    if module != '__init__.py' and module[-3:] == '.py':
#        #importlib.import_module('MixIns.'+module[:-3])
#        __import__('MixIns.'+module[:-3], globals(), locals(), ['*'])
##        for k in dir(module):
# #           locals()[k] = getattr(module[:-3], k)
#del module
##import MixIns.PlayerPhysicsMixIn
##import MixIns.DrawAsCircleMixIn
##import MixIns.InputControllerMixIn