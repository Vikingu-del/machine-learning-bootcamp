class TinyStatistician:
    def mean(self, x: list) -> float:
        m = len(x)
        if m == 0:
            return None
        return float(sum(i for i in x) / m)
    
    def median(self, x: list) -> float:
        m = len(x)
        if m == 0:
            return None
        sorted_x = sorted(x)
        if m % 2 == 1:
            return float(sorted_x[m // 2])
        else:
            return float((sorted_x[(m // 2) - 1] + sorted_x[m // 2]) / 2)
        
    def quartile(self, x: list) -> list:
        m = len(x)
        if m == 0:
            return None
        sorted_x = sorted(x)
        f_quart = sorted_x[round(0.25 * (m - 1))]
        th_quart = sorted_x[round(0.75 * (m - 1))]
        return [float(f_quart), float(th_quart)]

    def var(self, x: list) -> float:
        m = len(x)
        if m == 0:
            return None
        mean = self.mean(x)
        return float((sum(pow(i - mean, 2) for i in x)) / m)
    

    def std(self, x: list) -> float:
        variance = self.var(x)
        if variance:
            return variance ** 0.5
        return None



    
if __name__ == "__main__":
    t = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print("mean: ", t.mean(a))
    print("median: ", t.median(a))
    print("quartiles: ", t.quartile(a))
    print("variance: ", t.var(a))
    print("standard deviation: ", t.std(a))


