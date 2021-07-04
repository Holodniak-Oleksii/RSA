import time
import os
import psutil
start_time = time.time()
process = psutil.Process(os.getpid())
named = input("Введи що потрібно закодувати: ")
conter = 0
P = 53  # Вибираєм 2 простх чсила
Q = 59
Mod = P * Q
conter += 1
F = (P-1) * (Q-1)  # Теорема Ейлєра знаходимо її значення
conter += 1
cs = ""
inter = []
cry = []
wow = []
prime = []  # створюємо масиви для простих чисел
r_prime = []


# Алгорим Евкліда занходмо НСД у майбутьньому перевіряємо чи він рівен 1 (якщо так то це взаємо прості числа)
def evc(x, b):
    global conter
    while x != 0 and b != 0:
        if x > b:
            x = x % b
            conter += 1
        else:
            b = b % x
            conter += 1
    conter += 1
    return x + b


# За допомогою метода ord() пертворюємо текст у юнікод
def encrypt(text):
    global conter
    vav = []
    for syb in text:
        e_text = str(ord(syb))
        vav.append(e_text)
        conter += 1
    return vav


# За допомогою метода chr() перетворюємо юнікод у тест
def decrypt(n):
    global conter
    m = chr(n)
    conter += 1
    return m


# у циклові знаходим прості числа які менші за F
for num in range(2, F):
    prim = True
    for i in range(2, num):
        conter += 1
        if num % i == 0:
            prim = False
    if prim:
        conter += 1
        prime.append(num)

# Знаходмо взаємо прості числа для F
for rp in prime:
    v = evc(F, rp)
    if v == 1:
        conter += 1
        r_prime.append(rp)
e = r_prime[0]
i = 0
while True:  # За формулею знаходимо d (закриту експоненту) для приватного ключа
    i += 1
    if (i*e) % F == 1:
        d = i
        conter += 1
        break
print("Приватний ключ: ", "Закрита експонетна: ", d, "; Mood: ", Mod)
print("Публічний ключ: ", "Відкрита експонетна: ", e, "; Mood: ", Mod)

spy = encrypt(named)
# Перетвоюємо str мисив spy у int масив inter
for c in spy:
    var = int(c)
    conter += 1
    inter.append(var)
# Зашифровуємо введений тест
for zero in inter:
    z = pow(zero, e) % Mod
    conter += 1
    cry.append(z)
print("Ваше зашифроване повідомлення: ", cry)
# Розшифровуємо введений текс
for cou in cry:
    nan = pow(cou, d) % Mod
    conter += 1
    wow.append(nan)
print("Ваше розшифроване повідомення: ", wow)
# Переводи юнікод у тест
for gag in wow:
    ca = decrypt(gag)
    conter += 1
    cs += ca
print("Ваше повідомлення такє: ", cs)

print("Кількість дій: ", conter)
print("--- %s seconds ---" % (time.time() - start_time))
print(process.memory_info().rss, "bytes")
