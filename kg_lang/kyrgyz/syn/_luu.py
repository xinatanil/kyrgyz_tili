# coding=utf-8
from kg_lang.kyrgyz.feature import Feature
from kg_lang.kyrgyz.lang import WordEndingTypes
from kg_lang.kyrgyz.mucho import SpecialMucho, L


class LuuZatMuchosu(Feature):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [LuuZatMuchosu.make]

    mucholor = [
        [u"луу", u"луу", u"лүү", u"лүү"],
        [u"дуу", u"дуу", u"дүү", u"дүү"],
        [L((u"дуу", u"луу")), L((u"дуу", u"луу")), u"лүү", u"лүү"],
        [u"туу", u"туу", u"түү", u"түү"],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + u""
            end_of_result = mucho
            if isinstance(end_of_result, SpecialMucho):
                start_of_result, end_of_result = end_of_result.make(self.word_object.word)
            return start_of_result + end_of_result
        return self.word_object.word