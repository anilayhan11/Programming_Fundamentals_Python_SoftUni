def loading_bar(num):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        percents = num // 10
        dots = 10 - percents
        return f"{num}% [{'%' * percents}{'.' * dots}]\nStill loading..."


number = int(input())
print(loading_bar(number))
