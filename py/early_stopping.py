class EarlyStop:
    """
    """
    def __init__(self, is_bigger_better=True, patience=2):
        self.is_bigger_better = is_bigger_better
        self.patience = patience
        self.tolerate = 0
        self.best_value = -9999999 if is_bigger_better is True else 9999999 
        self.best_step = 0

    def check(self, value, step):
        if self.is_bigger_better:
            if value > self.best_value:
                self.tolerate = 0
                self.best_value = value
                self.best_step = step
            else:
                self.tolerate += 1
        else:
            if value < self.best_value:
                self.tolerate = 0
                self.best_value = value
                self.best_step = step
            else:
                self.tolerate += 1
        # check
        if self.tolerate >= self.patience:
            return False
        else:
            return True


if __name__ == "__main__":
    es = EarlyStop(is_bigger_better=True, patience=4)
    values = [1, 2, 3, 2, 4, 5, 4, 3, 4, 6, 1]
    for s in range(len(values)):
        if es.check(values[s], s):
            continue
        else:
            break
    print(es.__dict__)
    assert es.best_value == 6
    assert es.best_step == 9
