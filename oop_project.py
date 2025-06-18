from bank_accounts import * #imports everything
Lara = BankAccount(1000,"Lara")
Sophia = BankAccount(2000,"Sophia")

Lara.getBalance()
Sophia.getBalance()
Lara.deposit(500)
Sophia.withdraw(3000)
Lara.withdraw(100)

Sophia.transfer(1000, Lara)

Mark = InterestRewardsAcct(2000,"Mark")
Mark.getBalance()
Mark.deposit(200)
Mark.transfer(100,Sophia)

Jack = SavingsAcct(1000, "Jack")
Jack.getBalance()
Jack.deposit(100)
Jack.transfer(500,Sophia)