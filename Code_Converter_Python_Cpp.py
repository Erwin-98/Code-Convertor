import re

def python_to_cpp(python_code):
    cpp_code = ""

    lines = python_code.split("\n")

    for line in lines:
        line = line.strip()

        #skip empty lines
        if not line:
            cpp_code += "\n"
            continue

        #1 print statement
        if line.startswith("print("):
            content = re.search(r"print\((.*)\)", line).group(1)
            cpp_code += f"std::cout << {content} << std::endl;\n"
            continue

        #2 variable declaration and assignment
        match = re.match(r"(\w+)\s*=\s*(.*)", line)
        if match:
            var_name, value = match.groups()
            if value.isdigit():
                cpp_code += f"int {var_name} = {value};\n"
            elif re.match(r"\d*\.\d+", value):
                cpp_code += f"double {var_name} = {value};\n"
            elif re.match(r'".*"|\'.*\'', value):
                cpp_code += f"std::string {var_name} = {value};\n"
            else:
                cpp_code += f"auto {var_name} = {value};\n"
            continue

        #3 input
        if "input(" in line:
            var_name = line.split("=")[0].strip()
            cpp_code += f"std::string {var_name};\nstd::cin >> {var_name};\n"
            continue

        #4 if-elif-else
        if line.startswith("if ") or line.startswith("elif ") or line.startswith("else"):
            if line.startswith("if"):
                condition = re.search(r"if (.*):", line).group(1)
                cpp_code += f"if ({condition}) {{\n"
            elif line.startswith("elif"):
                condition = re.search(r"elif (.*):", line).group(1)
                cpp_code += f"else if ({condition}) {{\n"
            else:
                cpp_code += "else {\n"
            continue

        #end block
        if line == "}":
            cpp_code += "}\n"
            continue

        #5 for loop
        match = re.match(r"for (\w+) in range\((.*)\):", line)
        if match:
            var_name, range_vals = match.groups()
            start, end = "0", range_vals 
            if "," in range_vals:
                start, end = map(str.strip, range_vals.split(","))
            cpp_code += f"for (int {var_name} = {start}; {var_name} < {end}; ++{var_name}) {{\n"
            continue

        #6 while loop
        match = re.match(r"while (.*):", line)
        if match:
            condition = match.group(1)
            cpp_code += f"while ({condition}) {{\n"
            continue

        #7 functions
        match = re.match(r"def (\w+)\((.*)\):", line)
        if match:
            func_name, params = match.groups()
            cpp_params = params.replace(",", " int")
            cpp_code += f"void {func_name}(int {cpp_params}) {{\n"
            continue

        #8 switch case
        match = re.match(r"switch (.*):", line)
        if match:
            condition = match.group(1)
            cpp_code += f"switch ({condition}) {{\n"
            continue

        match = re.match(r"case (.*):", line)
        if match:
            case_val = match.group(1)
            cpp_code += f"case {case_val}:\n"
            continue


        #9 classes
        match = re.match(r"class (\w+):", line)
        if match:
            class_name = match.group(1)
            cpp_code += f"class {class_name} {{\npublic:\n"
            continue

        

        cpp_code += f"{line}\n"

    return cpp_code

# Functionality tested
python_code = """
#1 print statement
print("Hello, World!")

#2 variable declaration and assignment
x = 1
y = 2.3
name = "Ioana"

#3 input
age = input("Enter your age: ")

#4 if-elif-else
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

#5 for loop
for i in range(5):
    print(i)

#6 while loop
while x < 15:
    print(x)
    x += 1

#7 functions
def greet(name):
    print(f"Hello, {name}!")

greet("Ioana")

#8 switch case
switch = 2
if switch == 1:
    print("Case 1")
elif switch == 2:
    print("Case 2")
else:
    print("Default case")


#9 classes
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "animal sound"

    def move(self):
        return f"{self.name} moves around"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Bark"

    def fetch(self):
        return f"{self.name} is fetching a stick"



def main():
    dog = Dog("Cutu", "Golden Retriever")
    
    print(dog.make_sound())
    print(dog.fetch())
    print(dog.move())


if __name__ == "__main__":
    main()
"""


cpp_code = python_to_cpp(python_code)
print(cpp_code)
