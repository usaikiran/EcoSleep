
import time
from pynput import mouse
import threading

class MouseListener:

    def __init__( self ):

        self.EXIT_FLAG = False

    def __destroy__( self ):

        print "detroy called !!"

    def on_move( self, *args ):

        print('Pointer moved to {0}'.format(
            (args[0], args[1])))

    def on_click( self, x, y, button, pressed ):

        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))

        if not pressed:
            return False

    def on_scroll( self, x, y, dx, dy ):

        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    def init_listener( self, target ):

        with mouse.Listener(
                on_move = target,
                on_click = target,
                on_scroll = target ) as listener:
            listener.join()


    def on_mouse_action( self, target ):

        threading.Thread( target=self.init_listener, args=[target] ).start()

if __name__ == '__main__' :

    init_listener( on_move )