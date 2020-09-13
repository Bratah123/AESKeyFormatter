# @author Brandon Nguyen
import sys

# Not the fastest way to find the AES Key as it requires you to look for it in IDA (ZLZ.dll)
# but it helps format it
# May help for versions that aren't GMS which aren't automated already

# Nexon always has 32 values for the AES Encryption Key (from what I observed)
MAX_KEY_VALUE = 32

def add_none_hex(text):
    for i in range(3):
        text += "0x00, "
    return text

def get_values_as_arr():
    print('Type in "quit" to stop program')
    values = input("Enter your AES Values in integer form (Usually 32 Values Spaced Out evenly 21 23 25 etc.):")
    # asks for values found in ZLZ.dll
    if values.lower() == "quit":
        sys.exit()
    values_arr = values.split(" ") # Splits all the values into an array ["23", "232", "632"] so on
    if len(values_arr) < MAX_KEY_VALUE:
        print("You did not input the correct amount of values.")
        get_values_as_arr() # recursion
    return values_arr

def convert_to_aob(values_arr):
    aob = "\nAOB = {\n\n"
    value_index = 1
    for value in values_arr:
        int_value = int(value)
        aob += f"0x{int_value:X}, "
        aob = add_none_hex(aob)
        if value_index == 4:
            aob += "\n"
            value_index = 0
        value_index += 1
    aob += "\n}"
    return aob

def convert_to_odin(values_arr):
    odin = "\nOdinFormat = {\n\n"
    value_index = 1
    for value in values_arr:
        int_value = int(value)
        if value_index == 1:
            odin += f"0x{int_value:X}, "
            odin = add_none_hex(odin)
            odin += "\n"
        if value_index == 4:
            value_index = 0
        value_index += 1
    odin += "\n}"
    return odin

values_arr = get_values_as_arr()
print(convert_to_aob(values_arr))
print(convert_to_odin(values_arr))
