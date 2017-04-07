#encoding:utf-8
#
#author:wuhao
#
#数独算法，先来一个简单的4x4

import time

#判断数独是否有问题
def is_ok(a,i,j):
    print(a)
    print("-----%s,%s"%(i,j))
    if(a[i][j]!=0):
        for k in range(4):
            if(a[k][j]!=0 and k!=i):
                if (a[k][j]==a[i][j]): return False
            if(a[i][k]!=0 and k!=j):
                if(a[i][k]==a[i][j]):return False
        for k in range(2):
            if a[int(i/2)*2+k][int(j/2)*2]!=0:
                if(a[i][j]==a[int(i/2)*2+k][int(j/2)*2] and int(i/2)*2+k!=i and int(j/2)*2!=j):return False
            if a[int(i/2)*2+k][int(j/2)*2+1]!=0:
                if(a[i][j]==a[int(i/2)*2+k][int(j/2)*2+1] and int(i/2)*2+k!=i and int(j/2)*2+1!=j):return False
    if i!=3 or j!=3:
        is_ok(a,i+int((j+1)/4),(j+1)%4)
    return True

#判断是否需要填充数据
def check(a,i,j):
    if a[i][j]==0: return True
    return False

#进行数据的填充
def FillData(a,i,j):
    if check(a,i,j):            #如果需要数据填充
        list_a=[1,2,3,4,5,6,7,8,9]
        for k in range(9):
            if a[i][k]!=0:      #纵向判断,如果已经溢出了，pass掉
                try:
                    list_a.remove(a[i][k])
                except:pass

            if a[k][j]!=0:      #横向判断,如果已经移除过了，pass掉
                try:
                    list_a.remove(a[k][j])
                except:pass

        for k in range(3):
            if a[int(i/3)*3+k][int(j/3)*3]!=0:
                try:
                    list_a.remove(a[int(i/3)*3+k][int(j/3)*3])
                except:pass
            if a[int(i/3)*3+k][int(j/3)*3+1]!=0:
                try:
                    list_a.remove(a[int(i/3)*3+k][int(j/3)*3+1])
                except:pass
            if a[int(i/3)*3+k][int(j/3)*3+2]!=0:
                try:
                    list_a.remove(a[int(i/3)*3+k][int(j/3)*3+2])
                except:pass
        return list_a
    return a[i][j]

Game_over=False


def listData(a,posx,posy,f):
    global Game_over
    if Game_over==True:return a
    if posx != 8 or posy != 8:
        if check(a,posx,posy):
            data=FillData(a,posx,posy)
            length=len(FillData(a,posx,posy))
            for k in range(length):
                print("(%s,%s),Gameover=%s"%(posx,posy,Game_over))
                if Game_over==False:
                    a[posx][posy]=data[k]
                    f.write(str(a))
                    f.write("\r\n")
                    listData(a,posx+(posy+1)//9,(posy+1)%9,f)
                else:return a
            if Game_over==False:
                a[posx][posy] = 0
        else:
            listData(a,posx+(posy+1)//9,(posy+1)%9,f)
    else:
        Game_over=True
        a[posx][posy]=FillData(a,posx,posy)[0]
        return a

if __name__=="__main__":
    list_a=\
    [
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]
    ]
    f = open("log.txt","w")
    if list_a==listData(list_a,0,0,f):
        print("此数独无解")
    else:print(list_a)
    f.close()
