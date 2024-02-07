"""
    Program purpose: To conver an amount in MAlaysian Ringgit (MYR)
    Programmer: Nooralia Evieanna Sofea
    Date: 7 February 2024
"""
print("Currency Conversion Program")
print (2 * "\n")

#Display exchange rates
print("Exchange Rates:")
print("ThaiBaht - ThaiBaht: 7.47")
print("IndonesianRupiah - IndonesianRupiah: 3291.13")
print("USDollar - USDollar: 025")
print ("\n")

print("Choose the target currency:")
print("1. ThaiBaht")
print("2. IndonesianRupiah")
print("3. US Dollar")
print ("\n")
choice = int(input("Enter your choice (1-3): "))

#Prompt the user to input amount in MYR
MYRamount = float(input("Enter the amount in Malaysia Ringgit (MYR): "))


if choice == 1: #To calculate the currency between Thai Bath to MYR
    convertThaiBaht = MYRamount * 7.47
    print("Equivalent amount in ThaiBaht :", convertThaiBaht)

elif choice == 2:
    convertIndonesianRupiah = MYRamount * 3291.13
    print("Equivalent amount in Indonesian Rupiah :", convertIndonesianRupiah)
elif choice == 3:
    convertUSDollar = MYRamount * 0.25
    print("Equivalent amount in USDollar :", convertUSDollar)

else:
    print("Invalid option !! Re-enter number 1-3:")