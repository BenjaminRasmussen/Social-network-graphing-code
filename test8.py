with open('data_01') as input_data:
    # Skips text before the beginning of the interesting block:
    for line in input_data:
        if line.strip() == 'Start':  # Or whatever test is needed
            break
    # Reads text until the end of the block:
    for line in input_data:  # This keeps reading the file
        if line.strip() == 'End':
            break
        print(line) # Line is extracted (or block_of_lines.append(line), etc.)

s = 'cyqfjhcclkbxpbojgkar'
longest = ""
max =""

for i in range(len(s) -1):
    if(s[i] == s[i+1] ):
        longest = longest + s[i]
        if(i==len(s) -2):
            longest = longest + s[i+1]
    else:
        longest  = longest + s[i]
        if(len(longest) > len(max)):
            max = longest
        longest = ""

if(len(s) == 1):
    longest = s

