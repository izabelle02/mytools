PI_INT = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
E_INT = '7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'

def pi_real(num):
    print('3,', end='')
    for i in range(num):
        print(PI_INT[i], end='')
    return None

def e_real(num):
    print('3,', end='')
    for i in range(num):
        print(E_INT[i], end='')
    return None