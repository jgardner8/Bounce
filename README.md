# Bounce
A small prototype game made in Python used to test the use of mixins as a method of implementing the component pattern. Python is a good language for this as base classes can be added and removed at runtime. It turns out that mixins are an easy way to implement and use and component pattern at a small scale but are not very extendable and can be confusing at times. Overall I wouldn't recommend it.

## Some interesting points:
- The volume of the sound a bounce produces is dependent on the force of the impact, which makes bouncing around quite satisfying.
- The levels are defined entirely as 60x40 bitmaps. 

## Dependencies:
- PyGame

## Play:
- Left/right to control direction
- Down to boost down (you cannot move up, you must rely on bounce-back to get higher)
- N goes to next level
- R restarts map
