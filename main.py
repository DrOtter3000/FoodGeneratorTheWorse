#!/usr/bin/env python3

import tkinter
import gen

generate = gen.generate

main = tkinter.Tk()

btnGenerator = tkinter.Button(main, text="generate", command=generate)
btnGenerator.pack()


main.mainloop()
