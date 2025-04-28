# map function applies a given function to all items in a collection

celsius = [0.0, 10.0 , 20.0, 30.0, 40.0, 50.0]

def c_to_f(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(c_to_f, celsius))

print(fahrenheit)