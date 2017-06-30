"""
Evalue N differents functions on a list previously initialized. 
The input is the N value and each of functions names to apply in 
the list. If the function needs some parameter, there are introduced 
by the user after the command separated by blank spaces.
"""
if __name__ == '__main__':
    # Number of commands to execute
    N = int(raw_input())
    # Predefined functions availables
    opt = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']
    # List to use in the commands execution
    mi_list = []
    # Repeat until the user introduces the last function
    for val in range(0, N):
        # Get the function name and parameters (if required)
    	command = raw_input().split()
        # Separating of parameters and function name
    	i = int(command[1]) if len(command) > 1 else None
    	e = int(command[2]) if len(command) > 2 else None
    	command = command[0]
        # Selecting of function to apply on list
    	if command == opt[0] and i != None and e != None:
    		mi_list.insert(i, e)
    	elif command == opt[1]:
    		print(mi_list)
    	elif command == opt[2] and i != None:
    		mi_list.remove(i)
    	elif command == opt[3] and i != None:
    		mi_list.append(i)
    	elif command == opt[4]:
    		mi_list.sort()
    	elif command == opt[5]:
    		mi_list.pop()
    	elif command == opt[6]:
    		mi_list.reverse()