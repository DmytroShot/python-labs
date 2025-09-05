data = input("->")

def calc_with_priority(data):
    
    # updated_data = data
    while("*" in data or "/" in data):
        res=[]
        operator=" "
        num=""
        priority_ops = "*/"
        for symbol in data:
            if symbol.isdigit():
                num+=symbol
            else:
                if symbol in priority_ops:
                    res.append(int(num))
                if operator in priority_ops:
                    data = data.replace(str(res[0])+operator+num,str(make_operation(operator,res[0],int(num))))
                
                num=""
                operator=symbol
        if num!="" and operator in priority_ops:
            data = data.replace(str(res[0])+operator+num,str(make_operation(operator,res[0],int(num))))
    return data

def calc_without_priority(data):
    res=[]
    operator=""
    num=""
    for symbol in data:
        if symbol.isdigit():
            num+=symbol
        else:
            res.append(int(num))
            num=""
            if len(res)>1:
                res = [make_operation(operator,res[0],res[1])]
            operator=symbol
        
    return make_operation(operator, res[0], int(num)) if num!="" else res[0]

def calc(data):
    res = 0
    updated_data = data
    if "*" in data or "/" in data:
        updated_data = calc_with_priority(data)
    res = calc_without_priority(updated_data)
    return res

def make_operation(operator,x,y):
    res = 0
    if operator == "+":
        res = x + y
    elif operator == "-":
        res = x - y
    elif operator == "*":
        res = x * y
    elif operator == "/" and y!=0:
        res = x // y
    else:
        print("error")
    return res
    
        
print(calc(data))