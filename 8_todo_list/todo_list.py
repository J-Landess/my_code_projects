tasks = ["Get Groceries","2Keep Coding", "Pick up Remi From boston"]

def first_options():
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Close")


def options(tasks):
    while True:
        try:
            firstchoice = int(input("select a number: "))
            if firstchoice == 1:
                print(tasks)
                first_options()
                continue
            elif firstchoice == 2:
                
                new_task = str(input("Please enter a task: "))
                tasks.append(new_task)
                print(tasks)
                continue
            elif firstchoice == 3:
                first_options()
                old_task = input("which task would you like to remove? ")
                if old_task in tasks:
                    tasks.remove(old_task)
                    print(tasks)
                    continue
            elif firstchoice == 4:
                print("exiting todo list")
                break
            else:
                print("Invalid Entry")
        except ValueError:
            print("Invalid Option")
            
         
def run(first_options, options):

    first_options()
    options(tasks)


run(first_options, options)   

    
    