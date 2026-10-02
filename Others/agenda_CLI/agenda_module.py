import json
import re
import datetime

print()


#melhorar
def add_plans(data_input):
    date_plan = input('Type the date that you have plans for - (MM/DD/AAAA): ')
    plan = input('Enter the plans: ')
    try:
        if re.fullmatch(r'\d{2}/\d{2}/\d{4}', date_plan):
            try:
                date = datetime.datetime.strptime(date_plan, "%m/%d/%y").date()
                today = datetime.today().date()
                if date < today:
                    print('\n Impossible to write plans for past dates')
                else:
                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(data_input, file, indent=4, ensure_ascii=False)

                print('Success adding the new plans')

            except ValueError:
                print('!!! ERROR, be sure you type correctly the date !!!')

            data_input[date_plan] = plan



    except:
        print('error')




#feito
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

#fazer com que veja do arquivo
def see_plans(data_input):
    print('\nYour plans:')
    for t in data_input:
        print(f'\t{t} - {data_input[t]}')
    print()


#fazer
def remove_plans():
    pass