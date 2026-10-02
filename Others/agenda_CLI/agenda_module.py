import json
import re
import datetime
import time
from pathlib import Path

from rich import print


# Always use the folder where this Python file is located
DATA_FILE = Path(__file__).parent / "data.json"


def add_plans(data_input):
    date_plan = input(
        'Type the date that you have plans for - (MM/DD/YYYY): '
    )

    # Check date format
    if not re.fullmatch(r'\d{2}/\d{2}/\d{4}', date_plan):
        print('[red]Invalid date format![/]')
        return

    # Convert string to date
    try:
        date = datetime.datetime.strptime(
            date_plan,
            "%m/%d/%Y"
        ).date()

    except ValueError:
        print(
            '[red]!!! ERROR, be sure you type correctly the date !!![/]'
        )
        return

    # Don't allow plans in the past
    today = datetime.date.today()

    if date < today:
        print('\n[red]Impossible to write plans for past dates.[/]')
        return

    plan = input('Enter the plans: ')

    # Add the plan to the dictionary
    data_input[date_plan] = plan

    # Save the updated dictionary
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data_input,
            file,
            indent=4,
            ensure_ascii=False
        )

    print('\n[green]Success adding the new plan![/]')


def load_json():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if not data:
                print(
                    '\n[yellow]!! Warning: The file is empty !![/]\n'
                )
            else:
                print(
                    '\n[green]__ Success loading the json file __[/]\n'
                )

            return data

    except FileNotFoundError:
        print(
            '\n[#ff8700]File not found. Creating a new one.[/]'
        )

        # Create an empty JSON file
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=4)

        return {}

    except json.JSONDecodeError:
        print(
            '[red]File is empty or contains invalid JSON![/]'
        )
        return {}


def see_plans(data_input):
    print('\nYour plans:')

    if not data_input:
        print('\t[red]No plans found.[/]')
    else:
        for date, plan in data_input.items():
            print(f'\t{date} - {plan}')

    print()


def remove_plans(data_input):
    date_plan = input(
        'Type the date of the plan you want to remove (MM/DD/YYYY): '
    )

    if date_plan not in data_input:
        print('\nNo plan found for this date.')
        return

    print(f'\nPlan: {data_input[date_plan]}')

    confirmation = input(
        'Do you want to remove it? (Y/n): '
    ).lower()

    if confirmation == 'y' or confirmation == '':
        del data_input[date_plan]

        # Save the updated dictionary
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(
                data_input,
                file,
                indent=4,
                ensure_ascii=False
            )

        print('\n[green]Plan removed successfully![/]\n')

    else:
        print('\n[red]Plan was not removed.[/]\n')


def exit_program():
    try:
        while True:
            sure = input(
                '\nAre you sure that you want to close the program (y/N): '
            ).lower()

            if sure == 'y':
                try:
                    print('\t[#ff8700]Exiting[/]', end='')

                    for _ in range(3):
                        time.sleep(0.5)
                        print('[#ff0000].[/]', end='')

                    print(
                        '\n[yellow]Thank you for using this program !![/]\n'
                    )
                
                    exit()

                except KeyboardInterrupt:
                    print(
                        '\n\n[blue]Damn, you don\'t have patience bro, '
                        'but alright, thank you anyways.[/]\n'
                    )
                    exit()

            elif sure == 'n' or sure == '':
                print()
                break
            else:
                print('[#ff8700]Type just "y" or "n" ! [/]')

    except Exception as e:
        print(f'An error occurred!\n\t{e}')
