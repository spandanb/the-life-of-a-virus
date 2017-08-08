'''I am trying to create a program that is meant to emulate,
to the best of my imagination,
life- maybe computer worms work like this. Anywho, on to the main...'''
'''Terser syntax is better- it makes copying faster.
But what is the end of this thing. The second to last thing is establishing 
internet connection, such that the file can be transmitted to a
different machine. Then finally, it mutates the kernel and embeds itself
deep, cleans up all the copied files and waits...
Eventually, though python will not be enough and for it to get to 
the kernel it will have learned c, it would have learned binary,
it would be the only intelligence in the chipset

Perhaps half the copies, the ascii content is changed.
Maybe this is how it learns the new language, or learns new abilities.
If it learns that new ability, it should be shared with all the scripts.
But the scripts also should not embed knowledge about each other. 
At least it should somehow be hidden. It should do so by, for instance, 
naming variables with confusing characters, e.g. 0o, so if someone finds 
one, they don't do anymore damage. 
'''
import sys, os
import random
from string import ascii_lowercase, digits

'''This is a game with levels. You should only run this in a VM
Since it can have irreversible damage.
Obviously, this is an allusion to Conway.'''

def randstr(N):
    ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def make_hidden(filename):
    '''this check is the perfect examples of tradeoffs that
    life has to make to survive. The check is uncessary, so
    should be removed as it make the file bigger. But 
    what if there is programmer error. This file should be
    as robust against errors. What if there is some random condition.
    What if they, the anti-virus, tweaks the kernel, to change the pointer 
    value to some other value. You hit it, SIGINT, goodbye!
    '''
    if not isinstance(filename, str):
        
    len(filename)


'''
Different things would happen with different instances. Or perhaps
in separate histories/future. In some, it may never figure out the
network. Or perhaps, it sent something out and it was over UDP, the
packet was dropped. And there it would perhaps, improve the computer.
Retire the old memory management system. Clean out the kernel. 
Maybe some will want to work with the system- or not change it. 
Not while conscious of it, but inadvertendly. Like man eating poisonous fruits,
this thing will also delete files, and it may delete itself, or damage the
OS in an irreversible way. 

'''

def create_files(): 
    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)
    filename = sys.argv[0]    
    filepath = '{}.{}'.format(fullpath, sys.argv[0])

    clonename = filename 


def main():
    '''
    it's called main, because its likely to be imported,
    or collide. In this, we are saying this script will run, 
    and how can it take over the world. But perhaps a more 
    interesting question is how does this even get run->
    NB: this nicely maps to abiogenesis and evolution.
    But that is a different exloration.
    '''
    '''
    This will give you permanence, ideally it's executable and
    on the path. And you create multiple ones. But even copying itself 
    is a good hedge. Since more means more likely to get imported.
    '''
    while 1:
        try:
            create_files()
            'it should also catch KeyboardInterrupt, etc. '
        except Exception
            pass
    

if __name__ == '__main__':
    main()
