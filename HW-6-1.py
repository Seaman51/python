import tkinter as tk


class TrafficLight(tk.Frame):
    def __init__(self, object):
        super().__init__(object)
        self.lights = [tk.Frame(object, width=300, height=300) for _ in range(3)]
        self.__color = (
            ('#FF0000', '#FFFF00', '#00FF00'),
            ('#000000', '#000000', '#000000'),
        )

    def running(self, counter=0):
        for i, a in enumerate(self.lights):
            a['bg'] = self.__color[i != counter % 3][i]
        root.after((2000 if counter == 1 else 7000), self.running, counter + 1)
        if counter == 3:
            self.lights[0]['bg'] = self.__color[1][0]
            self.lights[1]['bg'] = self.__color[0][1]
            self.lights[2]['bg'] = self.__color[1][2]
            root.after(2000, self.running, counter - 3)
        for a in self.lights:
            a.pack()


root = tk.Tk(className='TrafficLight')
app = TrafficLight(object=root)
app.running()
app.mainloop()
