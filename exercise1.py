def strstr(hay,ndl):
    m=len(hay)
    n=len(ndl)
    for i in range(m-n+1):
        j=0
        for j in range(n):
            if hay[i]!=ndl[j]:
                i+=1
            else:
                if hay[i+j]==ndl[j]:
                    j+=1

            if j==n:
                return i
            else :
                return -1


hay="aaaaa"
ndl='bba'
check=strstr(hay,ndl)
print(check)
