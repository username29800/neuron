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
      ins=str(p)
def NtInput(ll,i1):
  if ':' in str(i1): #start input with : to read from a line
    return ll[int(str(i1[1:]))-1]
  else:
    return i1
def ed(x):
  if str(cp)==str(x):
    return 1
  else:
    return 0
pc=''
ec=''
cr=''
cp=''
ap=''
ii=' '*0
ll=[]
k1=[]
kl=[]
k0=[]
bs=[]
while True:
  try:
    if 1: #input
      ui=str(input('> '))
      cp=ui.split()[0]
      ap=''
      for i in ui.split()[1:]:
        ap=ap+' '+i
      ap=ap[1:]
    if ed('l'): #print current line
      print(pc)
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
      lpc.append(ii+pc)
      ll=lpc+llc
      pc=''
    if ed('lo'): #append line
      ll.append(ii+pc)
      pc=''
    if ed('n'): #set line
      pc=ll[int(ap)-1]
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
      break
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
    if ed('m'): #copy to line
      ln=int(ap)-1
      lpc=ll[:ln]
      llc=ll[ln:]
      lpc.append(ii+pc)
      ll=lpc+llc
    if ed('i'): #insert to line
      ll[int(ap)-1]=ii+pc
      pc=''
    if ed('ll'): #last line number
      print(len(ll))
    if ed('ii'): #set auto indentation
      ii=' '*int(ap)
    if ed('e'): #empty current line
      pc=''
    if ed('cx'): #convert to integer
      ll[int(ap)-1]=str(int(float(ll[int(ap)-1])))
    if ed('q'): #keyword init
      k0.extend(ap.split())
    if ed('z'): #erase a keyword
      for i in ap.split():
        k0.remove(i)
    if ed('zz'): #erase all keywords
      k0=[]
      k1=[]
    if ed('w'): #print keywords
      print(' '.join(k0))
      print(' '.join(k1))
    if ed('r'): #order keywords
      for i in ap.split():
        k1.append(k0[int(i)-1])
    if ed('rr'): #swap keyword lists
      kl=list(k0)
      k0=list(k1)
      k1=list(kl)
    if ed('ww'): #move keywords to the current line
      pc=pc+' '.join(k1)
    if ed('fs'): #'fission' programming language implementation
      for i in fission(ll[int(ap.split()[0])-1:int(ap.split()[1])]):
        pc=pc+str(i)
    if ed('add'):
      pc=str(FsAdd(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('sub'):
      pc=str(FsSub(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('tx'):
      pc=str(FsMx(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('dd'):
      pc=str(float(NtInput(ll,ap.split()[0]))/float(NtInput(ll,ap.split()[1])))
    if ed('dr'):
      pc=str(FsDr(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('xx'):
      pc=str(Fexp(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('str'):
      pc=str(Fstr(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('cut'):
      pc=str(Fstc(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1]),NtInput(ll,ap.split()[2])))
    if ed('ssc'):
      pc=str(Fssr(NtInput(ll,ap.split()[0]),NtInput(ll,ap.split()[1])))
    if ed('app'):
      pc+=ap
    if ed('fl'): #find from lines
      lf=''
      for i in range(len(ll)):
        if str(ap) in ll[i]:
          lf=lf+str(i+1)+' '
      print(lf)
    if ed('ed'): #set encoding
      enc=str(ui[2:])
  except Exception as xp:
    print(xp)
