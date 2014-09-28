from MixIns.DrawAsCircleMixIn import DrawAsCircleMixIn
from MixIns.InputControllerMixIn import InputControllerMixIn
from MixIns.PlayerPhysicsMixIn import PlayerPhysicsMixIn

#TODO: Revise this
class Entity(object):
    """A tuple of components (MixIns) that make up a Game Object, with params to initialise them"""
    def __init__(self, components, params):
        new_type = type('Entity', components, {})
        #types.new_class('a', components, 
        self = new_type()

    def update(self, delta):
        for component in __bases__:
            if has_method(component, 'update'):
                component.update()

    def draw(self, display):
       for component in __bases__:
            if has_method(component, 'draw'):
                component.draw()

    def has_method(obj, method):
        return hasattr(obj, method) and callable(getattr(obj, method))

class EntityFactory(object):
    """Creates common entities, ensures consistent component use."""
    def player(start_position, color):
        RADIUS = 10
        ACCELERATION_POWER = 1000
        MAX_SPEED = 250
        START_VELOCITY = (0, 0)
        components = (InputControllerMixIn, DrawAsCircleMixIn, PlayerPhysicsMixIn)
        params = (start_position, START_VELOCITY, ACCELERATION_POWER, MAX_SPEED, #InputControllerMixIn
                  color, RADIUS, #DrawAsCircleMixIn
                  start_position, START_VELOCITY, RADIUS) #PlayerPhysicsMixIn
        return Entity(components, params)