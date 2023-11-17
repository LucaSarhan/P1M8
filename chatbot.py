import re

def go_to1(local):
    phrase_conclusion = "Atualiza no site da empresa"
    for loc in local[0]:
        if loc:
            phrase_conclusion += f"{loc} "
    
    return phrase_conclusion

def go_to2(local):
    phrase_conclusion = "Voce ve o status do pedido no site da empresa"
    for loc in local[0]:
        if loc:
            phrase_conclusion += f"{loc} "
    
    return phrase_conclusion

dict_intent = {
    r"\b(?:[Qq]uero|[Cc]omo|[Mm]etodo|[Mm]étodo|[Pp]reciso)\s?(?:posso|atualizar|mudar|de)\s?(?:pagamento|atualizar|[aà]|minha)\s?(meu|forma|desatualizado|informa[cç][oõ]es)\s?(?:cart[aã]o|de)?\s?(?:pagamento|de)?\s?(?:cr[eé]dito|,)?\s?(?:o)?\s?(?:que)?\s?(?:fazer)?(\d*)", "go_to1" }

dict_action = {
    "go_to1": go_to1,
}

dict_intent2 = {
    r"\b(?:[Qq]uero|[Cc]omo|[Oo]nde|[Ss]tatus)\s?(?:vejo|fa[cç]o|saber|de)\s?(?:o|para|onde|entrega)\s?(status|rastrear|est[áa]|,)\s?(?:do|meu|como)?\s?(?:meu|pedido|consultar)\s?(?:pedido)?\s?", "go_to2" }

dict_action2 = {
    "go_to2": go_to2,
}

def main():
    while True:
        send_command = input("Digite sua duvida ").lower()

        for key, value in dict_intent.items():
            pattern = re.compile(key)
            groups = pattern.findall(send_command)
            if groups:
                print(dict_action[value](groups))

        for key, value in dict_intent2.items():
            pattern = re.compile(key)
            groups = pattern.findall(send_command)
            if groups:
                print(dict_action2[value](groups))

        print()

if __name__ == "_main_":
    main()