"""Спросите пользователя, идет ли дождь. Преобразуйте его ответ к нижнему регистру.
Если пользователь ответит «yes», спросите, ветрено ли на улице.
Если пользователь ответит «yes» и на второй вопрос, выведите сообщение «It is too windy for an umbrella»;
в противном случае выведите сообщение «Take an umbrella».
Если же пользователь не дал положительного ответа на первый вопрос, выведите сообщение «Enjoy your day»
"""

answer = input("Идет ли дождь?\n").lower()

if answer == "yes":
    answer = input("Ветрено ли на улице?\n").lower()
    print("It is too windy for an umbrella" if answer == "yes" else "Take an umbrella")
else:
    print("Enjoy your day")