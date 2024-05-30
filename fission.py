#latest fission script language engine
# reactor (pre-fission processor)
def FsAdd(a,b):
  fs=[f'prep {a}',f'prep {b}','add','o']
  return(fission(fs)[0])
def FsSub(a,b):
  fs=[f'prep {a}',f'prep {b}','sub','o']
  return(fission(fs)[0])
def FsMx(a,b):
  fs=['bs',f'prep {a}','o','be',f'prep {b}','rr','sum','o']
  return(fission(fs)[0])
def FsDv(a,b):
  c=0
  while a>=b:
    fs=[f'prep {a}',f'prep {b}','sub','o']
    a=fission(fs)[0]
    c+=1
  return c
def FsDr(a,b):
  while a>=b:
    fs=[f'prep {a}',f'prep {b}','sub','o']
    a=fission(fs)[0]
  return a
def Fexp(a,b):
  c=1
  for i in range(int(b)):
    c=FsMx(a,c)
  return c
def Fstr(a,b):
  fs=[f'prep {a}',f'prep {b}','comb','o']
  return(fission(fs)[0])
def Fstc(istr,b,c):
  fs=[f'prep {istr}',f'prep {b}',f'prep {c}','cut','o']
  return(fission(fs)[0])
def Fssr(a,b):
  fs=[f'prep {a} ',f'prep {b}','comb','o']
  return(fission(fs)[0])
def fission(particles):
  arg=[]
  blk=[]
  ins=''
  DoInterPret=1
  BlockDepth=0
  for p in particles:
    #print(arg)
    #print('i:',p,'\nDIP:',DoInterPret)
    if DoInterPret==0:
      blk.append(p)
    if p=='bs':
      if BlockDepth==0:
        blk=[]
      DoInterPret=0 #interpreter switch off
      BlockDepth+=1
      #print('D:',BlockDepth)
      #print('DIP:',DoInterPret)
    if p=='be':
      BlockDepth-=1
      #print('D:',BlockDepth)
      if BlockDepth<=0:
        DoInterPret=1
        del blk[-1]
        #print('DIP:',DoInterPret)
    if DoInterPret==1:
      if p=='rt':
        p=str(ins)
      if p=='if':
        cc=arg[0]
        if eval(str(arg[0])):
          cc=fission(blk)
          arg=cc+arg
          del arg[len(cc)]
        else:
          del arg[0]
      elif p=='rr':
        cc=arg[0]
        for i in range(int(arg[0])):
          arg=fission(blk)+arg
        del arg[int(cc)]
      elif p=='wh':
        while True:
          cc=arg[0]
          if eval(cc)==True:
            arg=fission(blk)+arg
          else:
            break
      elif p=='rp':
        arg=[]
      elif p=='e':
        for i in arg[0]:
          del arg[i]
      elif p=='o':
        return(arg)
      elif p=='comb':
        arg[0]=str(arg[1])+str(arg[0])
        del arg[1]
      elif p=='add':
        arg[0]=float(arg[0])
        arg[0]+=float(arg[1])
        del arg[1]
      elif p=='sub':
        arg[0]=float(arg[1])-float(arg[0])
        del arg[1]
      elif p=='cut':
        arg[0]=arg[2][int(arg[1]):int(arg[0])]
        del arg[1:3]
      elif p=='sum':
        s=0
        for i in arg:
          s+=int(i)
        arg=[str(s)]
      elif p=='rd':
        ltmp=[]
        for i in arg[0].split():
          ltmp.append(arg[int(i)])
        arg=list(ltmp)
      elif p[:2] in ['Fs','Fe']:
        arg=[eval(p)]+arg
      elif p[:4]=='prep':
        arg=[p[5:]]+arg
      elif p[:4]=='varc': #varc type name index
        arg=[p.split()[1]+'.'+p.split()[2]+'.'+str(arg[int(p.split()[3])])]+arg
      elif p[:4]=='varr':
        for v in arg:
          try:
            if v.split('.')[1]==p[5:]:
              del arg[arg.index(v)]
          except:
            pass
      elif p=='co':
        arg=[arg[0]]
      elif p[:3]=='var': #var type.name.value
        for v in arg:
          try:
            if v.split('.')[1]==p[4:]:
              if v.split('.')[0]=='str':
                arg=[str('.'.join(v.split('.')[2:]))]+arg
              elif v.split('.')[0]=='int':
                arg=[int(float('.'.join(v.split('.')[2:])))]+arg
              elif v.split('.')[0]=='float':
                arg=[float('.'.join(v.split('.')[2:]))]+arg
          except:
            pass
      ins=str(p)
#demo
fission(['prep 3','varc int a 0','prep str.b.5','var b','varr b','varc int b 0','var a','var b','add','varc int c 0','var c','varc str d 0','var d','co','o'])
