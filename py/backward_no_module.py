import torch
import torch.nn as nn

# network
class Net(object):
    """
    """
    def __init__(self):
        super(Net, self).__init__()

    def init_param(self, *args, **kwargs):
        raise NotImplementedError

    def forward(self, *args, **kwargs):
        raise NotImplementedError


class Simple(Net):
    """
    """
    def __init__(self):
        super(Net, self).__init__()
        self.w1 = nn.Parameter(data=torch.FloatTensor(1))
        self.w2 = nn.Parameter(data=torch.FloatTensor(1))
        self.b1 = nn.Parameter(data=torch.FloatTensor(1))
        self.b2 = nn.Parameter(data=torch.FloatTensor(1))
        self.init_param()

        self.loss = nn.MSELoss()

    def init_param(self, *args, **kwargs):
        self.w1.data.fill_(2.0)
        self.w2.data.fill_(3.0)
        self.b1.data.fill_(3.0)
        self.b2.data.fill_(4.0)

    def forward(self, x):
        h1 = x * self.w1 + self.b1
        h2 = h1 * self.w2 + self.b2
        return h2

    def get_loss(self, true, pred):
        return self.loss(true, pred)

    def parameters(self):
        return [self.w1, self.b1, self.w2, self.b2]

    def named_parameters(self):
        names = ['w1', 'b1', 'w2', 'b2']
        return {x: y for x, y in zip(names, self.parameters())}

    def train(self):
        print("in train mode")

    def print_weight(self):
        for n, p in self.named_parameters().items():
            print(n)
            print(p.data)

    def print_grad(self):
        for p in self.parameters():
            print(p.grad)


class Trainer(object):
    def __init__(self):
        super(Trainer, self).__init__()

    def train(self):
        pass

    def eval(self):
        pass

    def predict(self):
        pass

    def save(self):
        pass
    
    def load(self):
        pass


class Singletrainer(object):
    def __init__(self):
        # data 
        self.x = torch.Tensor(1).fill_(2)
        self.y = torch.Tensor(1).fill_(1)
        # model
        self.model = Simple()
        # optim
        self.optim = torch.optim.SGD(params=self.model.parameters(), lr=1)

    def train(self):
        epoch = 1
        self.model.train()
        for i in range(epoch):
            # forward
            output = self.model.forward(self.x)
            loss = self.model.get_loss(output, self.y)
            print("Epoch:{}\tloss:{}".format(i, loss.item()))
            # backward
            self.optim.zero_grad()
            loss.backward()
            self.model.print_grad()
            self.model.print_weight()
            self.optim.step()
            self.model.print_weight()

    def eval(self):
        pass

    def predict(self):
        pass

    def save(self):
        pass
    
    def load(self):
        pass

if __name__ == "__main__":
    s = Singletrainer()
    s.train()
