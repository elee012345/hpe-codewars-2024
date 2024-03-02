chemString = input().split('\t')
formula = chemString[0]
newFormula = ""
formulaLineTwo = ''
for character in formula:
    if character.isnumeric():
        formulaLineTwo += character
        newFormula += (" ")
    else:
        formulaLineTwo += " "
        newFormula += (character)
print(newFormula)
print(formulaLineTwo)