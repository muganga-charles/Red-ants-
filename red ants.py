def get_data():#a sub program to capture data from the user
    start_number=int(input("Enter the starting number of red ants"))
    days=int(input("Enter the number of days"))
    average=(start_number,days)
    return (average)#the sub program returns  th e starting number of red ants and the number of days
def averge_1(start_number1,days2):
    day=0
    average_population=int(input("Enter average population"))
    for i in range(day,days2):#this loops and provides the increament for a given number of days
        final=start_number1+(((average_population/100)+start_number1)*i)
        print("the population for day",i+1,"is",final)#this prints out the out put

def main():
    (start_number1,days2)=get_data()
    averge_1(start_number1,days2)
main()