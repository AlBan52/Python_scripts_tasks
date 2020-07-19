from transliterate import translit
from num2words import num2words

print(translit('''Ladies and gentlemen, I'm 78 years old and I finally
got 15 minutes of fame once in a lifetime and I guess that this is mine.
People have also told me to make these next few minutes escruciatingly
embarrassing and to take vengeance of my enemies. Neither will happen.''', 'ru'))
print(translit('''More than 3 years ago I moved to Novo-Novsk, but worked
on new Magnetic Storage for last 40. When I was 8...''', 'ru'))
print()

age = "78 - "
trans = translit(num2words(78, lang='en'), 'ru')
print(age + trans)
speech_time = "15 -"
trans = translit(num2words(15, lang='en'), 'ru')
print(speech_time + trans)
moved = "3 -"
trans = translit(num2words(3, lang='en'), 'ru')
print(moved + trans)
worked = "40 -"
trans = translit(num2words(40, lang='en'), 'ru')
print(worked + trans)
was = "8 -"
trans = translit(num2words(8, lang='en'), 'ru')
print(was + trans)
