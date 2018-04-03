# -*- coding: utf-8 -*-
"""
TTT F       TCT S       TAT Y       TGT C   
TTC F       TCC S       TAC Y       TGC C   
TTA L       TCA S       TAA end     TGA end   
TTG L       TCG S       TAG end     TGG W   

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
  
  listT = [] 
  listTa = []
  listC = [] 
  listCa = []
  listA = [] 
  listAa = []
  listG = [] 
  listGa = []

  spaceCount = 0

  #Comprueba si tienen la misma longitud las 4 cadenas
  if aasSize == c1Size and c1Size == c2Size and c2Size == c3Size:
    print("Same lenght.")
  else:
    print("Not same lenght.")
    
  #Obtiene el aminoacido y forma el codon basandose en el mismo indice
  for i in range(len(aas)):
    codon = ""
    aasL = aas[i]
    c1L = c1[i]
    c2L = c2[i]
    c3L = c3[i]
    codon += c1L + c2L + c3L
    
    #Sustituye el simbolo * por end
    if aasL == "*":
      aasL = "end"
      
    #Clasifica los codones en función de la primera letra
    if c1L == "A":
      listA.append(codon) 
      listAa.append(aasL)
    elif c1L == "T":
      listT.append(codon)
      listTa.append(aasL)
    elif c1L == "C":
      listC.append(codon)
      listCa.append(aasL)
    else:
      listG.append(codon)
      listGa.append(aasL)
    
    def printDictList(codonList, aaList):
      spaceCount = 0
      for i in range(len(codonList)):
        spaceCount += 1
        if aaList[i] == "end":
          print(codonList[i], aaList[i], end = "  ")
        else:
          print(codonList[i], aaList[i], end = "    ")

        if spaceCount%4 == 0:
          print("")
      print("")

  printDictList(listT, listTa)
  printDictList(listC, listCa)
  printDictList(listA, listAa)
  printDictList(listG, listGa)

#main
getCodonTable(chainP, chain1, chain2, chain3)


