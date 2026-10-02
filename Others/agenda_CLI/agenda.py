from rich import *
from agenda_module import *


data = load_json()

while True:
    try:
        opts = int(input('\nChoose one of the following options:\n\t0 - Reload JSON file\n\t1 - See plans\n\t2 - Add plans\n\t3 - Remove plans\n\t4 - Exit Program\n>> '))
        if opts == 0:
            data = load_json()
        elif opts == 1:
            see_plans(data_input=data)
        elif opts == 2:
            new_plans = add_plans(data_input=data)
        elif opts == 3:
            remove_plans(data_input=data)
        elif opts == 4:
            exit_program()
        else:
            print('\n[red]!! You can just type a number between 0 and 4 [/]\n')
            continue
    except KeyboardInterrupt:
        exit_program()
    except ValueError:
        print('\n[#ff8700]Be sure you type correctly the numbers[/]\n')
    except Exception as e:
        print(f'\n\t[red]ERROR - {e}[/]\n')
        exit()