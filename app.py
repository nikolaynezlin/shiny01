from shiny import reactive
from shiny.express import ui, render, input

ui.input_slider("s1", "Slider 1", min=0, max=10, value=5)
ui.input_slider("s2", "Slider 2", min=0, max=100, value=50)


# This output only reacts to the first slider
@render.text
def result():
    return f"{input.s1()} squared is {input.s1() ** 2}."


# This output reacts to both sliders
@render.text
def both_sliders_output():
    return f"{input.s1()} + {input.s2()} is {input.s1() + input.s2()}."

