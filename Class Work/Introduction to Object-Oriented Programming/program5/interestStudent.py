##################################################################
# Student contributions to the interest calculator
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------

def greeting():
    print('This interest calculator will ask you to select an interest rate,followed by a principal value.  It will then calculate and display the principal, interest rate, and balance after one year.  You will then be invited to execute the process again or terminate.')

#---------------------------------------------------------------------------------

def getRate(choices):
    d = 0
    while d == 0:
        letters = ['A','B','C','D','E','F']
        c = 0
        print('Please select an interest rate:')
        for choice in choices:
            print(letters[c]+')', str(choice)+'%')
            c = c + 1
        RateAsk = 'Enter '+letters[0]+'-'+letters[c-1]+': '
        Choice = input(RateAsk)
        Choice = Choice.upper()
        if Choice in letters:
            rate = float(choices[letters.index(Choice)]/100)
            d = 1
        else:
            d = 0
            print('That is not a valid selection.')
    return rate

#---------------------------------------------------------------------------------

def getPrincipal(limit):
    a = 0
    while a == 0:
        e = 0
        prin = input('Enter the principal (limit '+str(limit)+'): ')
        if '$' in prin:
            prin = prin[1:]
        prin = float(prin)
        if prin > limit:
            print('The principal can be at most '+str(limit)+'.')
            e = 1
        if 0 >= prin:
            print('You must enter a positive amount.')
            e = 1 
        if round(prin,2) < prin:
            print('The principal must be specified in dollars and cents.')
            e = 1
        if e == 0:
            prin = round(prin,2)
            a = 1
    prin = float(prin)
    return prin

#---------------------------------------------------------------------------------

def computeBalance(principal, rate):
    balance = principal + (principal * rate)
    return balance

#---------------------------------------------------------------------------------

def displayTable(principal, rate, balance):
    print('Initial Principal   Interest Rate   End of Year Balance')
    print('=======================================================')
    print(f'{principal:<20}{rate:<16}{balance:19}')

#---------------------------------------------------------------------------------

def askYesNo(prompt):
    b = 0
    while b == 0:
        ans = input('Another Computation [y/n]? ')
        ans = ans.lstrip()
        if ans[0] == 'y' or ans[0] == 'Y':
            b = 1
            return True
        if ans[0] == 'n' or ans[0] == 'N':
            b = 1
            return False
        else:
          b = 0  

#---------------------------------------------------------------------------------
