import rich
from agenda_module import *


data = load_json()

while True:
    opts = int(input('Choose one of the following options:\n\t0 - Reload JSON file\n\t1 - See plans\n\t2 - Add plans\n\t3 - Remove plans\n>> '))
    if opts == 0:
        data = load_json()
    elif opts == 1:
        see_plans(data_input=data)
    elif opts == 2:
        new_plans = add_plans(data_input=data)
        print(new_plans)
    elif opts == 3:
        remove_plans()
    