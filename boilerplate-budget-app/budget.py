class Category:

  def __init__(self,name):
    self.name = name
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description = ''):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, point):
    if self.withdraw(amount, f"Transfer to {point.name}"):
      point.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self, amount):
    return self.balance >= amount

  def __str__(self):
    text = ''
    text += self.name.center(30,'*')+'\n'
    for x in self.ledger:
      if len(x['description'])>23:
        text += x['description'][0:23]
      else:
        text += x['description'][0:23].ljust(23)
      text += "{0:.2f}".format(x['amount']).rjust(7)
      text += '\n'
    text += f"Total: {self.balance}"
    return text
      
    
def create_spend_chart(categories):
  total = 0
  text = "Percentage spent by category\n"
  withdrawals = {}
  for x in categories:
    withdrawals[x.name] = 0
    for y in x.ledger:
      if y['amount'] < 0:
        withdrawals[x.name] += y['amount']
    withdrawals[x.name] = -withdrawals[x.name]
  for x in withdrawals:
    total += (withdrawals[x])
  for x in withdrawals:
    withdrawals[x] = int(withdrawals[x] / total * 100)

  for i in range(100,-10,-10):
    text += str(i).rjust(3)+'| '
    for x in categories:
      if withdrawals[x.name] >= i:
        text += 'o  '
      else:
        text += '   '
    text += '\n'
  text += ' ' * 4 + '-' * (1+len(categories)*3) + '\n'

  space = 0
  for x in categories:
    if len(x.name) > space:
      space = len(x.name)
  for i in range(space):
    text += ' ' * 5
    for x in categories:
      if len(x.name)>i:
        text += x.name[i] + '  '
      else:
        text += ' ' * 3
    text += '\n'
  return text[0:-1]