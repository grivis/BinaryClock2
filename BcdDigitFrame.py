import Tkinter


class BcdDigitFrame(object):
    def __init__(self, parent, images):
        self._images=images
        self._digit = 0
        self._setup_ui(parent)

    def _setup_ui(self, parent):
        self._dots = self._initialize_dots(parent)
        self._digit_label = Tkinter.Label(parent, text=self._digit)
        self._digit_label.grid(row=4, column=0)

    def _initialize_dots(self, parent):
        dots = []
        for index in range(0, 4):
            dot = Tkinter.Label(parent, image=self._images['OFF_PHOTO'])
            dot.grid(row=index, column=0)
            dots.append(dot)
        return dots

    def _calculate_bcd_array(self, digit):
        return [digit / (2 ** x) % 2 == 1 for x in range(3,-1,-1)]

    def set_digit(self, digit):
        if not digit == self._digit:
            self._digit = digit
            bcd_array = self._calculate_bcd_array(self._digit)
            self._apply_digit(self._digit)
            self._apply_bcd_array(bcd_array)

    def _apply_digit(self, digit):
        self._digit_label.config(text=digit)

    def _apply_bcd_array(self, bcd_array):
        for (is_on, dot) in zip(bcd_array, self._dots):
            if is_on:
                dot.config(image=self._images['ON_PHOTO'])
            else:
                dot.config(image=self._images['OFF_PHOTO'])


if __name__ == '__main__':
    root = Tkinter.Tk()
    images = {'ON_PHOTO': Tkinter.PhotoImage(file='on40.gif'), 'OFF_PHOTO': Tkinter.PhotoImage(file='off40.gif')}
    bdf = BcdDigitFrame(root, images)
    root.mainloop()
