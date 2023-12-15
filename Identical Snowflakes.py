def main():
    snowflakes = []
    sumSnowflakes = {}
    while True:
        try:
            #INPUT
            numSnowflakes = int(input("How many snowflakes are you inputting?\n"))
            [snowflakes.append(input("Input 6 numbers separated by spaces\n").split()) for i in range(numSnowflakes)]
            for i in range(0,len(snowflakes)):
                for o in range(len(snowflakes[i])):
                    snowflakes[i][o] = int(snowflakes[i][o])
            for i in snowflakes:
                print(f"Snowflake {i} has more/less than 6 numbers\n") if len(i) != 6 else None
                snowflakes.remove(i) if len(i) != 6 else None
            #ORGANIZING BY SUM
            for i in range(len(snowflakes)):
                sumSnowflakes[sum(snowflakes[i])].append(snowflakes[i]) if sum(snowflakes[i]) in sumSnowflakes else sumSnowflakes.update({sum(snowflakes[i]):[snowflakes[i]]})
            #COMPARISON
            for i 
        except ValueError:
            print("That is not a number\n")
main()