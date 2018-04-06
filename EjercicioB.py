#Imports
import ../EjercicioC/EjercicioC.py as Ejc

#Variables
sequence1 = ""
sequence1Rna = ""
sequence1RnaRev = ""
sequence1RnaRevComp = ""
sequence2 = ""
sequence2Rna = ""
sequence2RnaRev = ""
sequence2RnaRevComp = ""
sequences = []
control1 = False
diffPairs = 0
##Variables para diccionario
aaChain = []
b1Chain = []
b2Chain = []
b3Chain = []

#Functions

#main

##Bucle donde se piden dos secuencias que sean iguales de longitud
while control1 == False:
  sequence1Name = input("Name the sequence: ")
  sequence1 = input("Insert the sequence: ")
  sequence2Name = input("Name the other sequence: ")
  sequence2 = input("Insert the other sequence: ")
  
  if len(sequence1) == len(sequence2):
    control1 = True
  else:
    print("Error, the chains are not equals.")

##Convertir a RNA
sequence1 = sequence1.upper()
sequence2 = sequence2.upper()
sequence1Rna = sequence1.replace("T", "U")
sequence2Rna = sequence2.replace("T", "U")

##Generar RNA inverso
for i in range(len(sequence1Rna)-1, -1, -1):
  sequence1RnaRev += sequence1Rna[i]
  sequence2RnaRev += sequence2Rna[i]

##Generar RNA inverso complementario
sequence1RnaRevComp = sequence1RnaRev.replace("A","u")
sequence1RnaRevComp = sequence1RnaRevComp.replace("U","a")
sequence1RnaRevComp = sequence1RnaRevComp.replace("C","g")
sequence1RnaRevComp = sequence1RnaRevComp.replace("G","c")
sequence1RnaRevComp = sequence1RnaRevComp.upper()
sequence2RnaRevComp = sequence2RnaRev.replace("A","u")
sequence2RnaRevComp = sequence2RnaRevComp.replace("U","a")
sequence2RnaRevComp = sequence2RnaRevComp.replace("C","g")
sequence2RnaRevComp = sequence2RnaRevComp.replace("G","c")
sequence2RnaRevComp = sequence2RnaRevComp.upper()

##Generar cadena aminoacidos
if len(sequence1)%3 == 0 and len(sequence2)%3 == 0:
  print("Cadena correcta.")
else:
  print("Cadena incorrecta.")

##Calcular porcentaje de diferencias 
for i in range(0,len(sequence1)):
  if sequence1[i] != sequence2[i]:
    diffPairs += 1

diffPerc = 100 - (((len(sequence1)-diffPairs) * 100) / len(sequence1))

print(sequence1Name + " vs " + sequence2Name + " has " + str(diffPairs)
        + " (" + str(diffPerc) + "%) differences in "
        + str(len(sequence1)) + " pb.")

##Guardar en diccionario
sequences = {"seq1":{"seqname":sequence1Name, "seq":sequence1, 
    "rna":sequence1Rna, "seqrev":sequence1RnaRev, 
    "seqrevcomp":sequence1RnaRevComp},
             "seq2":{"seqname":sequence2Name, "seq":sequence2, 
    "rna":sequence2Rna, "seqrev":sequence2RnaRev, 
    "seqrevcomp":sequence2RnaRevComp}}

print(sequence1)
print(sequence1Rna)
print(sequence1RnaRev)
print(sequence1RnaRevComp)
print(sequences.items())
