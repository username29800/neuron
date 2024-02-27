kwd0=''
pc=''
lc=''
ec=''
cr=''
cp=''
ap=''
ii=' '*0
ll=[]
bs=[]
run=1
def ed(x):
  if str(cp)==str(x):
    return 1
  else:
    return 0
while run:
  try:
    if 1: #input
      ui=str(input('> '))
      cp=ui.split()[0]
      ap=''
      for i in ui.split()[1:]:
        ap=ap+' '+i
      ap=ap[1:]
    if ed('a'): #append prev cursor
      pc=str(pc)+str(ui[2:])
    if ed('l'): #print current line
      print(pc+'|'+lc)
    if ed('p'): #set pointer
      ec=pc+lc
      pc=ec[:int(ap)]
      lc=ec[int(ap):]
    if ed('x'): #delete char, prev cursor
      pc=pc[:-int(ap)]
    if ed('d') and ll!=[]: #delete line
      for i in ap.split()[::-1]:
        del ll[int(i)-1]
    if ed('k'): #kill lines in range
      pa=ap.split()
      del ll[int(pa[0])-1:int(pa[1])]
    if ed('o') and ll!=[]: #insert line
      ln=int(ap)-1
      lpc=ll[:ln]
      llc=ll[ln:]
      lpc.append(ii+pc+lc)
      ll=lpc+llc
      pc=''
      lc=''
    if ed('lo'): #append line
      ll.append(ii+pc+lc)
      pc=''
      lc=''
    if ed('y'): #yank
      cr=ll[int(ap)-1]
    if ed('n'): #set line
      pc=ll[int(ap)-1]
      lc=''
    if ed('pi'): #paste into
      pc=pc+cr
    if ed('l.'): #print lines, indexed
      li=1
      for i in ll:
        print(f'{str(li):{len(str(len(ll)))}} {i}')
        li+=1
    if ed('lm'): #print lines, indexed, with range
      li=1
      for i in ll[int(ap.split()[0])-1:int(ap.split()[1])]:
        print(f'{int(ap.split()[0])+li-1:{len(str(len(ll)))}} {i}')
        li+=1
    if ed('ml'): #print lines, not indexed, with range
      for i in ll[int(ap.split()[0])-1:int(ap.split()[1])]:
        print(i)
    if ed('.l'): #print lines, not indexed
      for i in ll:
        print(i)
    if ed('quit'):
      run=0
    if ed('of'): #open file
      of=open(str(ap),'r')
      ll=of.read().splitlines()
      of.close()
    if ed('wf'): #write to file
      op=''
      for i in ll:
        op=op+str(i)+'\n'
      wf=open(str(ap),'w')
      wf.write(op)
      wf.close()
    if ed('ecl'): #clear all editor lines
      ll=[]
    if ed('fn'): #forward search with count
      pa=ap.split()
      pa[0]=str(pa[0])
      pa[1]=int(pa[1])
      for p in range(pa[1]):
        #pc=pc+lc[0]
        #lc=lc[1:]
        for i in range(len(lc)):
          if lc[i:i+len(pa[0])]==pa[0]:
            pc=pc+lc[:i+len(pa[0])]
            lc=lc[i+len(pa[0]):]
            break
    if ed('bn'): #backward search with count
      pa=ap.split()
      pa[0]=str(pa[0])
      pa[1]=int(pa[1])
      for p in range(pa[1]):
        #lc=pc[-1]+lc
        #pc=pc[:-1]
        for i in range(len(pc),0,-1):
          if pc[i-len(pa[0]):i]==pa[0]:
            uc=pc+lc
            pc=uc[:i-len(pa[0])]
            lc=uc[i-len(pa[0]):]
            break
    if ed('pl'): #move pointer to the end of the line
      pc=pc+lc
      lc=''
    if ed('pp'): #set relative cursor position
      if ap[0]=='0':
        ap=-int(ap)
      else:
        ap=int(ap)
      cc=len(pc)
      uc=pc+lc
      pc=uc[:cc+ap]
      lc=uc[cc+ap:]
    if ed('m'): #copy to line
      ln=int(ap)-1
      lpc=ll[:ln]
      llc=ll[ln:]
      lpc.append(ii+pc+lc)
      ll=lpc+llc
    if ed('i'): #insert to line
      ll[int(ap)-1]=ii+pc+lc
      pc=''
      lc=''
    if ed('ll'): #last line number
      print(len(ll))
    if ed('h') or ed(';'): #help
      print('''Editor Commands

a - Append to Current Line
l - Print Current Line
p - Set Pointer
x - Delete Characters
d - Delete Line
o - Insert Line
lo - Append Line
y - Yank (Copy) Line
n - Set Line
pi - Paste Into
l. - Print Lines (Indexed)
lm - Print Lines (Indexed, Range)
ml - Print Lines (Not Indexed, Range)
.l - Print Lines (Not Indexed)
quit - Quit the Editor
of - Open File
wf - Write to File
ecl - Clear All Editor Lines
fn - Forward Search with Count
bn - Backward Search with Count
pl - Move Pointer to End of Line
pp - Set Relative Cursor Position
m - Copy to Line
i - Insert to Line
ll - Last Line Number
ol - Append to Line then Append to Document''')
    if ed('ol'): #append input to the document
      ll.append(ii+pc+str(ui[3:])+lc)
      pc=''
      lc=''
    if ed('ii'): #set auto indentation
      ii=' '*int(ap)
    if ed('j'): #join lines in range
      pa=ap.split()
      uc=str("\n".join(ll[int(pa[0])-1:int(pa[1])]))
      ll[int(pa[0])-1]=uc
    if ed('jl'): #join lines in list
      uc=''
      for i in ap.split():
        uc=f'{uc}\n{ll[int(i)-1]}'
      uc=uc[1:]  
      ll[int(ap.split()[0])-1]=uc
    if ed('s'): #split joined line
      for i in ll[int(i)-1].splitlines():
        ll.append(i)
    if ed('ss'): #split line in place
      ln=int(ap)-1
      lpc=ll[:ln]
      llc=ll[ln+1:]
      lpc.extend(ll[ln].splitlines())
      ll=lpc+llc
    if ed('v'): #move line
      pa=ap.split()
      uc=str(ll[int(pa[0])-1])
      ll[int(pa[1])-1]=uc
      del ll[int(pa[0])-1]
    if ed('c'): #copy and paste line
      pa=ap.split()
      uc=str(ll[int(pa[0])-1])
      ll[int(pa[1])-1]=uc
    if ed('e'): #empty current line
      pc=''
      lc=''
    if ed('b'): #backup lines after arg
      ln=int(ap)-1
      bs=list(ll[ln:])
      ll=ll[:ln]
    if ed('bb'): #restore lines
      ll.extend(bs)
    if ed('jn'): #join lines in range without newline
      pa=ap.split()
      uc=str("".join(ll[int(pa[0])-1:int(pa[1])]))
      ll[int(pa[0])-1]=uc
    if ed('jnn'): #join lines in list without newline
      uc=''
      for i in ap.split():
        uc=f'{uc}{ll[int(i)-1]}'
      uc=uc[1:]  
      ll[int(ap.split()[0])-1]=uc
    if ed('f'): #search and replace by given count
      pa=ap.split()
      pa[0]=str(pa[0])
      pa[2]=int(pa[2])
      for p in range(pa[2]):
        #pc=pc+lc[0]
        #lc=lc[1:]
        for i in range(len(lc)):
          if lc[i:i+len(pa[0])]==pa[0]:
            pc=pc+lc[:i+len(pa[0])]
            lc=lc[i+len(pa[0]):]
            break
        pc=pc[:-len(pa[0])]+pa[1]
    if ed('g'): #search and replace all
      pa=ap.split()
      for p in range(int(len(lc)/len(pa[0]))):
        #pc=pc+lc[0]
        #lc=lc[1:]
        for i in range(len(lc)):
          if lc[i:i+len(pa[0])]==pa[0]:
            pc=pc+lc[:i+len(pa[0])]
            lc=lc[i+len(pa[0]):]
        pc=pc[:-len(pa[0])]+pa[1]
        lc=pc[-1]+lc
        pc=pc[:-1]
  except Exception as xp:
    print(xp)
