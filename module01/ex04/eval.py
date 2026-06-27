from typing import List, Union

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs: List[Union[int, float]], words: List[str]) -> int:
        if len(coefs) == len(words):
            return sum(len(word) * coef for word, coef in zip(words, coefs))
        return -1

    @staticmethod
    def enumerate_evaluate(coefs: List[Union[int, float]], words: List[str]) -> int:
        if len(coefs) == len(words):
            return sum(len(word) * coefs[i] for i, word in enumerate(words))
        return -1
