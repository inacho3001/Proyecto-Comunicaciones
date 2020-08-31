#Abrir archivo txt para transmitir
with open('info.txt','r') as rf:
    info = rf.read()
  
#Convertir a ASCII
results_in_ASCII = list(info.encode(encoding='us-ascii'))

#Convertir a binario
result_in_binary = []
for symbol in results_in_ASCII:
    result_in_binary.append((bin(symbol)[2:]).zfill(8))

#Pasar todos los bits a un mismo canal de transmision
channel = []
for bits in result_in_binary:
    for i in range(len(bits)):
        channel.append(bits[i])

#Hasta aqui llega la codificacion, los caracteres se envian en codigo ascii en paquetes de 8 bits

#Decodificar los bits en paquetes de 8 bits
decoded_bits = []
for i in range(int(len(channel)/8)):
    aux = ''.join(channel[i*8:(i*8)+8])
    decoded_bits.append(aux)


#Decodificar mensaje
decoded_message = ''
for bits in decoded_bits:
    n = int(bits, 2)
    decoded_message += n.to_bytes(1, 'big').decode('us-ascii')


#Escribir el archivo decodificado y transmitido
with open('transmision.txt','w') as wf:
    wf.write(decoded_message)

print('Transmitiendo ...')
print('Hecho!')