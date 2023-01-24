intable=""
outtable="12345754"
str="Shawn Linton Miranda"
transtable=str.maketrans(intable,outtable)

x=str.translate(transtable)
print(x)
