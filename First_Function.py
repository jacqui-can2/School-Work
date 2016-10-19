#Jacqueline Cantu
#Computer Science 1370.02
#ConvertLab

#Part 1:
# define your conversion function here. it should:
# - take in one parameter, a temperature in Fahrenheit
# - return the corresponding temperature in Celcius
# - don't forget a docstring!


# here is the main function definition which contains the highest-level
#  steps that make up the program
def main():
    """
    This interactive console program gets a temperature in Fahrenheit
    from the user, and displays the conversion to Celcius.
    """

    # as the user for a temperature in Fahrenheit
    f = float(input("Enter a temperature in Fahrenheit:\n"))

    # use your function above to convert it to Celcius
    c = (f - 32) * (5/9)

    # display the converted temperature
    print(f, "degrees in Fahrenheit is","{0:.2f}".format(c), "degrees in Celcius.")
    
    # so far you've just defined functions, this line is what calls main to
    #start off the program
main()        
