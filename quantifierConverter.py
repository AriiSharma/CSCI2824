class QuantifierConverter(object):

    def quantifierConverter(self,s):

        s = s.replace("\u2200", "for every")
        s = s.replace("\u2203","there exists")

        return s

    obj = QuantifierConverter()

print(quantifierConverter("\u2200 beautiful day there is, \u2203 some family time."))
