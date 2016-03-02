import Tkinter
import datetime
from BcdDigitFrame import BcdDigitFrame


class BinaryClock(object):
    def __init__(self, root):
        self._root = root
        self._digits = [0,0,0,0,0,0]
        self._setup_ui(self._digits)

    def _setup_ui(self, digits):
        self._frames= []
        images =  {'ON_PHOTO': Tkinter.PhotoImage(file='on40.gif'), 'OFF_PHOTO': Tkinter.PhotoImage(file='off40.gif')}
        for index, digit in enumerate(self._digits):
            frame = Tkinter.Frame(self._root)
            frame.grid(row=0, column=index)
            bcd_frame = BcdDigitFrame(frame, images)
            bcd_frame.set_digit(digit)
            self._frames.append(bcd_frame)

    def _time_to_digits(self, the_time):
        return [
                the_time.hour / 10,
                the_time.hour % 10,
                the_time.minute / 10,
                the_time.minute % 10,
                the_time.second / 10,
                the_time.second % 10]

    def tick(self):
        the_now = datetime.datetime.now().time()
        new_digits = self._time_to_digits(the_now)
        if not new_digits == self._digits:
            self._digits = new_digits
            for (frame, digit) in zip(self._frames, self._digits):
                frame.set_digit(digit)
        self._root.after(100, self.tick)


if __name__ == '__main__':
    root = Tkinter.Tk()
    bc = BinaryClock(root)
    bc.tick()
    root.mainloop()
