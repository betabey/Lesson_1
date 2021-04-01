class Error:
    def __init__(self, *args):
        self.my_list = []

    def inputline(self):

        while True:
            try:
                val = input('Input element or write "done" :')

                if val == 'done' or val == 'Done' or val=='DONE':
                    self.my_list.append(val)
                    print(f'Current line - {self.my_list[:-1]} \nDone!!!')
                    break
                else:
                    self.my_list.append(int(val))
                    print(f'Current line - {self.my_list} \n ')
            except:
                print(f"Only numbers bro!!!")
                stop = input('Try again or write "stop" :').title()

                if stop == 'Stop':
                    print('Done')
                else:
                    return 'Done'

try_except = Error()
print(try_except.inputline())