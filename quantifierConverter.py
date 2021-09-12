#creating class name QuantifierConverter
class QuantifierConverter(object):
    #function name quantifierConverter with s as a parameter
    def quantifierConverter(self,s):
        #using replace function to replace "\u2200" with "for every" in string s
        s = s.replace("\u2200", "for every")
        #using replace function to replace "\u2203" with "there exists" in string s
        s = s.replace("\u2203","there exists")
        #returning s
        return s
#creating instance name obj of class QuantifierConverter to call function quantifierConverter
obj = QuantifierConverter()
#calling quantifierConverter function using instance 
#passing string "\u2200 beautiful day there is, \u2203 some family time." as parameter
print(instance.quantifierConverter("\u2200 beautiful day there is, \u2203 some family time."))
