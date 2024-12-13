#1
class Real:
    def action(self):
        return "Real operation"

class Proxy:
    def __init__(self, real):
        self.real = real

    def action(self):
        print("Pre-check call")
        return self.real.action()


real = Real()
proxy = Proxy(real)
print(proxy.action())

#2
class ImplA:
    def run(self):
        return "A"

class ImplB:
    def run(self):
        return "B"

class Bridge:
    def __init__(self, impl):
        self.impl = impl

    def use(self):
        return f"Use: {self.impl.run()}"

a = ImplA()
b = ImplB()

bridge_a = Bridge(a)
bridge_b = Bridge(b)

print(bridge_a.use())
print(bridge_b.use())

#3
class Old:
    def old_action(self):
        return "Old method"

class Adapter:
    def __init__(self, old_obj):
        self.old_obj = old_obj

    def action(self):
        return self.old_obj.old_action()


old = Old()
adapter = Adapter(old)
print(adapter.action())