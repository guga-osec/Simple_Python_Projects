import json
import re
import datetime

print()



def add_plans(data_input):
    date_plan = input('Type the date that you have plans for - (MM/DD/AA): ')
    plan = input('Enter the plans: ')
    try:
        date = datetime.datetime.strptime(date_plan, "%m/%d%y")
        current_year = datetime.datetime.now().year
        if re.fullmatch(r'(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/\d{2}', date_plan):

            data_input[date_plan] = plan

            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data_input, file, indent=4, ensure_ascii=False)

            print('Success adding the new plans')

    except:
        print('error')





def load_json():
    with open('data.json', 'r', encoding='utf-8' ) as f:
        try:
            data = json.load(f)
            
            if not data:
                print('\n!! Warning: The file is empty !!\n')
            print('\n__ Success loading the json file __\n')
            return data
        
        except json.JSONDecodeError:
            print('File completely empty or invalid file !!')


def see_plans(data_input):
    print('\nYour plans:')
    for t in data_input:
        print(f'\t{t} - {data_input[t]}')
    print()

def remove_plans():
    pass