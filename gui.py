import dearpygui.dearpygui as dpg
from tileset import TileSet
from math import floor

ts = TileSet()

def update_circle_fills(ts):
    for i, index in enumerate(ts.i_list):
        if index >= 0:
            state = ts.state_list()[i]
            if state:
                fill = (255,255,255,255)
            else:
                fill = (255,255,255,-255)
            dpg.configure_item(f'c{index}', fill=fill)
    if all(ts.state_list()):
        disable_all_buttons(ts)

def enable_all_buttons(ts):
    for i in range(8):
        dpg.configure_item(f'b{i}', enabled=True)
    update_circle_fills(ts)


def disable_all_buttons(ts):
    for i in range(8):
        dpg.configure_item(f'b{i}', enabled=False)
        dpg.configure_item(f'c{i}', fill=(30,190,85,255))

def reset_tiles(sender, app_data, ts):
    ts.init_tiles()
    enable_all_buttons(ts)

def flip_button(sender, app_data, i):
    ts.flip_tile(i)
    update_circle_fills(ts)


dpg.create_context()
dpg.create_viewport(title='Kephri Tile Trainer by abyssalheaven', width=600, height=600)

def create_tile_button(pos, i, width=100, height=100, radius=40):
    px, py = pos
    _b = dpg.add_button(pos=pos, width=width, height=height, tag=f'b{i}', user_data=i)
    _c = dpg.draw_circle(center=(px + 42, py + 42), radius=radius, tag=f'c{i}')
    dpg.set_item_callback(f'b{i}', flip_button)
    return _b, _c


with dpg.window(label='Tile Window', tag='ktt'):
    buttons, circles = [], []
    x, y = 35, 35
    for i, index in enumerate(ts.i_list):
        if index >= 0:
            px = x + (i % 3) * 200
            py = y + floor(i / 3) * 200
            pos = (px, py)
            b, c = create_tile_button(pos, index)
    update_circle_fills(ts)
    reset = dpg.add_button(pos=(235,260), height=50, width=100, label='Reset', tag='reset', user_data=ts)
    dpg.set_item_callback('reset', reset_tiles)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('ktt', True)
dpg.start_dearpygui()
dpg.destroy_context()