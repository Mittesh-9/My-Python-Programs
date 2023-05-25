
# logic yaha aise hoga ki first of all (a) aur (b) ki length same hai ya nahi wo check karna hai
# (a) ko (a+a)karna hoga aur fir wo hojaega (abcdeabcde) aur fir (b) ko (a+a) me dhoondna hai.

a= "abcde"
b= "cdeab"

def rotate_string(a, b):
    return(len(a) == len(b) and b in (a + a))

# Java language me solution:
# return(a.length() == b.length && (a + a).contains(b))