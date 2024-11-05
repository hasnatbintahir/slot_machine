import random


#declairing constants
MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3
machine_symbols = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

machine_values = {
    "A":5,
    "B":8,
    "C":2,
    "D":4
}

def check_winnings(columns, lines, bet, values):
    global wallet_balance
    winnings = 0
    for line in range(lines):
        symbol_check = columns[0][line]
        for column in columns:
            if column[line] != symbol_check:
                break
        else:
            winnings += values[symbol_check]*bet
            wallet_balance += winnings
    return winnings
            
            
    

symbols = []
for symbol,count in machine_symbols.items():
    for _ in range(count):
        symbols.append(symbol)

wallet_balance = 0

# deposit function to deposit amount from user and then add them in wallet
def deposit():
    #running while loop until getting positive input int from user
    while True:
        amount = input("Enter the amount you want to Deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                global wallet_balance
                wallet_balance = amount + wallet_balance
                break
            else:
                print("Enter a Valid Amount!")
        else:
            print("Invalid Input!")
    return wallet_balance

#inquiring bet
def get_bet():
    while True:
        lines = input(f"Enter the number of lines wanna bet: ({MIN_LINES}-{MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter lines between {MIN_LINES} & {MAX_LINES}")
        else:
            print("Invalid Input!")
            
    while True:
        global wallet_balance
        bet = input("Enter the amount you wanna bet: () ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                if ((bet*lines) <= wallet_balance):
                    wallet_balance -= (bet*lines)
                    break
                
                else:
                    print(f"You are trying to bet for {lines*bet} but your Balance is {wallet_balance}")
                    while True:
                        # the user gives more bet now asking user to ask wether he wanna deposit or bet another amount
                        query = input(f"Press d for deposit more or b for another bet! ")
                        if query.lower() == "d":
                            deposit()
                            break
                        elif query.lower() == "b":
                            break
                        else:
                            print("Invalid Input! ")
                        
            else:
                print(f"Enter bet between {MIN_BET} & {MAX_BET}")
        else:
            print("Invalid Input!")
            
    return lines,bet

    
def get_slot_machine_spin(rows, clos, symbols):
    columns = []
    for _ in range(rows):
        column = []
        symbol_duplicate = symbols[:]
        for _ in range(clos):
            symb = random.choice(symbol_duplicate)
            symbol_duplicate.remove(symb)
            column.append(symb)
        columns.append(column)
    return columns


def print_slot(column):
    for row in range(len(column[0])):
        for i,col in enumerate(column):
            if i != (len(column)-1):
                print(f"{column[i][row]}",end=" | ")
            else:
                print(f"{column[i][row]}")
                
            
   
             
        
# before
# A,D,H   
# B,E,I 
# C,F,J   
  
# after          
# A,B,C
# D,E,F
# H,I,J            
    


def main():
    amount = deposit()
    while True:
        querry = input("press y for play and q to quit: (y/q) ")
        if querry.lower() == "q":
            break
        else:
            lines, bet = get_bet()
            slots = get_slot_machine_spin(ROWS,COLS,symbols)
            print_slot(slots)
            winner = check_winnings(slots, lines,bet, machine_values )
            print(f"You won {winner}$ and your balance is now {wallet_balance}.")
            

    
main()

