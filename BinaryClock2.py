import Tkinter
import datetime


class BinaryClock:
    def __init__(self, root):
        self.root = root
        self.on_photo = Tkinter.PhotoImage(file='on40.gif')
        self.off_photo = Tkinter.PhotoImage(file='off40.gif')
        self.digits = [0,0,0,0,0,0]
        self.setup_ui(self.digits)

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
            self.setup_ui(new_digits)
        self.root.after(100, self.tick)

    def setup_ui(self, digits):
        index = 0
        for digit in digits:
            bcd = self.bcd_num(digit)
            for jndex in range(0,4):
                photo = self.off_photo
                if bcd[jndex]:
                    photo = self.on_photo
                Tkinter.Label(self.root, image=photo).grid(row=jndex, column=index)
            Tkinter.Label(self.root, text=digit).grid(row=4, column=index)
            index += 1



if __name__ == '__main__':
    root = Tkinter.Tk()
    bc = BinaryClock(root)
    bc.tick()
    root.mainloop()
