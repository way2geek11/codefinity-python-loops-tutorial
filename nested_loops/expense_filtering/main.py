# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []
processed_expenses1 = []
i=0
i2=0
s='Cheap'
while i < len(travel_costs):
    i2=0
    expense=[]
    while i2 < len(travel_costs[i]):
        cost=travel_costs[i][i2]
        if travel_costs[i][i2] <= 100:
            #travel_costs[i][i2]='Cheap'
            expense.append('Cheap')
            #processed_expenses.append(expense)
            #i2+=1
        else: 
            expense.append(cost)
            #processed_expenses.append(expense)
        i2 += 1
    processed_expenses.append(expense)
    i += 1
    
    
            
            



# Testing
print('Processed Travel Expenses:', processed_expenses)