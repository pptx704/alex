import pystray
from PIL import Image, ImageDraw
from datetime import datetime
from util import check_out

# Timer is on from the moment the program is started
state = {
    'started': True,
    'time': datetime.now().isoformat(),
}

# Checks for logo.png. If it doesn't exist, creates a red and blue square.
def create_image():
    try:
        image = Image.open('logo.png')
        image = image.resize((64, 64))
        return image
    except FileNotFoundError:
        image = Image.new('RGB', (64, 64), (255, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 32, 64), fill=(0, 0, 255))
        draw.rectangle((32, 0, 64, 64), fill=(255, 0, 0))
        return image

# Resets the timer
def reset():
    state['time'] = datetime.now().isoformat()

# Starts or stops the timer
def log():
    state['started'] = not state['started']
    if not state['started']:
        check_out('Work', state['time'], datetime.now().isoformat())
        reset()
    icon.menu = create_menu()

# Quit the program and save the timer
def quit():
    if state['started']:
        check_out('Work', state['time'], datetime.now().isoformat())
    icon.stop()

# Generate the menu
def create_menu():
    return pystray.Menu(
        pystray.MenuItem('Quit without saving', lambda: icon.stop()),
        pystray.MenuItem('Reset', reset),
        pystray.MenuItem('Check Out' if state['started'] else 'Check In', log),
        pystray.MenuItem('Quit', quit),
    )


# Create an icon with the given image and menu
icon = pystray.Icon('Alex', create_image(), 'Alex', create_menu())

# Start the icon
icon.run()