import keyboard

events = keyboard.record(until='space')  # records all events until 'space' is pressed

typed = list(keyboard.get_typed_strings(events, allow_backspace=True))

print("You typed:", typed[-1])