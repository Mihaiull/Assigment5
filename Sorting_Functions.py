#overload the sort function:
def sort(self, key=None, reverse=False):
    if key is None:
        self.__departaments.sort(key=lambda departament: len(departament.patients), reverse=reverse)
    else:
        self.__departaments.sort(key=key, reverse=reverse)