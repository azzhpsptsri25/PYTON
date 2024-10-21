import PySimpleGUI as sg
sg.theme("BluePurple")
sg.theme_text_color("#7FFFD4")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010025 ")],
[sg.Text("Nama : Azizah Puspitasari Saputri ")],
[sg.Text("Kelas : 5A Non-Reguler Banjarmasin ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()