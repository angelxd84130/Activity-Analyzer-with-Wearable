import pandas as pd
import collections

string = "SHLDataset_preview_v1/User1/260617/"
labelStr = ["timest", "coarse", "fine", "road", "traffic", "tunnels", "social", "food"]
label = pd.read_csv(string+"Label.txt", sep=' ', header=None, names=labelStr)
del label['road']
del label['traffic']
del label['tunnels']
del label['social']
del label['food']
motionStr = ["timest", "b_accel_x", "b_accel_y", "b_accel_z", "b_gyros_x", "b_gyros_y", "b_gyros_z",
             "b_magne_x", "b_magne_y", "b_magne_z", "orien_w", "orien_x", "orien_y", "orien_z",
             "gravi_x", "gravi_y", "gravi_z", "i_accel_x", "i_accel_y", "i_accel_z",
             "press", "altit", "tempe"]
bag = pd.read_csv(string+"Bag_Motion.txt", sep=' ', header=None, names=motionStr)
del bag['orien_w']
del bag['orien_x']
del bag['orien_y']
del bag['orien_z']
del bag['gravi_x']
del bag['gravi_y']
del bag['gravi_z']
del bag['i_accel_x']
del bag['i_accel_y']
del bag['i_accel_z']
del bag['tempe']
del bag['altit']
del bag['press']
motionStr = ["timest", "h_accel_x", "h_accel_y", "h_accel_z", "h_gyros_x", "h_gyros_y", "h_gyros_z",
             "h_magne_x", "h_magne_y", "h_magne_z", "orien_w", "orien_x", "orien_y", "orien_z",
             "gravi_x", "gravi_y", "gravi_z", "i_accel_x", "i_accel_y", "i_accel_z",
             "press", "altit", "tempe"]
hand = pd.read_csv(string+"Hand_Motion.txt", sep=' ', header=None, names=motionStr)
del hand['orien_w']
del hand['orien_x']
del hand['orien_y']
del hand['orien_z']
del hand['gravi_x']
del hand['gravi_y']
del hand['gravi_z']
del hand['i_accel_x']
del hand['i_accel_y']
del hand['i_accel_z']
del hand['tempe']
del hand['altit']
del hand['press']
motionStr = ["timest", "p_accel_x", "p_accel_y", "p_accel_z", "p_gyros_x", "p_gyros_y", "p_gyros_z",
             "p_magne_x", "p_magne_y", "p_magne_z", "orien_w", "orien_x", "orien_y", "orien_z",
             "gravi_x", "gravi_y", "gravi_z", "i_accel_x", "i_accel_y", "i_accel_z",
             "press", "altit", "tempe"]
hips = pd.read_csv(string+"Hips_Motion.txt", sep=' ', header=None, names=motionStr)
del hips['orien_w']
del hips['orien_x']
del hips['orien_y']
del hips['orien_z']
del hips['gravi_x']
del hips['gravi_y']
del hips['gravi_z']
del hips['i_accel_x']
del hips['i_accel_y']
del hips['i_accel_z']
del hips['tempe']
del hips['altit']
del hips['press']
motionStr = ["timest", "t_accel_x", "t_accel_y", "t_accel_z", "t_gyros_x", "t_gyros_y", "t_gyros_z",
             "t_magne_x", "t_magne_y", "t_magne_z", "orien_w", "orien_x", "orien_y", "orien_z",
             "gravi_x", "gravi_y", "gravi_z", "i_accel_x", "i_accel_y", "i_accel_z",
             "press", "altit", "tempe"]
torso = pd.read_csv(string+"Torso_Motion.txt", sep=' ', header=None, names=motionStr)
del torso['orien_w']
del torso['orien_x']
del torso['orien_y']
del torso['orien_z']
del torso['gravi_x']
del torso['gravi_y']
del torso['gravi_z']
del torso['i_accel_x']
del torso['i_accel_y']
del torso['i_accel_z']
del torso['tempe']
del torso['altit']
del torso['press']
'''
dic = collections.Counter()
for i in range(8):
    dic[i] = 0
for i in range(len(label)):
      dic[label['coarse'][i]]+=1
      #print(label['coarse'][i])     
print(dic)
'''
result = pd.merge(label, bag, on="timest")
print("len", len(result))
result = pd.merge(result, hand, on="timest")
print("len", len(result))
result = pd.merge(result, hips, on="timest")
print("len", len(result))
result = pd.merge(result, torso, on="timest")
print("len", len(result))
print(result)
result.to_csv("train_result.csv")


# 270617/ Counter({0: 1216891, 8: 911943, 7: 897124, 1: 193588, 4: 123014, 2: 53941, 3: 0, 5: 0, 6: 0})
# 260617/ Counter({0: 1814595, 6: 913184, 1: 424521, 4: 373607, 2: 361645, 3: 10549, 5: 0, 7: 0})
# 220617/ Counter({0: 2819190, 5: 993161, 2: 388469, 1: 250542, 3: 122923, 6: 70516, 4: 0, 7: 0})
#print(len(label))
#print(bag.head(5))
#print(hand.head(5))
#print(hips.head(5))
#print(torso.head(5))
