# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:11:42 2020

@author: YOULA Mohamed
"""
# Fonction pour récupérer les éléments de chaque ligne   
def parse_file(ch):
    if ch[0]=="<":
        [r1, p1] = ch.split("<", 1) #les sujets sont soit des URIs entre chevrons,
        [r2, p2] = p1.split(">", 1) 
    else:
        [r2, p2] = ch.split(" ", 1) # soit des noeuds anonymes,
       
    [r3, p3] = p2.split("<", 1) #les prédicats sont des URIs entre chevrons.
    [r4, p4] = p3.split(">", 1)
          
    if p4.find('<')==1:
        [r5, p5] = p4.split("<", 1) #les objets sont soit des URIs entre chevrons,
        [r6, p6] = p5.split(">", 1)  
    elif p4.find('"')!=-1:
        [r5, p5] = p4.split('"', 1)#soit des littéraux,
        [r6, p6] = p5.split('"', 1)# soit des noeuds anonymes.
    else:
        [r6, p6] = p4.split(' ', 1) # pour la recherche des tags 
       
    values=[r2,r4,r6,p6]    
    return values

#Fonction pour récupérer chaque éléments (sujet,prédicat,objet ) d'une requête écrite sous forme de triplet.
#les  differentes conditions (if ..., elif ...) correspondent chacune à une combinaison du triplet (sujet,prédicat,objet) dans une requête donnée.     

def parse_requet(R):
    if R=="? ? ?":
          return ['?','?','?'] 
      
    elif R[-4:]==" ? ?" and R[:-4].find('<')==0:
         rr=R[:-4][:-1][1:]
         return [rr,'?','?'] 
     
    elif R[0]=='?' and R[2] =='<' :
             [r1, p1] = R.split("<", 1)
             [r2, p2] = p1.split(">", 1)
             if r2 !='?' and  R[-4:][:-2]=='?@':
                return ['?',r2,R[-4:]]
             elif r2 !='?' and  p2==' ?':
                  return ['?',r2,'?']
    elif R[0]=="<" and R[1:].find('?')!=-1 and R[-1]=='>':
       [r1, p1] = R.split("<", 1)
       [r2, p2] = p1.split(">", 1)
       [r3, p3] = p2.split("<", 1)
       [r4, p4] = p3.split(">", 1)
       return [r2,'?',r4]         
                
    elif R[0]=="_" and R[:-1].find('>')==-1 and R[-1]=='>':
       [r1, p1] = R.split(" ", 1)
       [r2, p2] = p1.split("<", 1)
       [r3, p3] = p2.split(">", 1)
       return [r1,'?',r3]
    elif R[0]=='?' and R[2] =='?' and R[4:][0]=='<': 
         return ['?','?',R[4:][1:][:-1]]
           
    elif R[0]=='<' and R[1:].find("<")!=-1 and R[-1]=='?':
        [r1, p1] = R.split("<", 1)
        [r2, p2] = p1.split(">", 1)
        [r3, p3] = p2.split("<", 1)
        [r4, p4] = p3.split(">", 1)
        return [r2,r4,'?']
    elif R[0]=="_" and R.find('<')!=-1 and R[-1]=='?':
       [r1, p1] = R.split(" ", 1)
       [r2, p2] = p1.split("<", 1)
       [r3, p3] = p2.split(">", 1)
       return [r1,r3,'?']  

    elif R[0]=='<' and R[-1]=='>':
        [r1, p1] = R.split("<", 1)
        [r2, p2] = p1.split(">", 1)
        [r3, p3] = p2.split("<", 1)
        [r4, p4] = p3.split(">", 1)
        [r5, p5] = p4.split("<", 1)
        [r6, p6] = p5.split(">", 1)
        return [r2,r4,r6] 
    elif R[0]=="_" and R[:-1].find('>')!=-1 and R[-1]=='>':
       [r1, p1] = R.split(" ", 1)
       [r2, p2] = p1.split("<", 1)
       [r3, p3] = p2.split(">", 1)
       [r4, p4] = p3.split("<", 1)
       [r5, p5] = p4.split(">", 1)
       return [r1,r3,r5]
    elif R[0]=='<' and R[-4:][:-2]=='?@':
        [r1, p1] = R.split("<", 1)
        [r2, p2] = p1.split(">", 1)
        [r3, p3] = p2.split("<", 1)
        [r4, p4] = p3.split(">", 1)
        [r5, p5] = p4.split(" ", 1)
        return [r2,r4,p5]            
    elif R[0]=='?' and R[2] =='?' and R[-4:][:-2]=='?@': 
        return ['?','?',R[-4:]]
      
    elif R[0]=="?" and R[1:].find('?')==-1 and R[-1]=='>':
       [r1, p1] = R.split("<", 1)
       [r2, p2] = p1.split(">", 1)
       [r3, p3] = p2.split("<", 1)
       [r4, p4] = p3.split(">", 1)
       return ['?',r2,r4]
    #############################
    elif R[0]=="?" and R[2]=='?' and R[4:].find("@")!=-1:
        [r1, p1] = R.split('"', 1)
        return ['?','?',p1]
    
    elif R[0]=="?" and R[2]=='?' and R[4:].find("^^")!=-1:
        [r1, p1] = R.split('"', 1)
        return ['?','?',p1]
    
    elif R[0]=="?" and R[2]=='?' and R[-1]=='"':
         [r1, p1] = R.split('"', 1)
         [r2, p2] = p1.split('"', 1)
         return ['?','?',r2]
   
# Cette fonction permet de procéder à la recherche d'un triplet via  une requête 
# le split d'une requête  est comparé au split de toutes les lingne d'un ficher Ntriples.
# les lignes trouvées sont affichées et comptées. leur nombre est affiché à la fin.           
def request(cm,R):
    f=open(cm, "r")
    i=0
    for line in f:
         rl=parse_file(line)
         r=parse_requet(R)
         s,p,o=r[0],r[1],r[2]
         v=rl[2]+'"'+rl[3][:-2]
         idxv=v.find(o)      
         if s=='?' and p=='?' and o =='?':
            i=i+1
            print(line)
         elif s==rl[0] and p=='?' and o=='?':
            i=i+1
            print(line) 
         elif s=='?' and p==rl[1] and o=='?' :
            i=i+1
            print(line)
         elif s==rl[0] and p=='?' and o==rl[2]:
              i=i+1 
              print(line)
         elif s=='?' and p=='?' and o==rl[2]:
              i=i+1 
              print(line)
         elif s==rl[0] and p==rl[1] and o=='?':
              i=i+1 
              print(line)
         elif s=='?' and p==rl[1] and o==rl[2]:
            i=i+1
            print(line)     
         elif s==rl[0] and p==rl[1] and o==rl[2]:
            i=i+1
            print(line)            
         elif s==rl[0] and p==rl[1] and o[1:] in rl[3]:
              i=i+1 
              print(line)
         elif s=='?' and p=='?' and o[1:] in rl[3]:
              i=i+1 
              print(line)
         elif s=='?' and p==rl[1] and o[1:] in rl[3]:
              i=i+1 
              print(line)
                
         elif s=='?' and p=='?' and idxv==0:
              i=i+1 
              print(line)      
        
    print("---------------------------------------------------------------------------------------------")  
    print("Le nombre de triplets trouvés est: " + str(i))



# Fonction Main   
def main():
    """Le programme principal."""
     
    saisie1 = input('''Saisissez le chemin de votre fichier, sans les crochets " et '(Exemple: C:/Users/.../fichier.txt)  : \n''')
    chemin=str(saisie1)
    
    saisie2 = input('''Saisissez une requête, sans les crochets " et ' et sans espace à la fin (Exemple:? ? ?@en):\n ''')    
    R = str(saisie2) 
    
    request(chemin,R)
    print("Pour la requête: "+R) 

if __name__ == "__main__":
    main()




#chemin= C:/Users/YOULA Mohamed/Desktop/Web_sémantique/YOULA_Mohamed_Ntriples/gro.txt
           ###########  REQUETES ###########
           
# <http://wikiba.se/ontology#Dump> ? ?           
# ? <http://www.w3.org/2000/01/rdf-schema#label> ?@eu
# ? <http://www.w3.org/2000/01/rdf-schema#label> ?
# ? ? "motorrenganako"@eu          
#? <http://www.w3.org/2000/01/rdf-schema#label> ?



      





















