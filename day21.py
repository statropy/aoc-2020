#day21.py

ingredients = set()
alergens = set()
foods = []
allalergens = {}

with open('input21.txt', 'r') as f:
    for line in f:
        ingr, aler = line.strip().split(' (contains ')
        ingr = ingr.split(' ')
        aler = aler[:-1].replace(' ', '').split(',')
        ingredients.update(ingr)
        alergens.update(aler)
        foods.append((set(ingr),set(aler)))

for a in alergens:
    allalergens[a] = ingredients.copy()

def testz(a):
    could = set()
    for fi, fa in foods:
        if a in fa:
            if len(could) == 0:
                could = set(fi)
            else:
                could &= set(fi)
    return list(could)

found = {}

while len(allalergens) > 0:
    count -= 1
    this_round = {}
    for a in allalergens:
        possible = testz(a)
        if len(possible) == 1:
            this_round[a] = possible[0]
            #print('found', a, possible[0])

    for a,v in this_round.items():
        del allalergens[a]
        found[a] = v
        for az in allalergens:
            allalergens[az].discard(v)
        for fi, fa in foods:
            fi.discard(v)

print(sum([len(fi) for fi, fa in foods]))
print(','.join([found[k] for k in sorted(found.keys())]))
