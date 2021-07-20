duration = int(input("Продолжительность секунд:"))
minutes=duration//60             # минуты
hours=duration//3600             # часы
days=duration//86400             # дни
print (days, "день", hours%24, "час", minutes%60, "мин", duration%60, "сек")
