ptr="picoCTF{w1{1wq83k055j5f}"
flag=[]

for i in range(0,8):
    print(ptr[i],end="")
for j in range(8,23):
    if(j&1):
        print(chr(ord(ptr[j])+2),end="")
    else:
        print(chr(ord(ptr[j])-5),end="")
print("}",end="")
'''
  stream = fopen("flag.txt", "r");
  v7 = fopen("rev_this", "a");
  if ( !stream )
    puts("No flag found, please make sure this is run on the server");
  if ( !v7 )
    puts("please run this on the server");
  v6 = fread(ptr, 0x18uLL, 1uLL, stream);
  if ( v6 <= 0 )
    exit(0);
  for ( i = 0; i <= 7; ++i )
  {
    v11 = ptr[i];
    fputc(v11, v7);
  }
  for ( j = 8; j <= 22; ++j )
  {
    v11 = ptr[j];
    if ( j & 1 )
      v11 -= 2;
    else
      v11 += 5;
    fputc(v11, v7);
  }
  v11 = v5;
  fputc(v5, v7);
  fclose(v7);
  return fclose(stream);
}
'''