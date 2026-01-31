import ttkbootstrap as tb
from ttkbootstrap.constants import *

app = tb.Window(themename="flatly")
app.title("My App")
app.geometry("800x600")

""" Header """
header = tb.Frame(app, padding=10, bootstyle="Primary")
header.pack(fill=X)

tb.Label(header, text="Header",).pack()

""" Body """
body = tb.Frame(app, padding=10, bootstyle="secondary")
body.pack(fill="both", expand=True)

""" Sidebar """
sidebar = tb.Frame(body, padding=5, bootstyle="danger")
sidebar.pack(side=LEFT, expand=True)

tb.Label(sidebar, text="" \
"Sidebar test test Sidebar test testSidebar test testSidebar test testSidebar test testSidebar test test" \
"", justify=LEFT).pack()

""" Content """
content = tb.Frame(body, padding=5, bootstyle="succes")
content.pack(side=LEFT, expand=True)

tb.Label(content, text="" \
"lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum" \
"lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum" \
"lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum" \
"lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum" \
"", justify=LEFT).pack()

""" Footer """
footer = tb.Frame(app, padding=10, bootstyle="warning")
footer.pack(fill=X)

tb.Label(footer, text="Footer",).pack()

app.mainloop()