#First part ==> reading a file

with open('username-password-recovery-code.csv', 'r') as csv_file:
    file_text = csv_file.read()
    lines = file_text.split('\n')

keys = lines[0].split(';')
data = lines[1:]
final_list = []

for i in range(len(data)):
    final_list.append({})

count = 0

for key in keys:
    for i in range(len(data)):
        temporary_dict = final_list[i]
        temporary_dict[key] = data[i].split(';')[count]
        final_list[i] = temporary_dict
    count += 1

print(final_list)

#Second part ==> writing in a file

keys_w = list(final_list[0].keys())
data_w = []

for i in range(len(final_list)):
    temporary_list = list(final_list[i].values())
    data_w.append(temporary_list)

text_data_w = ''

for i in range(len(data_w)):
    text_data_w += ';'.join(data_w[i]) + '\n'
    

text_w = ';'.join(keys_w) + '\n'+ text_data_w

wr = open('write.txt', 'w')
wr.write(text_w)
wr.close

