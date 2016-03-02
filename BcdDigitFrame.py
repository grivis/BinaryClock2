import Tkinter


class BcdDigitFrame:
    def __init__(self, parent):
        self.parent = parent
        self.digit = 0
        self.bcd_array=self.calculate_bcd_array(self.digit)
        self.setup_ui()

    def setup_ui(self):
        self.dots = self.initialize_dots()
        index = 0
        for dot in self.dots:
            dot.grid(row=index, column=0)
            index += 1
        self.digit_label = Tkinter.Label(self.parent, text=self.digit)
        self.digit_label.grid(row=4, column=0)

    def initialize_dots(self):
        dots = [None] * 4
        for index in range(0, 4):
            dots[index] = Tkinter.Label(self.parent, image=OFF_PHOTO)
            dots[index].grid(row=index, column=0)
        return dots

    def calculate_bcd_array(self, digit):
        bcd = [False, False, False, False]
        if digit % 2 == 1:
            bcd[3] = True
        digit /= 2
        if digit % 2 == 1:
            bcd[2] = True
        digit /= 2
        if digit % 2 == 1:
            bcd[1] = True
        digit /= 2
        if digit % 2 == 1:
            bcd[0] = True
        return bcd

    def set_digit(self, digit):
        if not digit == self.digit:
            self.digit = digit
            self.bcd_array = self.calculate_bcd_array(digit)
            self.apply_digit(self.digit)
            self.apply_bcd_array(self.bcd_array)

    def apply_digit(self, digit):
        self.digit_label.config(text=digit)

    def apply_bcd_array(self, bcd_array):
        for index in range(0,4):
            is_on = bcd_array[index]
            dot = self.dots[index]
            if is_on:
                dot.config(image=ON_PHOTO)
            else:
                dot.config(image=OFF_PHOTO)


if __name__ == '__main__':
    root = Tkinter.Tk()
    ON_PHOTO = Tkinter.PhotoImage(file='on40.gif')
    OFF_PHOTO = Tkinter.PhotoImage(file='off40.gif')
    bdf = BcdDigitFrame(root)
    root.mainloop()
