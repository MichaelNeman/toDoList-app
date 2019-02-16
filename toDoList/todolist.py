import csv

FILENAME = "toDoList.csv"

def write_toDoList(toDoList):
    with open(FILENAME, 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(toDoList)
        
        
def read_toDoList():
    toDoList = []
    with open (FILENAME, newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            toDoList.append(row)
    return toDoList


def menu():
    print()
    print()
    print('**To Do List Application**')
    print()
    print('(A)dd')
    print('(D)elete')
    print('(E)xit')
    print()
    print('---------------------------------------------------')
    print()
    
    
    
def list_toDoList(toDoList):
    for i in range(len(toDoList)):
        item = toDoList[i]
        print(str(i + 1) + '. ' + item[0])
    print()
    
    
def add_item(toDoList):
    description = input('Task: ')
    item = []
    item.append(description)
    toDoList.append(item)
    write_toDoList(toDoList)
    list_toDoList(toDoList)
    
    
def delete_item(toDoList):
    number = int(input('Number: '))
    if number < 1 or number > len(toDoList):
        print('invalid number.\n')
    else:
        item = toDoList.pop(number-1)
        write_toDoList(toDoList)
        list_toDoList(toDoList)
        


def main():
    
    menu()
    
    toDoList = read_toDoList()
    
    list_toDoList(toDoList)
    
    while True:
        command = input('Command: ')
        if command.lower() == 'a':
            add_item(toDoList)
        elif command.lower() == 'd':
            delete_item(toDoList)
        elif command.lower() == 'e':
            break
        else:
            print('Not a valid command. \n')
            
    print('Bye')
    
    
if __name__ == '__main__':
    main()
    
    