
ages = {
    'Archaea': 2800,
    'Proterozoic': 635,
    'Paleozoic': 300,
    'Mesozoic': 145
}


while year := input():
    year_mln = int(year) / 1000
    for period, years in ages.items():
        if year_mln >= years:
            print(period)
            break
    else:
        print('Cenozoic')
