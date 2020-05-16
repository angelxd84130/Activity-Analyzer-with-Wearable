import pandas as pd
df = pd.read_csv("train_result_3.csv")
#print(df)
string = ["timest", "coarse", "fine",
          "b_accel_x", "b_accel_y", "b_accel_z", "b_gyros_x", "b_gyros_y", "b_gyros_z", "b_magne_x", "b_magne_y", "b_magne_z",
          "h_accel_x", "h_accel_y", "h_accel_z", "h_gyros_x", "h_gyros_y", "h_gyros_z", "h_magne_x", "h_magne_y", "h_magne_z",
          "p_accel_x", "p_accel_y", "p_accel_z", "p_gyros_x", "p_gyros_y", "p_gyros_z", "p_magne_x", "p_magne_y", "p_magne_z",
          "t_accel_x", "t_accel_y", "t_accel_z", "t_gyros_x", "t_gyros_y", "t_gyros_z", "t_magne_x", "t_magne_y", "t_magne_z"]
#Still = pd.DataFrame([], columns=string)
#Walking = pd.DataFrame([], columns=string)
Run = pd.DataFrame([], columns=string)
#Bike = pd.DataFrame([], columns=string)
#Car = pd.DataFrame([], columns=string)
#Bus = pd.DataFrame([], columns=string)
#Train = pd.DataFrame([], columns=string)
#Subway = pd.DataFrame([], columns=string)

for i in range(len(df)):
    '''
    if df['coarse'][i] == 1:
        Still = Still.append(df.loc[i], ignore_index=True)
    elif df['coarse'][i] == 2:
        Walking = Walking.append(df.loc[i], ignore_index=True)
    '''
    if df['coarse'][i] == 3:
        Run = Run.append(df.loc[i], ignore_index=True)
    '''
    elif df['coarse'][i] == 4:
        Bike = Bike.append(df.loc[i], ignore_index=True)
    
    elif df['coarse'][i] == 5:
        Car = Car.append(df.loc[i], ignore_index=True)
    
    elif df['coarse'][i] == 6:
        Bus = Bus.append(df.loc[i], ignore_index=True)
    
    if df['coarse'][i] == 7:
        Train = Train.append(df.loc[i], ignore_index=True)
    elif df['coarse'][i] == 8:
        Subway = Subway.append(df.loc[i], ignore_index=True)
    '''

#print(Still)
#Still.to_csv("Still.csv")
#Walking.to_csv("Walking.csv")
Run.to_csv("Run.csv")
#Bike.to_csv("Bike.csv")
#Car.to_csv("Car.csv")
#Bus.to_csv("Bus.csv")
#Train.to_csv("Train.csv")
#Subway.to_csv("Subway.csv")