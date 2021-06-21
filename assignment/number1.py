def countBase (self): 
    print ('A: {} '.format(self.count ("A"))) 
    print ('T: {} '.format(self.count ("T")))
    print ('G: {} '.format(self.count ("G")))
    print ('C: {} '.format(self.count ("C")))
print ("Input your DNA")
dna = input()
countBase (dna)
