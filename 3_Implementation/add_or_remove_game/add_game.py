
filename="a.txt"
add_game_buffer=[]
f= open(filename,'r',encoding='utf-8')
add_game_buffer.append(f.read())


final_buffer=[]

for bufferobj in add_game_buffer:
   buffer_split=bufferobj[:]
   buffer_split=buffer_split.split('\n')
   for i in range(len(buffer_split)): 
             final_buffer.append([buffer_split[i]])
print(final_buffer)             
   