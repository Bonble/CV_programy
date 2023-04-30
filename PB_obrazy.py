# Jest to program okienkowy który przetwarza pliki .jpg za pomocą kilkunastu algorytmów, takich jak np. mieszanie
# dwóch obrazów, wyszukiwanie krawędzi itd. i pozwala je zapisywać na dysk lub do schowków


import math
import tkinter.messagebox
from functools import partial
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import tkinter as tk

class Okno:
    def __init__(self):
        self.schow = [0, 0, 0, 0]
        self.plik1 = 0
        self.plik2 = 0
        self.wynik = 0
        self.win = tk.Tk()
        self.win.title('Przemysław Bajkowski - projekt nr 2')
        self.win.geometry("1000x650")

            # menu
        menubar = Menu(self.win)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Pliki", menu=filemenu)
        filemenu.add_command(label="Wybierz zdjęcie 1", command=self.otworzZdj1)
        filemenu.add_command(label="Wybierz zdjęcie 2", command=self.otworzZdj2)
        filemenu.add_command(label="Zapisz wynik do pliku", command=self.zapisz)
        zapSchowmenu = Menu(filemenu, tearoff=0)
        zapSchowmenu.add_command(label='1', command=partial(self.zapiszSchow, 1))
        zapSchowmenu.add_command(label='2', command=partial(self.zapiszSchow, 2))
        zapSchowmenu.add_command(label='3', command=partial(self.zapiszSchow, 3))
        zapSchowmenu.add_command(label='4', command=partial(self.zapiszSchow, 4))
        filemenu.add_cascade(
            label="Zapisz wynik do schowka",
            menu=zapSchowmenu
        )

        filemenu.add_separator()

        wczySchowmenu = Menu(filemenu, tearoff=0)
        wczySchowmenu1 = Menu(wczySchowmenu, tearoff=0)
        wczySchowmenu1.add_command(label='do 1', command=partial(self.wczytajSchow, 1, 1))
        wczySchowmenu1.add_command(label='do 2', command=partial(self.wczytajSchow, 1, 2))
        wczySchowmenu.add_cascade(
            label="1",
            menu=wczySchowmenu1
        )
        wczySchowmenu2 = Menu(wczySchowmenu, tearoff=0)
        wczySchowmenu2.add_command(label='do 1', command=partial(self.wczytajSchow, 2, 1))
        wczySchowmenu2.add_command(label='do 2', command=partial(self.wczytajSchow, 2, 2))
        wczySchowmenu.add_cascade(
            label="2",
            menu=wczySchowmenu2
        )
        wczySchowmenu3 = Menu(wczySchowmenu, tearoff=0)
        wczySchowmenu3.add_command(label='do 1', command=partial(self.wczytajSchow, 3, 1))
        wczySchowmenu3.add_command(label='do 2', command=partial(self.wczytajSchow, 3, 2))
        wczySchowmenu.add_cascade(
            label="3",
            menu=wczySchowmenu3
        )
        wczySchowmenu4 = Menu(wczySchowmenu, tearoff=0)
        wczySchowmenu4.add_command(label='do 1', command=partial(self.wczytajSchow, 4, 1))
        wczySchowmenu4.add_command(label='do 2', command=partial(self.wczytajSchow, 4, 2))
        wczySchowmenu.add_cascade(
            label="4",
            menu=wczySchowmenu4
        )
        filemenu.add_cascade(
            label="Wczytaj ze schowka",
            menu=wczySchowmenu
        )

        filemenu.add_separator()
        filemenu.add_command(label="Histogram wyniku", command=self.histogram)
        filemenu.add_separator()
        filemenu.add_separator()
        filemenu.add_command(label="Wyjdź", command=self.win.quit)


        pojmenu = Menu(menubar, tearoff=0)
        pojmenu.add_command(label="Negatyw", command=self.negatyw)
        pojmenu.add_command(label="Jasność Liniowa", command=self.jasnoscLiniowa)
        pojmenu.add_command(label="Jasność Potęgowa", command=self.jasnoscPotegowa)
        pojmenu.add_command(label="Kontrast", command=self.kontrast)
        pojmenu.add_command(label="Sobel - Pion", command=self.sobelPion)
        pojmenu.add_command(label="Sobel - Poziom", command=self.sobelPoziom)
        pojmenu.add_command(label="Prewitt - Pion", command=self.prewittPion)
        pojmenu.add_command(label="Prewitt - Poziom", command=self.prewittPoziom)
        pojmenu.add_command(label="Roberts - Pion", command=self.robertsPion)
        pojmenu.add_command(label="Roberts - Poziom", command=self.robertsPoziom)
        pojmenu.add_command(label="Minimum", command=self.minimum)
        pojmenu.add_command(label="Maksimum", command=self.maksimum)
        pojmenu.add_command(label="Mediana", command=self.mediana)
        menubar.add_cascade(label="Efekty do zdjęcia 1", menu=pojmenu)

        mieszmenu = Menu(menubar, tearoff=0)
        mieszmenu.add_command(label="Suma", command=self.suma)
        mieszmenu.add_command(label="Odejmowanie", command=self.odejmowanie)
        mieszmenu.add_command(label="Różnica", command=self.roznica)
        mieszmenu.add_command(label="Mnożenie", command=self.mnozenie)
        mieszmenu.add_command(label="Mnożenie odwrotności", command=self.mnozenieOdwrotnosci)
        mieszmenu.add_command(label="Negacja", command=self.negacja)
        mieszmenu.add_command(label="Ciemniejsze", command=self.ciemniejsze)
        mieszmenu.add_command(label="Wyłączanie", command=self.wyloczanie)
        mieszmenu.add_command(label="Nakładka", command=self.nakladka)
        mieszmenu.add_command(label="Ostre światło", command=self.ostreSwiatlo)
        mieszmenu.add_command(label="Łagodne światło", command=self.lagodneSwiatlo)
        mieszmenu.add_command(label="Rozcieńczanie", command=self.rozcienczanie)
        mieszmenu.add_command(label="Wypalenie", command=self.wypalanie)
        mieszmenu.add_command(label="Reflect", command=self.reflect)
        mieszmenu.add_command(label="Rozcieńczanie", command=self.rozcienczanie)
        mieszmenu.add_command(label="Prezroczystość", command=self.przezroczystosc)
        menubar.add_cascade(label="Mieszanie zdjęć", menu=mieszmenu)
            # napisy
        tk.Label(self.win, text="Zdjęcie 1:").place(x=25, y=2)
        tk.Label(self.win, text="Zdjęcie 2:").place(x=595, y=2)
        tk.Label(self.win, text="Wynik:").place(x=25, y=270)

        self.slid = tk.Scale(self.win, from_=-255, to=255, orient='horizontal', length=450)
        self.zatwierdz = Button(self.win, text="Zatwierdź", command=self.jasnoscLiniowaZmiana)

        self.win.config(menu=menubar)
        self.win.mainloop()

        # funkcje menu
    def otworzZdj1(self):
        plik1 = fd.askopenfilename()
        if plik1:
            image = Image.open(plik1)
            self.plik1 = image
            image = image.resize((450,250))
            img = ImageTk.PhotoImage(image)


            label1 = tk.Label(image=img)
            label1.image = img
            label1.place(x = 20, y = 20)

    def otworzZdj2(self):
        plik2 = fd.askopenfilename()
        if plik2:
            image = Image.open(plik2)
            self.plik2 = image
            image = image.resize((450,250))
            img = ImageTk.PhotoImage(image)

            label2 = tk.Label(image=img)
            label2.image = img
            label2.place(x=490, y=20)

    def zapisz(self):
        if (self.wynik != 0):
            plik = fd.asksaveasfilename(filetypes=[("jpg file", ".jpg")],defaultextension=".jpg")
            if plik:
                self.wynik.save(plik)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie ma pliku wynikowego!")

    def zapiszSchow(self, i):
        if(self.wynik != 0):
            self.schow[i] = self.wynik
        else:
            tkinter.messagebox.showinfo("Bład schowka", "Nie ma obrazu wynikowego!")

    def wczytajSchow(self, skad, gdzie):
        if (self.schow[skad] != 0):
            if(gdzie == 1):
                image = self.schow[skad]
                self.plik1 = image
                image = image.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                label1 = tk.Label(image=img)
                label1.image = img
                label1.place(x=20, y=20)
            else:
                image = self.schow[skad]
                self.plik2 = image
                image = image.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                label2 = tk.Label(image=img)
                label2.image = img
                label2.place(x=490, y=20)
        else:
            tkinter.messagebox.showinfo("Bład schowka", "W schowku nie ma zapisanego obrazu!")

    def czysc(self):
        self.slid.destroy()
        self.zatwierdz.destroy()

            # algorytmy zmieniające obrazy
    def negatyw(self):
        if(self.plik1 != 0):
            self.czysc()
            img = self.plik1
            result_img = Image.new('RGB', (img.width, img.height))
            w, h = img.size
            for i in range(w):
                for j in range(h):
                    r, g, b = img.getpixel((i, j))
                    r = 255 - r
                    g = 255 - g
                    b = 255 - b
                    result_img.putpixel((i, j), (r, g, b))

            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def jasnoscLiniowa(self):
        if (self.plik1 != 0):
            self.czysc()
            self.wynik = self.plik1
            image = self.plik1.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)

            self.slid = tk.Scale(self.win, from_=-255, to=255, orient='horizontal', length=450)
            self.slid.pack()
            self.slid.set(0)
            self.slid.place(x=25, y=550)
            self.zatwierdz = Button(self.win, text="Zatwierdź", command=self.jasnoscLiniowaZmiana)
            self.zatwierdz.place(x=490, y=570)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def jasnoscLiniowaZmiana(self): # self.slid.get() dodatnia rozjaśnia, ujemna przyciemnia
        img = self.plik1
        result_img = Image.new('RGB', (img.width, img.height))
        w, h = img.size
        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r += self.slid.get()
                if r < 0: r = 0
                if r > 255: r = 255
                g += self.slid.get()
                if g < 0: r = 0
                if g > 255: r = 255
                b += self.slid.get()
                if b < 0: r = 0
                if b > 255: r = 255
                result_img.putpixel((i, j), (r, g, b))
        self.wynik = result_img
        image = result_img.resize((450, 250))
        img = ImageTk.PhotoImage(image)

        self.label3 = tk.Label(image=img)
        self.label3.image = img
        self.label3.place(x=25, y=290)

    def jasnoscPotegowa(self):
        if (self.plik1 != 0):
            self.czysc()
            self.wynik = self.plik1
            image = self.plik1.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)

            self.slid = tk.Scale(self.win, from_=0, to=10, orient='horizontal', length=450, resolution=0.1)
            self.slid.pack()
            self.slid.set(0)
            self.slid.place(x=25, y=550)
            self.zatwierdz = Button(self.win, text="Zatwierdź", command=self.jasnoscPotegowaZmiana)
            self.zatwierdz.place(x=490, y=570)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def jasnoscPotegowaZmiana(self): # self.slid.get() <1 rozjaśnia, >1 przyciemnia
        img = self.plik1
        result_img = Image.new('RGB', (img.width, img.height))
        w, h = img.size
        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r /= 255
                r = pow(r, self.slid.get())
                r *= 255
                if r < 0: r = 0
                if r > 255: r = 255
                g /=  255
                g = pow(g, self.slid.get())
                g *= 255
                if g < 0: r = 0
                if g > 255: r = 255
                b /= 255
                b = pow(b, self.slid.get())
                b *= 255
                if b < 0: r = 0
                if b > 255: r = 255
                result_img.putpixel((i, j), (round(r), round(g), round(b)))
        self.wynik = result_img
        image = result_img.resize((450, 250))
        img = ImageTk.PhotoImage(image)

        self.label3 = tk.Label(image=img)
        self.label3.image = img
        self.label3.place(x=25, y=290)

    def kontrast(self):
        if (self.plik1 != 0):
            self.czysc()
            self.wynik = self.plik1
            image = self.plik1.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)

            self.slid = tk.Scale(self.win, from_=-127, to=126, orient='horizontal', length=450, resolution=1)
            self.slid.pack()
            self.slid.set(0)
            self.slid.place(x=25, y=550)
            self.zatwierdz = Button(self.win, text="Zatwierdź", command=self.kontrastZmiana)
            self.zatwierdz.place(x=490, y=570)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def kontrastZmiana(self):  # self.slid.get() obniża kontrast, >0 zwiększa
        img = self.plik1
        result_img = Image.new('RGB', (img.width, img.height))
        w, h = img.size
        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r = (127 / (127 - self.slid.get())) * (r - self.slid.get())
                g = (127 / (127 - self.slid.get())) * (g - self.slid.get())
                b = (127 / (127 - self.slid.get())) * (b - self.slid.get())
                result_img.putpixel((i, j), (round(r), round(g), round(b)))
        self.wynik = result_img
        image = result_img.resize((450, 250))
        img = ImageTk.PhotoImage(image)

        self.label3 = tk.Label(image=img)
        self.label3.image = img
        self.label3.place(x=25, y=290)

    def robertsPion(self):
        if (self.plik1 != 0):
            maska = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def prewittPion(self):
        if (self.plik1 != 0):
            maska = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def sobelPion(self):
        if (self.plik1 != 0):
            maska = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def robertsPoziom(self):
        if (self.plik1 != 0):
            maska = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def prewittPoziom(self):
        if (self.plik1 != 0):
            maska = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def sobelPoziom(self):
        if (self.plik1 != 0):
            maska = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def laplace(self):
        if (self.plik1 != 0):
            maska = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    r += r1 * maska[x + 1][y + 1]
                                    g += g1 * maska[x + 1][y + 1]
                                    b += b1 * maska[x + 1][y + 1]

                    result_img.putpixel((i, j), (r, g, b))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def maksimum(self):
        if (self.plik1 != 0):
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    maskaR = []  # sort
                    maskaG = []  # sort
                    maskaB = []  # sort
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                    maskaR.sort()
                    maskaG.sort()
                    maskaB.sort()
                    result_img.putpixel((i, j), (maskaR[8], maskaG[8], maskaB[8]))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def minimum(self):
        if (self.plik1 != 0):
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    maskaR = []  # sort
                    maskaG = []  # sort
                    maskaB = []  # sort
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                    maskaR.sort()
                    maskaG.sort()
                    maskaB.sort()
                    result_img.putpixel((i, j), (maskaR[0], maskaG[0], maskaB[0]))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")

    def mediana(self):
        if (self.plik1 != 0):
            img1 = self.plik1
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            for i in range(w):
                for j in range(h):
                    r = 0
                    b = 0
                    g = 0
                    maskaR = []  # sort
                    maskaG = []  # sort
                    maskaB = []  # sort
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i == 0 and x < 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                            elif i == w - 1 and x > 0:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                            else:
                                if j == 0 and y < 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                elif j == h - 1 and y > 0:
                                    r1, g1, b1 = img1.getpixel((i + x, j))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                                else:
                                    r1, g1, b1 = img1.getpixel((i + x, j + y))
                                    maskaR.append(r1)
                                    maskaG.append(g1)
                                    maskaB.append(b1)
                    maskaR.sort()
                    maskaG.sort()
                    maskaB.sort()
                    result_img.putpixel((i, j), (maskaR[4], maskaG[4], maskaB[4]))
            self.wynik = result_img
            image = result_img.resize((450, 250))
            img = ImageTk.PhotoImage(image)

            self.label3 = tk.Label(image=img)
            self.label3.image = img
            self.label3.place(x=25, y=290)
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano pliku!")


    def suma(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w<=w2 or h<=h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = r1 + r2
                        if r > 255: r = 255
                        g = g1 + g2
                        if g > 255: g = 255
                        b = b1 + b2
                        if b > 255: b = 255
                        result_img.putpixel((i, j), (r, g, b))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def odejmowanie(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = r1 + r2 - 255
                        if r < 0: r = 0
                        g = g1 + g2
                        if g < 0: g = 0
                        b = b1 + b2
                        if b < 0: b = 0
                        result_img.putpixel((i, j), (r, g, b))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def roznica(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = r1 - r2
                        if r < 0: r *= -1
                        g = g1 - g2
                        if g < 0: g *= -1
                        b = b1 - b2
                        if b < 0: b *= -1
                        result_img.putpixel((i, j), (r, g, b))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def mnozenie(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = r1 / 255 * r2 / 255
                        g = g1 / 255 * g2 / 255
                        b = b1 / 255 * b2 / 255
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def mnozenieOdwrotnosci(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = 1 - (1 - r1 / 255) * (1 - r2 / 255)
                        g = 1 - (1 - g1 / 255) * (1 - g2 / 255)
                        b = 1 - (1 - b1 / 255) * (1 - b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def negacja(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = 1 - r1 - r2
                        if r < 0:
                            r *= -1
                        g = 1 - g1 - g2
                        if g < 0:
                            g *= -1
                        g = 1 - g
                        b = 1 - b1 - b2
                        if b < 0:
                            b *= -1
                        b = 1 - b
                        result_img.putpixel((i, j), (r, g, b))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def ciemniejsze(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r1 < r2:
                            r = r1
                        else:
                            r = r2
                        if g1 < g2:
                            g = g1
                        else:
                            g = g2
                        if b1 < b2:
                            b = b1
                        else:
                            b = b2
                        result_img.putpixel((i, j), (r, g, b))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def jasniejsze(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r1 > r2:
                            r = r1
                        else:
                            r = r2
                        if g1 > g2:
                            g = g1
                        else:
                            g = g2
                        if b1 > b2:
                            b = b1
                        else:
                            b = b2
                        result_img.putpixel((i, j), (r, g, b))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def wyloczanie(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = r1 / 255 + r2 / 255 - (2 * r1 / 255 * r2 / 255)
                        g = g1 / 255 + g2 / 255 - (2 * g1 / 255 * g2 / 255)
                        b = b1 / 255 + b2 / 255 - (2 * b1 / 255 * b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def nakladka(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r1 / 255 < 0.5:
                            r = 2 * r1 / 255 * r2 / 255
                        else:
                            r = 1 - 2 * (1 - r1 / 255) * (1 - r2 / 255)
                        if g1 / 255 < 0.5:
                            g = 2 * g1 / 255 * g2 / 255
                        else:
                            g = 1 - 2 * (1 - g1 / 255) * (1 - g2 / 255)
                        if b1 / 255 < 0.5:
                            b = 2 * b1 / 255 * b2 / 255
                        else:
                            b = 1 - 2 * (1 - b1 / 255) * (1 - b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def ostreSwiatlo(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r2 / 255 < 0.5:
                            r = 2 * r1 / 255 * r2 / 255
                        else:
                            r = 1 - 2 * (1 - r1 / 255) * (1 - r2 / 255)
                        if g2 / 255 < 0.5:
                            g = 2 * g1 / 255 * g2 / 255
                        else:
                            g = 1 - 2 * (1 - g1 / 255) * (1 - g2 / 255)
                        if b2 / 255 < 0.5:
                            b = 2 * b1 / 255 * b2 / 255
                        else:
                            b = 1 - 2 * (1 - b1 / 255) * (1 - b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def lagodneSwiatlo(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r2 / 255 < 0.5:
                            r = 2 * r1 / 255 + r1 / 255 * r1 / 255 * (1 - 2 * r2 / 255)
                        else:
                            r = math.sqrt(r1 / 255) * (2 * r2 / 255 - 1) + (2 * r1 / 255) * (1 - r2 / 255)
                        if g2 / 255 < 0.5:
                            g = 2 * g1 / 255 + g1 / 255 * g1 / 255 * (1 - 2 * g2 / 255)
                        else:
                            g = math.sqrt(g1 / 255) * (2 * g2 / 255 - 1) + (2 * g1 / 255) * (1 - g2 / 255)
                        if b2 / 255 < 0.5:
                            b = 2 * b1 / 255 + b1 / 255 * b1 / 255 * (1 - 2 * b2 / 255)
                        else:
                            b = math.sqrt(b1 / 255) * (2 * b2 / 255 - 1) + (2 * b1 / 255) * (1 - b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def rozcienczanie(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r2 == 255:
                            r = 1
                        else:
                            r = (r1 / 255) / (1 - r2 / 255)
                        if g2 == 255:
                            g = 1
                        else:
                            g = (g1 / 255) / (1 - g2 / 255)
                        if b2 == 255:
                            b = 1
                        else:
                            b = (b1 / 255) / (1 - b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def wypalanie(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r2 == 0:
                            r = 0
                        else:
                            r = 1 - (1 - r1 / 255) / (r2 / 255)
                        if g2 == 0:
                            g = 0
                        else:
                            g = 1 - (1 - g1 / 255) / (g2 / 255)
                        if b2 == 0:
                            b = 0
                        else:
                            b = 1 - (1 - b1 / 255) / (b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def reflect(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            self.czysc()
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        if r2 == 255:
                            r = 1
                        else:
                            r = (r1 / 255 * r1 / 255) / (1 - r2 / 255)
                        if g2 == 255:
                            g = 1
                        else:
                            g = (g1 / 255 * g1 / 255) / (1 - g2 / 255)
                        if b2 == 255:
                            b = 1
                        else:
                            b = (b1 / 255 * b1 / 255) / (1 - b2 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def przezroczystosc(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = (1 - 0.5) * r2 / 255 + (0.5 * r1 / 255)
                        g = (1 - 0.5) * g2 / 255 + (0.5 * g1 / 255)
                        b = (1 - 0.5) * b2 / 255 + (0.5 * b1 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)

                self.slid = tk.Scale(self.win, from_=0, to=1, orient='horizontal', length=450, resolution=0.01)
                self.slid.pack()
                self.slid.set(0)
                self.slid.place(x=25, y=550)
                self.zatwierdz = Button(self.win, text="Zatwierdź", command=self.przezroczystoscZmiana)
                self.zatwierdz.place(x=490, y=570)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")

        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def przezroczystoscZmiana(self):
        if (self.plik1 != 0 and self.plik2 != 0):
            img1 = self.plik1
            img2 = self.plik2
            result_img = Image.new('RGB', (img1.width, img1.height))
            w, h = img1.size
            w2, h2 = img2.size
            if (w <= w2 or h <= h2):
                for i in range(w):
                    for j in range(h):
                        r1, g1, b1 = img1.getpixel((i, j))
                        r2, g2, b2 = img2.getpixel((i, j))
                        r = (1 - self.slid.get()) * r2 / 255 + (self.slid.get() * r1 / 255)
                        g = (1 - self.slid.get()) * g2 / 255 + (self.slid.get() * g1 / 255)
                        b = (1 - self.slid.get()) * b2 / 255 + (self.slid.get() * b1 / 255)
                        result_img.putpixel((i, j), (round(r * 255), round(g * 255), round(b * 255)))
                self.wynik = result_img
                image = result_img.resize((450, 250))
                img = ImageTk.PhotoImage(image)

                self.label3 = tk.Label(image=img)
                self.label3.image = img
                self.label3.place(x=25, y=290)
            else:
                tkinter.messagebox.showinfo("Bład pliku", "Pliki nie są kompatybilne!")
        else:
            tkinter.messagebox.showinfo("Bład pliku", "Nie wczytano obu plików!")

    def histogram(self):
        img = self.wynik
        w, h = img.size
        rTab = [0 for x in range(256)]
        gTab = [0 for x in range(256)]
        bTab = [0 for x in range(256)]
        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                rTab[r] += 1
                gTab[g] += 1
                bTab[b] += 1
        for x in range(256):
            rTab[x] = rTab[x] / (w * h)
            gTab[x] = gTab[x] / (w * h)
            bTab[x] = bTab[x] / (w * h)
        fig, axs = plt.subplots(3)
        axs[0].stairs(rTab)
        axs[0].title.set_text('Czerwony')

        axs[1].stairs(gTab)
        axs[1].title.set_text('Zielony')

        axs[2].stairs(bTab)
        axs[2].title.set_text('Niebieski')
        plt.show()


win = Okno()