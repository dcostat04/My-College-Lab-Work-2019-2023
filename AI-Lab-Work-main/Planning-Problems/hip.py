print("Travelling by 1.Bus 2.Train 3.Car" )
actions=["select destination"]
option1=[
    {
        "actions":"go by bus"
    },
    {
        "actions":"go by Train"
    },
    {
        "actions":"go by Car"
    }
]
option2=[
    {
        "actions":"Book ticket Online"
    },
    {
        "actions":"Book ticket at Stop"
    }
]
option3=[
    {
        "actions":"Refil the Fuel"
    }
]
option4=[
    {
        "actions":"Start Travel"
    },
    {
        "actions":"Reach Destination"
    }
]
var1=int(input("Select 1,2,3:"))
if var1 ==1:
    actions.append(option1[0]["actions"])
    var2=int(input("Select 1.Book ticket Online 2.Book ticket at Stop:\n"))
    if var2==1:
        actions.append(option2[0]["actions"])
        actions.append(option4[0]["actions"])
        actions.append(option4[1]["actions"])
    else:
        actions.append(option2[1]["actions"])
        actions.append(option4[0]["actions"])
        actions.append(option4[1]["actions"])
elif var1 == 2:
    actions.append(option1[0]["actions"])
    var2=int(input("Select 1.Book ticket Online 2.Book ticket at Stop:\n"))
    if var2==1:
        actions.append(option2[0]["actions"])
        actions.append(option4[0]["actions"])
        actions.append(option4[1]["actions"])
    else:
        actions.append(option2[1]["actions"])
        actions.append(option4[0]["actions"])
        actions.append(option4[1]["actions"])
else:
    actions.append(option1[2]["actions"])
    actions.append(option3[0]["actions"])
    actions.append(option4[0]["actions"])
    actions.append(option4[1]["actions"])

print(actions)
    

