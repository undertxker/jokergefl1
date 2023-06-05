from time import sleep

firstlst = []
secondlst = []
a = 1

while a != 0:
    print('You have 4 moves: ')
    print('1. Input')
    print('2. Output')
    print('3. Addition')
    print('4. Deleting')

    move = input('What move do you prefer? If you want to stop, print "Stop". ')

    if move == 'Stop':
        a -= 1

    elif move == 'Input':
        que = input('Choose list (first or second): ')
        if que == 'first':
            firstlst.clear()
            b = 1
            while b != 0:
                pr = input('Input: ')
                if pr == '0':
                    b -= 1
                else:
                    if pr not in firstlst:
                        splited = pr.split()
                        for i in splited:
                            if i in firstlst:
                                print('Element '+ i + ' is already in', que)
                            else:
                                firstlst.append(i)
                    else:
                        print('Such element is already in', que)

        elif que == 'second':
            secondlst.clear()
            b = 1
            while b != 0:
                pr = input('Input: ')
                if pr == '0':
                    b -= 1
                else:
                    if pr not in secondlst:
                        splited = pr.split()
                        for i in splited:
                            if i in secondlst:
                                print('Element '+ i + ' is already in', que)
                            else:
                                secondlst.append(i)
                    else:
                        print('Such element is already in', que)
        else:
            print('Invalid list')
            sleep(3)

    elif move == 'Output':
        que = input('Choose list (first or second): ')
        if que == 'first':
            print(firstlst)
            sleep(3)
        elif que == 'second':
            print(secondlst)
            sleep(3)
        else:
            print('Invalid list')
            sleep(3)

    elif move == 'Addition':
        que = input('Choose list (first or second): ')
        if que == 'first':
            pr = input('Input: ')
            splited = pr.split()
            for i in splited:
                if i in firstlst:
                    print('Element '+ i + ' is already in', que)
                else:
                    firstlst.append(i)
        elif que == 'second':
            pr = input('Input: ')
            splited = pr.split()
            for i in splited:
                if i in secondlst:
                    print('Element '+ i + ' is already in', que)
                else:
                    secondlst.append(i)

        else:
            print('Invalid list')
            sleep(3)

    elif move == 'Deleting':
        print('You can delete a specific element or clear the list')
        que = input('Choose list (first or second): ')
        if que == 'first':
            choice = input('Clear/Delete: ')
            if choice == 'Clear':
                firstlst.clear()
            elif choice == 'Delete':
                try:
                    firstlst.remove(input('What element do you want to delete: '))
                except ValueError:
                    print('There is no such element. Try again later.')
                    sleep(3)
            else:
                print('Invalid instruction')
                sleep(3)

        elif que == 'second':
            choice = input('Clear/Delete: ')
            if choice == 'Clear':
                secondlst.clear()
            elif choice == 'Delete':
                try:
                    secondlst.remove(input('What element do you want to delete: '))
                except ValueError:
                    print('There is no such element. Try again later.')
                    sleep(3)
            else:
                print('Invalid instruction')
                sleep(3)
