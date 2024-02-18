def CMYK_to_RGB(c,m,y,k):
    output = {}
    r = int(255 * (1-(c/100))*(1-(k/100)))
    g = int(255 * (1-(m/100))*(1-(k/100)))
    b = int(255 * (1-(y/100))*(1-(k/100)))

    output["Red"] = r
    output["Green"] = g
    output["Blue"] = b
    return output

def main():
    final_input = {}
    final_output = {}
    print("CMYK to RGB Convertor")
    while True:
        user_input = {}
        c = str(input("Enter the Cyan Color Value: "))
        if (c.lower() == "q" or c.lower()=="quit"):
            break
        else:
            c =float(c)
        m = float(input("Enter the Magenta Color Value: "))
        y = float(input("Enter the Yellow Color Value: "))
        k = float(input("Enter the Key Color Value: "))

        if (c>100 or m>100 or y>100 or k>100):
            print("Please enter values betweeen 0-100\n")

        else:
            user_input["Cyan"] = c
            user_input["Magenta"] = m
            user_input["Yellow"] = y
            user_input["Black"] = k
            final_input.update(user_input)
        
            for i in range(len(final_input)):
                output = CMYK_to_RGB(final_input["Cyan"],final_input["Magenta"],final_input["Yellow"],final_input["Black"] )
                final_output.update(output)
            print("\nRGB Values")
            for key,value in final_output.items():
                print(f"{key}: {value}")
            print()

if __name__ == "__main__":
    main()