class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1, "V": 5, "X": 10 , "L": 50, "C": 100, "D": 500, "M": 1000,
                "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        integer = 0
        s_length = len(s)
        final = s_length-1
        index = 0
        while(index < s_length):
            if (s[index]=="I" and index !=final and s[index+1]=="V"):
                integer += roman["IV"]
            elif (s[index]=="I" and index !=final and s[index+1]=="X"):
                integer+= roman["IX"]
            elif (s[index]=="X" and index !=final and s[index+1]=="L"):
                integer += roman["XL"]
            elif (s[index]=="X" and index !=final and s[index+1]=="C"):
                integer += roman["XC"]
            elif (s[index]=="C" and index !=final and s[index+1]=="D"):
                integer += roman["CD"]
            elif (s[index]=="C" and index !=final and s[index+1]=="M"):
                integer += roman["CM"]
            else:
                integer += roman[s[index]]
                index +=1
                continue
            index +=2
        return integer
                
            
                
                
                
                
        
