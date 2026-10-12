import argparse

import os

class Main:
        def __init__(self, file, output_name, response=["200"]):
                self.file = file
                self.file_name = file.rsplit('.', 1)[0]
                self.responses = response
                if isinstance(self.responses[0], list):
                    self.responses = self.responses[0]
                if output_name.replace(" ", "")  == '':
                        self.output_name = f'output_{self.file_name}.txt'
                else:
                        self.output_name = output_name


        def read_write_file(self):
                content = f'\nOutput of the {self.file} with the responses {self.responses}:\n'
                with open(self.file, 'r') as f:
                        for line in f:
                                if any(rs in line for rs in self.responses) or 'DIRECTORY' in line:
                                        content += f'\t--> {line} '

                if os.path.exists(self.output_name):
                        print('\n!!! File already exists !!!\n')
                        prefer = input('Continue anyway ? (Y/n) >> ').lower()

                        if prefer == 'y' or prefer == '':
                                self.output(file=self.output_name, content=content)
                        elif prefer == 'n':
                                another_name = input('Enter the Output file name (with the extension): ')
                                self.output(file=another_name, content=content)
                        else:
                                print('Only Y or N\n Exiting...')
                                exit()
                else:
                        self.output(file=self.output_name,content=content)

        def output(self, file,content):
                with open(file ,'w') as o:
                        o.write(content)



parser = argparse.ArgumentParser(description='Rf_DIRB')

parser.add_argument('-f', '--file', help='file to see' , dest='input_file')
parser.add_argument('-o','--output',help='output file', dest='output_file', default='')
parser.add_argument('-r','--responses', help='wanted responses',dest='responses', default=['200'], nargs='+' )

args = parser.parse_args()


if args.input_file:
        m = Main(file=args.input_file, output_name=args.output_file, response=args.responses)
        m.read_write_file()
else:
        f = input('\nEnter the file name (with the extension): ')
        r = input('Enter how much response you want (split them by a ,): ')
        o = input('Enter the output file name (Let it empty for standart): ')

        if len(r) == 0:
                r = ["200"]
        else:
                r = [resp.strip() for resp in r.split(',') ]

        m = Main(file=f,output_name=o,response=r)
        m.read_write_file()


