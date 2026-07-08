colombian = int(input("how much do you left in pesos?"))
usd_from_colombia = colombian*0.00030
peruvian = int(input("how much do you left in soles"))
usd_from_peruvia = peruvian*0.29
brazilian = int(input("how much do you left in reais"))
usd_from_brazilia = brazilian*0.19
total = (usd_from_colombia + usd_from_peruvia + usd_from_brazilia)
print(total)
