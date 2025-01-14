from kg.lang.lang import Unduu, Unsuz

"""
SpecialMucho - это такой суффикс, при применении которого начальная часть слова меняется.
    Обычно в кыргызском языке суффиксы просто прибавляется в конец слова.

    Потомки названы коротко, чтобы при построении матрицы форм суффиксов они не занимали много места.
"""


class SpecialMucho(object):
    def __init__(self, mucho):
        self.mucho = mucho

    def make(self, word):
        if isinstance(self.mucho, SpecialMucho):
            return self.mucho.make(word)
        return word, self.mucho

    class Meta:
        __doc__ = "Бул мучо уланганда унгу соз озгорот"


class J(SpecialMucho):
    def __init__(self, mucho):
        super(self.__class__, self).__init__(mucho)

    def make(self, word):
        word, mucho = super(J, self).make(word)
        if word[-1] == 'к':
            return word[:-1] + 'г', mucho
        if word[-1] == 'п':
            return word[:-1] + 'б', mucho
        return word, mucho

    class Meta:
        __doc__ = "Бул мучо уланганда к жана п менен буткон создор жумшарат"


class L(SpecialMucho):
    def __init__(self, mucho):
        super(self.__class__, self).__init__(mucho)

    def make(self, word):
        word, mucho = super(L, self).make(word)
        if isinstance(mucho, tuple):
            if word[-1] == 'р':
                mucho = mucho[0]
            if word[-1] == 'й':
                mucho = mucho[1]
        return word, mucho

    class Meta:
        __doc__ = "Бул мучо р жана й тамгалар менен буткон создорго колдонулуп," \
                  "р менен буткон создорго биринчи мучону, й мн буткондорго экинчи мучону" \
                  "кайтарат"


class U(SpecialMucho):
    def __init__(self, mucho):
        super(self.__class__, self).__init__(mucho)

    def make(self, word):
        word, mucho = super(U, self).make(word)
        if word[-1] in Unduu.all:
            if len(word) == 2 or word[-3] == " ":
                return word, "ш"
            if word[-2] in Unduu.all:
                return word, "ш"
            return word[:-1], mucho
        return word, mucho

    class Meta:
        __doc__ = "Бул мучо уланганда ундуу менен буткон этиштер кыскарат, же 'ш' мучосу уланат"


class P(SpecialMucho):
    def __init__(self, mucho):
        super(self.__class__, self).__init__(mucho)

    def make(self, word):
        word, mucho = super(P, self).make(word)
        if (word[-1] == 'п' or word[-1] == 'б') and word[-2] in Unduu.all:
            if isinstance(mucho, tuple):
                return word[:-2] + Unduu.sozulgandar[word[-2]], (self.cut_if_starts_with_unduu(mucho[0]),
                                                                 self.cut_if_starts_with_unduu(mucho[1]))
            return word[:-2] + Unduu.sozulgandar[word[-2]], self.cut_if_starts_with_unduu(mucho)
        return word, mucho

    def cut_if_starts_with_unduu(self, mucho):
        if mucho[0] in Unduu.all:
            return mucho[1:]
        return mucho

    class Meta:
        __doc__ = "Бул мучо уланганда 'тап-, теп-' деген этиштер 'табып, тебип' болбой 'таап, тээп' болуп жондолот"


class K(SpecialMucho):
    def __init__(self, mucho):
        super(self.__class__, self).__init__(mucho)

    def make(self, word):
        word, mucho = super(K, self).make(word)
        if word[-1] in Unsuz.katkalan:
            return word, 'п' + mucho[1:]
        return word, mucho

    class Meta:
        __doc__ = "Каткалан унсуздор менен буткон создорго 'б' тамгасы менен башталган мучо уланса 'п' болуп жондолот"
