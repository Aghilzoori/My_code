def mortab(vorodi):
    zkhire = ""
    for i in vorodi:
        if i.isupper():
            zkhire += " "
        zkhire += i
    return "    " + zkhire
print(mortab("AghilZoori"))
print(mortab("<UNK>"))
print(mortab("<UNK>"))
print(mortab("<UNK>"))