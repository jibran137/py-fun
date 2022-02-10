def createList(r1, r2):
    li=[]
    while(r1!=r2):
        li.append(r1)
        r1+=.25
        if r1==24:
            r1=0
    return(li)


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def uInputs():
    s = input("When did the chiller start: ")
    s = float(s)
    e = input("When did the chiller stop: ")
    e = float(e)

    return(s,e)

## Add times in quarters and in the 24hour format i.e, 3:15pm would be 15.25

s = 3                    #When the chiller starts
e = 15.75                #When the chiller stops

## Comment the line below if you dont want to take an input
s,e = uInputs()

ourtime=createList(s,e)

## Predefined lists for the time periods
## Generating the lists as they mighit be very long

peak=createList(18,23)
offline=createList(3,7)
oth1=createList(7,18)
oth=oth1+createList(23,3)

## Use intersections to find the number of quarter hours the machine was on during a period

peaktime=intersection(ourtime,peak)
offtime=intersection(ourtime,offline)
othtime=intersection(ourtime,oth)

## Printing the results

print("Peak hours: ",len(peaktime)/4)
print("Offline hours: ",len(offtime)/4)
print("Other hours: ", len(othtime)/4)