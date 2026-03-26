def chesseshop(kind,*argument ,**keyword):
    print(f"do you have any {kind} chess pieces?")
    print(f"we need {argument} chess pieces")

    for arg in argument:
     print(arg)
     print("-" * 40)
    for kwarg in keyword:
        print(kwarg,":",keyword[kwarg])


chesseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")