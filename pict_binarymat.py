from PIL import Image
import numpy as np

# PILでsample.jpgを開いてグレースケール画像に変換し、NumPy配列に変換
im = np.array(Image.open('sample.jpg').convert('L'))

# NumPy配列のshapeと、要素のデータ型を表示
print(im.shape[0], im.shape[1])

# グレースケール化した画像のNumPy配列に変換したものを表示
print(im)

# 上記NumPy配列をテキストで保存
#   np.savetxt('im_ndarray.txt', im)

bin_mat=np.zeros((im.shape[0], im.shape[1]))

centerRow=int(im.shape[0]/2)    #行
centerCol=int(im.shape[1]/2)    #列

bin_mat[centerRow,centerCol]=1

#左-上
for r in range(centerRow,0,-1):
    for c in range(centerCol,0,-1):
        #bin_matの初期値0なので1の時のみ記述
        if im[r,c]<255:
            #上下左右確認
            if bin_mat[r-1,c]==1 or bin_mat[r+1,c]==1 or bin_mat[r,c-1]==1 or bin_mat[r,c+1]==1:
                bin_mat[r,c]=1
#右-上
for r in range(centerRow,im.shape[0],1):
    for c in range(centerCol,0,-1):
        if im[r,c]<255:
            if bin_mat[r-1,c]==1 or bin_mat[r+1,c]==1 or bin_mat[r,c-1]==1 or bin_mat[r,c+1]==1:
                bin_mat[r,c]=1
#右-下
for r in range(centerRow,im.shape[0],1):
    for c in range(centerCol,im.shape[1],1):
        if im[r,c]<255:
            if bin_mat[r-1,c]==1 or bin_mat[r+1,c]==1 or bin_mat[r,c-1]==1 or bin_mat[r,c+1]==1:
                bin_mat[r,c]=1
#左-下
for r in range(centerRow,0,-1):
    for c in range(centerCol,im.shape[1],1):
        if im[r,c]<255:
            if bin_mat[r-1,c]==1 or bin_mat[r+1,c]==1 or bin_mat[r,c-1]==1 or bin_mat[r,c+1]==1:
                bin_mat[r,c]=1
#binary edge search
for r in range(0,bin_mat.shape[0],1):
    for c in range(0,bin_mat.shape[1],1):
        if bin_mat[r,c]==1:
            b_top=r/1.33
            break
    else:
        continue
    break
for r in range(bin_mat.shape[1],0,-1):
    for c in range(0,bin_mat.shape[1],1):
        if bin_mat[r,c]==1:
            b_bottom=r/1.33
            break
    else:
        continue
    break
for c in range(0,bin_mat.shape[1],1):
    for r in range(0,bin_mat.shape[1],1):
        if bin_mat[r,c]==1:
            b_left=c/1.33
            break
    else:
        continue
    break
for c in range(bin_mat.shape[1],0,-1):
    for r in range(0,bin_mat.shape[1],1):
        if bin_mat[r,c]==1:
            b_right=c/1.33
            break
    else:
        continue
    break

print(b_top,b_bottom,b_left,b_right)
