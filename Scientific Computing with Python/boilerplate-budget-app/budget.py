import math
class Category:

    #initialize Class with defaults set to empty or 0.
    def __init__(self, name, ledger = None, credit = 0, debit = 0):
        if ledger is None:
            ledger = []
        self.name = name
        self.ledger = ledger
        self.credit = credit
        self.debit = debit

    #Deposits into credit and creates an entry in ledger
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.credit += amount

    #If credit is sufficient, adds to debit and creates a ledger entry with a negative amount 
    def withdraw(self, amount, description = ""):
        if amount <= self.credit + self.debit:
            self.ledger.append({"amount": -amount, "description": description})
            self.debit -= amount
            return True
        else: return False

    #Get the current balance
    def get_balance(self):
        return self.credit + self.debit

    #Transfers an amount to the TARGET budget category
    def transfer(self, amount, target):
        if amount <= self.credit + self.debit:
            self.withdraw(amount, "Transfer to " + target.name)
            target.deposit(amount, "Transfer from " + self.name)
            return True
        else: return False

    #Check if an amount is greater than current balance. Returns true or false
    def check_funds(self, amount):
        if amount <= self.credit + self.debit:
            return True
        else: return False

    #Create print output
    def __str__(self):
        max_len = 30
        name_len = len(self.name)
        num_fill = int((max_len - name_len) / 2)
        title = "*" * num_fill + self.name + "*" * num_fill + "\n"
        body = ""

        for items in self.ledger:
            len_desc = len(items["description"])
            len_amt = len("{:.2f}".format(items["amount"]))

            if len_desc > 23:
                trunc_desc = items["description"][0:23]
                body += trunc_desc + " " * (7 - len_amt) + "{:.2f}".format(items["amount"]) + "\n"
            else:
                body += items["description"] + " " * (30 - len_desc - len_amt) + "{:.2f}".format(items["amount"]) + "\n"
    
        return title + body + "Total: " + "{:.2f}".format(self.credit + self.debit)


def create_spend_chart(categories):

    #initialize vars
    rows = 0
    finalStr = ""
    name = []
    spent = []

    #Find % of each category
    for category in categories:
        name.append(category.name) #add category to name array
        net = 0 #reset net to 0 for each new category
        
        #Calculate spending for current category
        for item in category.ledger:
            if item["amount"] < 0:
                net += item["amount"]
        
        #Store spending for current category
        spent.append(net)

    #calculate total spent across all categories and initialize array to store percentages
    totalSpent = sum(spent)
    pCent = []

    #Create array containing category spend percentages
    for item in spent:
        pCent.append(math.floor(item / totalSpent * 10) * 10)

    lines = []
    pLines = "Percentage spent by category\n"

    #Create array for numeric percentages on a 10-scale
    for i in reversed(range(11)):
        num = i * 10
        gLine = " "

        for p in pCent:
            if p >= num:
                gLine += "o  "
            else: gLine += "   "
        lines.append(" " * (3 - len(str(num))) + str(num) + "|" + gLine)

    for line in lines:
        pLines += line + "\n"

    pLines += " " * 4 + "-" * (1 + 3 * len(categories))

    #determine longest category name and store in rows var
    for category in categories:
        #print("category:",category)
        rows = max(rows, len(category.name))

    #there will be 1 column per category
    cols = len(categories)

    #initialize string array with length = rows
    output = ["" for i in range(rows)]

    #verticalize the category names
    for i in range(cols):
        for j in range(len(name[i])):
            #print(j,i)
            while i - len(output[j]) >= 1:
                output[j] += " "
            output[j] += name[i][j]

    #print("output:",output)

    for i in range(len(output)):
        finalStr += "\n" + " " * 5 + "  ".join(output[i]) + "  "
        #print("i =",i,"finalStr:\n"+finalStr+"|")

    pLines += finalStr

    return pLines