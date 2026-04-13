import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("SharkTankIndia.csv")
print(df.head())

# print(df.columns[1])
# print(df.iloc[:,1])
# print(len(df))

ashneerInvestment=0
anupamInvestment=0
namitaInvestment=0
amanInvestment=0
vineetaInvestment=0
peyushInvestment=0
gazalInvestment=0
i=0
while (i<len(df)):
      if(df.iloc[i,1]>=20 and df.iloc[i,1]<=30):
            if(df.iloc[i,9]==1):
                  ashneerInvestment+=df.iloc[i,6]
            elif(df.iloc[i,10]==1):
                  anupamInvestment+=df.iloc[i,6]
            elif(df.iloc[i,11]==1):
                  namitaInvestment+=df.iloc[i,6]
            elif(df.iloc[i,12]==1):
                  amanInvestment+=df.iloc[i,6]
            elif(df.iloc[i,13]==1):
                  vineetaInvestment+=df.iloc[i,6]
            elif(df.iloc[i,14]==1):
                  peyushInvestment+=df.iloc[i,6]
            elif(df.iloc[i,15]==1):
                  gazalInvestment+=df.iloc[i,6]
      i+=1


def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i-0.2, y[i], y[i])

xInvestorList=["ashneer","anupam","namita","aman","vineeta","peyush","gazal"]
yAmountList=[ashneerInvestment,anupamInvestment,namitaInvestment,amanInvestment,vineetaInvestment,peyushInvestment,gazalInvestment]
plt.figure(figsize=(10, 5))
plt.bar(xInvestorList,yAmountList,color="orange", width=0.5)
add_labels(xInvestorList,yAmountList)
plt.title("Total Amount Invested from Ep 20 to 30 by each Sharks")
plt.xlabel("Sharks")
plt.ylabel("Amounts in Ruppes")
plt.ticklabel_format(style='plain', axis='y')






top5CompanyName=[]
top_5 = sorted(df.iloc[:,6], reverse=True)[:5]
i=0
while (i<len(df)):
      if(df.iloc[i,6]==top_5[0]):
            top5CompanyName.insert(0,df.iloc[i,3])
            break
      i+=1
i=0
while (i<len(df)):
      if(df.iloc[i,6]==top_5[1]):
            top5CompanyName.insert(1,df.iloc[i,3])
            break
      i+=1
i=0
while (i<len(df)):
      if(df.iloc[i,6]==top_5[2]):
            top5CompanyName.insert(2,df.iloc[i,3])
            break
      i+=1
i=0
while (i<len(df)):
      if(df.iloc[i,6]==top_5[3]):
            top5CompanyName.insert(3,df.iloc[i,3])
            break
      i+=1
i=0
while (i<len(df)):
      if(df.iloc[i,6]==top_5[4] and df.iloc[i,0]!=13):
            top5CompanyName.insert(4,df.iloc[i,3])
            break
      i+=1

plt.figure(figsize=(10, 5))
plt.barh(top5CompanyName,top_5,height=0.5,color="lightgreen")
plt.title("Top 5 Company with Big Amount Deal")
plt.xlabel("Amount in Ruppes")
plt.ylabel("Company Name")
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.ticklabel_format(style='plain', axis='x')



i=0
food=0
bikes=0
fashionBeauty=0
educationTechnology=0
tourism=0
hygeine=0
healthcare=0
technology=0
socialCause=0
healthcareEquipment=0
socialMedia=0
construction=0
ecofriendly=0
fintech=0
electronics=0
pet=0
gifting=0
funeral=0
safety=0
agriculture=0
kitchen=0

while (i<len(df)):
      if(df.iloc[i,5]=="Food"):
            food+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Bikes"):
            bikes+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Fashion/Beauty"):
            fashionBeauty+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Education Technology"):
            educationTechnology+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Tourism"):
            tourism+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Hygeine"):
            hygeine+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Healthcare"):
            healthcare+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Technology"):
            technology+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Social Cause"):
            socialCause+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Healthcare Equipment"):
            healthcareEquipment+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Social Media"):
            socialMedia+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Construction"):
            construction+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Eco Friendly"):
            ecofriendly+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Fintech"):
            fintech+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Electronics"):
            electronics+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Pet"):
            pet+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Gifting"):
            gifting+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Funeral"):
            funeral+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Safety"):
            safety+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Agriculture"):
            agriculture+=df.iloc[i,6]
      elif(df.iloc[i,5]=="Kitchen"):
            kitchen+=df.iloc[i,6]
      i+=1

xPieValue=[food,bikes,fashionBeauty,educationTechnology,tourism,hygeine,healthcare,technology,socialCause,healthcareEquipment,socialMedia,construction,ecofriendly,fintech,electronics,pet,gifting,funeral,safety,agriculture,kitchen]
yPieLabel = ["Food", "Bikes", "FashionBeauty", "EducationTechnology", "Tourism", "Hygeine", "Healthcare", "Technology", "SocialCause", "HealthcareEquipment", "SocialMedia", "Construction", "Ecofriendly", "Fintech", "Electronics", "Pet", "Gifting", "Funeral", "Safety", "Agriculture", "Kitchen"]

plt.figure(figsize=(10,10))
plt.pie(xPieValue,labels=yPieLabel,autopct="%1.1f%%", wedgeprops=dict(width=0.5))
plt.title("Industry with the Most Investment in SharkTank S1")






ashneerEquity=0
anupamEquity=0
namitaEquity=0
amanEquity=0
vineetaEquity=0
peyushEquity=0
gazalEquity=0
i=0
while (i<len(df)):
      if(df.iloc[i,9]!=0):
            ashneerEquity+=df.iloc[i,8]
      elif(df.iloc[i,10]!=0):
            anupamEquity+=df.iloc[i,8]
      elif(df.iloc[i,11]!=0):
            namitaEquity+=df.iloc[i,8]
      elif(df.iloc[i,12]!=0):
            amanEquity+=df.iloc[i,8]
      elif(df.iloc[i,13]!=0):
            vineetaEquity+=df.iloc[i,8]
      elif(df.iloc[i,14]!=0):
            peyushEquity+=df.iloc[i,8]
      elif(df.iloc[i,15]!=0):
            gazalEquity+=df.iloc[i,8]
      i+=1

yTotalEquity=[ashneerEquity,anupamEquity,namitaEquity,round(amanEquity, 2),vineetaEquity,peyushEquity,gazalEquity]

plt.figure(figsize=(10, 5))
plt.bar(xInvestorList,yTotalEquity,color="yellow", width=0.5)
add_labels(xInvestorList,yAmountList)
plt.title("Most Equity of each Sharks")
plt.xlabel("Sharks")
plt.ylabel("Total Equity")
plt.ticklabel_format(style='plain', axis='y')
plt.show()

