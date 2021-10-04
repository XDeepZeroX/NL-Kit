from razdel import sentenize
import regex


def tokenization(text: str) -> list[str]:
    '''
    Разбиение текста на предложения
    '''
    return list(map(lambda x: x.text, sentenize(text)))

def replace_time(text, repl='(TBD)'):
    '''
    Поиск времени в фразе и замена его на (TBD) 
    '''
    # pattern = regex.compile(r'(^|\s)((24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])(:[0-5][0-9])?)(\s|$)', regex.S)
    pattern = regex.compile(
        r'(?<=^|[\s\.,\'\"!?\n])((24:00|2[0-3]:[0-5]?[0-9]|[0-1]?[0-9]:[0-5][0-9])(:[0-5][0-9])?)(?=[\s\.,\'\"!?\n]|$)', regex.MULTILINE)
    return regex.sub(pattern, repl, text)
    # for find in list(regex.finditer(pattern, text))[::-1]:
    #     text = text[:find.start()] + f'{find.group(1)}{repl}{find.group(5)}' + text[find.end():]
    # return text


def summ_purchase(text, word_before_amount='куплено', word_after_cost='руб'):
    '''
    Расчет суммы 

    word_before_amount - слово после которого находится число с количеством
    word_after_cost - слово перед которым находится число со стоимостью одного елемента/товара/т.п.
    '''
    amount = regex.search(fr'{word_before_amount}\s+(\d+([\.,]\d+)?)', text)
    cost = regex.search(fr'(\d[\d _]*([\.,]\d+)?)\s+{word_after_cost}', text)
    if amount == None or cost == None:
        return None

    amount = float(regex.sub('[_ ]', '', amount.group(1)).replace(',', '.'))
    cost = float(regex.sub('[_ ]', '', cost.group(1)).replace(',', '.'))

    return round(amount * cost, 4)
