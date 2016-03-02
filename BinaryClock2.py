import Tkinter
import datetime
import BcdDigitFrame


class BinaryClock:
    def __init__(self, root):
        self.root = root
        self.images =  {'ON_PHOTO': Tkinter.PhotoImage(file='on40.gif'), 'OFF_PHOTO': Tkinter.PhotoImage(file='off40.gif')}
        self.digits = [0,0,0,0,0,0]
        self.setup_ui(self.digits)

    def setup_ui(self, digits):
        self.frames= [None] * 6
        for index in range(0,6):
            frame = Tkinter.Frame(self.root)
            frame.grid(row=0, column=index)
            bcd_frame= BcdDigitFrame.BcdDigitFrame(frame, self.images)
            bcd_frame.set_digit(index)
            self.frames[index] = bcd_frame

    def time_to_digits(self, the_time):
        digits = [0, 0, 0, 0, 0, 0]
        hours = the_time.hour
        digits[0] = hours / 10
        digits[1] = hours % 10
        minutes = the_time.minute
        digits[2] = minutes / 10
        digits[3] = minutes % 10
        seconds = the_time.second
        digits[4] = seconds / 10
        digits[5] = seconds % 10
        return digits

    def tick(self):
        the_now = datetime.datetime.now().time()
        new_digits = self.time_to_digits(the_now)
        if not new_digits == self.digits:
            self.digits = new_digits
            for index in range(0, 6):
                self.frames[index].set_digit(self.digits[index])
        self.root.after(100, self.tick)


if __name__ == '__main__':
    root = Tkinter.Tk()
    bc = BinaryClock(root)
    bc.tick()
    root.mainloop()
