import random

pierwsze = [37, 41, 43, 47, 53, 59, 61, 67, 71]

def nwd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

def reverse_mod(a,n):
    p0 = 0
    p1 = 1
    a0 = a
    n0 = n
    q  = n0//a0
    r  = n0%a0
    while r > 0:
        t = p0-q*p1
        if t >= 0:
            t = t%n
        else:
            t = n-((-t)%n)
            p0 = p1
            p1 = t
            n0 = a0
            a0 = r
            q  = n0//a0
            r  = n0%a0
    return p1

def pot_mod(a,w,n):
    pot,wyn,q = a,1,w
    while q > 0:
        if q%2 != 0:
            wyn = (wyn*pot)%n
        pot = (pot*pot)%n
        q //= 2
    return wyn


#p = pierwsze[random.randrange(len(pierwsze))]
#q = pierwsze[random.randrange(len(pierwsze))]

p = int(input('Podaj p: '))
q = int(input('Podaj q: '))

#p = 13
#q = 17

phi = (p-1)*(q-1)
n = p*q

e = 3
while nwd(e,phi) != 1:
    e += 2

d = reverse_mod(e,phi)

print(f'publiczny ({e},{n})')
print(f'prywatny ({d},{n})')


number_to_script = int(input('Do zaszyfrowania: '))

#number_to_script = 12
#print(f'Do zaszyfrowania: {number_to_script}')
number_scritp = pot_mod(number_to_script,e,n)
print(f'zaszyfrowane: {number_scritp}')
number_descript = pot_mod(number_scritp,d,n)    
print(f'Odszyfrowane: {number_descript}')