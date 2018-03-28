# -*- coding: utf-8 -*-
"""
TTT F       TCT S       TAT Y       TGT C   
TTC F       TCC S       TAC Y       TGC C   
TTA L       TCA S       TAA end       TGA end   
TTG L       TCG S       TAG end       TGG W   

CTT L       CCT P       CAT H       CGT R   
CTC L       CCC P       CAC H       CGC R   
CTA L       CCA P       CAA Q       CGA R   
CTG L       CCG P       CAG Q       CGG R   

ATT I       ACT T       AAT N       AGT S   
ATC I       ACC T       AAC N       AGC S   
ATA I       ACA T       AAA K       AGA R   
ATG M       ACG T       AAG K       AGG R   

GTT V       GCT A       GAT D       GGT G   
GTC V       GCC A       GAC D       GGC G   
GTA V       GCA A       GAA E       GGA G   
"""
# Exercise C


#Variables locales
chainP = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
chainS = ""
chain1 = "TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
chain2 = "TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG"
chain3 = "TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG"

#Funciones
def getCodonTable (aas, c1, c2, c3):
  aasSize = len(aas)
  c1Size = len(c1)
  c2Size = len(c2)
  c3Size = len(c3)
  
  aasL = ""
  c1L  = ""
  c2L  = ""
  c3L  = ""
  
  dicT = {}
  dicA = {}
  dicG = {}
  dicC = {}
  
  #Comprueba si tienen la misma longitud las 4 cadenas
  if aasSize == c1Size and c1Size == c2Size and c2Size == c3Size:
    print("Same lenght.")
  else:
    print("Not same lenght.")
    
  for i in range(len(aas)):
    print(i)
    codon = ""
    aasL = aas[i]
    c1L = c1[i]
    c2L = c2[i]
    c3L = c3[i]
    codon += c1L + c2L + c3L
    print(codon)
    
    if aasL == "*":
      aasL = "end"
      
    if c1L == "A":
      dicA[codon] = aasL
    elif c1L == "T":
      dicT[codon] = aasL
    elif c1L == "C":
      dicC[codon] = aasL
    else:
      dicG[codon] = aasL
    
  print("Diccionario A", dicA)
  print("Diccionario T", dicT)
  print("Diccionario C", dicC)
  print("Diccionario G", dicG)
#main
getCodonTable(chainP, chain1, chain2, chain3)


