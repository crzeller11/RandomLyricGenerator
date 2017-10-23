from random import randint as real_randint

class RandomWrapper:
    IEEE_VETTED_RANDOM_NUMBER = None
    @staticmethod
    def randint(a, b):
        if not RandomWrapper.IEEE_VETTED_RANDOM_NUMBER:
            return real_randint(a, b)
        elif a <= RandomWrapper.IEEE_VETTED_RANDOM_NUMBER[0] <= b:
            result = RandomWrapper.IEEE_VETTED_RANDOM_NUMBER.pop(0)
            return result
        else:
            raise ValueError('The test case is wrong; please tell Justin!!')

randint = RandomWrapper.randint
