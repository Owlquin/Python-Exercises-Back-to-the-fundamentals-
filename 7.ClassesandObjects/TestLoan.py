from Loan import Stock

def main():
    Stock1 = Stock("INTC","Intel Corporation", 20.5, 20.35)

    print(f"The price change percentage is: {Stock1.getChangePercent()}")


main()