# pets={
#     'dog':{'zxx':'zq','zzz':'222','aaa':'333'},
#     'cat':{'qqq':'444','www':'123'}
# }
# for a,b in pets.items():
#     for c,d in b.items():
#         print(f'{d} is {c} de {a}')
# a=int(input("qsr："))
# print(a)
prompt = "\nPlease enter the name of a city you have visited:" 
prompt += "\n(Enter 'quit' when you are finished.) " 
while True: 
    city = input(prompt) 
    if city == 'quit': 
        break 
    else: 
        print(f"I'd love to go to {city.title()}!")