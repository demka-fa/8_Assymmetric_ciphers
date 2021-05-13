class DiffieHellman:

    __private_key = None
    __mixed_key = None

    def __init__(self, a: int, p: int, g: int):
        self.__a = a
        self.__p = p
        self.__g = g

    @property
    def mixed_key(self):
        """
        Возвращает смешанный ключ
        :return:
        """
        result = self.__g ** self.__a % self.__p
        if self.__mixed_key is None:
            self.__mixed_key = result
        return result

    def generate_key(self, mixed_key):
        """
        Возвраащет приватный ключ
        :param mixed_key:
        :return:
        """

        self.__private_key = mixed_key ** self.__a % self.__p
        return self.__private_key

