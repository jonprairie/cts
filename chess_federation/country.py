class country:
    def __init__(self, name, short_name, adjective):
        self.name = name
        self.short_name = short_name
        self.adjective = adjective
        
    def Adjective(self):
        return self.adjective
        
    def GetName(self):
        return self.name
        
    def GetShortName(self):
        return self.short_name

russia = country("russia", "rus", "russian")
usa = country("usa", "usa", "american")
germany = country("germany", "ger", "german")
france = country("france", "fra", "french")
norway = country("norway", "nor", "norwegian")
armenia = country("armenia", "arm", "armenian")
ukraine = country("ukraine", "ukr", "ukranian")
china = country("china", "chi", "chinese")
india = country("india", "ind", "indian")
spain = country("spain", "spa", "spanish")
england = country("england", "eng", "english")   
japan = country("japan", "jap", "japanese")
world = country("terra", "ter", "terran")
country_list = [russia, usa, germany, france, norway, armenia, ukraine, china, india, spain, england, japan]