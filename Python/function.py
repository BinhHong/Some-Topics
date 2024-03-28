"harry boc cuc".title()
"harry boc cuc".capitalize()
"harry boc cuc".upper()

# positional and keyword argument
def f(a,b=1, c=3):
    return (a+b)-c # a-2

f(5)
f(5,2)
print(f(a=5))
f(2,2,2)


def name(first_name, last_name, age=False):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

name('A', 'ku', 'b')


 unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
 completed_models = []
 
 while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
    
    
    
# slice
l = [5,1,2,3,22,4]
l[3::-1]
l.copy()

# arbitrary number of arguments
def make_pizza(*toppings):  
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")  
    for topping in toppings:
        print("- " + topping)
 
    

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def example_function(positional_arg1, positional_arg2, keyword_arg1=None, keyword_arg2=None, *args, **kwargs):
    print("Positional arguments:")
    print("positional_arg1:", positional_arg1)
    print("positional_arg2:", positional_arg2)
    
    print("\nKeyword arguments:")
    print("keyword_arg1:", keyword_arg1)
    print("keyword_arg2:", keyword_arg2)
    
    print("\nArbitrary arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nArbitrary keyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function with different types of arguments
example_function(1, 2, keyword_arg1=3, keyword_arg2=4, arg1=5, arg2=6, arg3=7, kwarg1="kwarg1", kwarg2="kwarg2")
example_function(1, 2, 3, 4, arg1=5, arg2=6, arg3=7, kwarg1="kwarg1", kwarg2="kwarg2")
example_function(1, 2, 3, 4, 10,11, arg1=5, arg2=6, arg3=7, kwarg1="kwarg1", kwarg2="kwarg2")
example_function(1, 2,5,6,7 ,arg1=5, arg2=6, arg3=7, kwarg1="kwarg1", kwarg2="kwarg2")

example_function(1, 2,4,keyword_arg1=3,arg1=5, arg2=6, arg3=7, kwarg1="kwarg1", kwarg2="kwarg2")
example_function(1, 2,4,keyword_arg1=3,keyword_arg2=3,arg1=5, arg2=6, arg3=7, kwarg1="kwarg1", kwarg2="kwarg2")


# sandwiches
