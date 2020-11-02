import fileinput, math

# Lee entradas
lines = []
for line in fileinput.input():
    lines.append(line)


# Vector S
S = [
41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6, 19,
98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188, 76, 130, 202,
30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24, 138, 23, 229, 18,
190, 78, 196, 214, 218, 158, 222, 73, 160, 251, 245, 142, 187, 47, 238, 122,
169, 104, 121, 145, 21, 178, 7, 63, 148, 194, 16, 137, 11, 34, 95, 33,
128, 127, 93, 154, 90, 144, 50, 39, 53, 62, 204, 231, 191, 247, 151, 3,
255, 25, 48, 179, 72, 165, 181, 209, 215, 94, 146, 42, 172, 86, 170, 198,
79, 184, 56, 210, 150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241,
69, 157, 112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2,
27, 96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197, 234, 38,
44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65, 129, 77, 82,
106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123, 8, 12, 189, 177, 74,
120, 136, 149, 139, 227, 99, 232, 109, 233, 203, 213, 254, 59, 0, 29, 57,
242, 239, 183, 14, 102, 88, 208, 228, 166, 119, 114, 248, 235, 117, 75, 10,
49, 68, 80, 180, 143, 237, 31, 26, 219, 153, 141, 51, 159, 17, 131, 20]

# convertir en ascii y padding
def conv(entrada):
    hexa = [ord(c) for c in entrada]
    paddingVal = (16 - (len(hexa) % 16))
    padding = paddingVal * [paddingVal]
    hexa += padding
    return hexa 

def check(mensaje):
    # Valores iniciales checksum
    checksum = 16 * [0]
    l = 0
    N = len(mensaje)
    bloques = math.ceil(N/16)
    global S
    for i in range (bloques):
        for j in range(16):
            c = mensaje[16*i + j] ^ l
            checksum[j] = l = checksum[j]^S[c]
    return checksum

def md2(mensaje, digesto):
    bloques = math.ceil(len(mensaje)/16)
    for i in range(bloques):
        for j in range(16):
            digesto[j+16]=mensaje[16*i + j]
            digesto[j+32]=digesto[j+16]^digesto[j]
        t = 0
        for j in range(18):
            for k in range(48):
                t = digesto[k] = digesto[k]^S[t]
            t = (t+j)%256
    res = ""
    for x in digesto[0:16]:
        res += '{:02X}'.format(x)
    return res



# Obtener las llaves y texto plano, limpiando el input
entrada = lines[0].replace("\n","")

# Inicializar digesto
digesto = 48*[0]

# Algoritmo main
mensaje = conv(entrada)
checkS = check(mensaje)
mensaje += checkS
cifrado = md2(mensaje, digesto)
print(cifrado.upper())