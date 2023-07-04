class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        five_changes=0
        ten_changes=0
        # Not maintaining the count of twnety_changes bcz that would be of no use as I won't require it
        for bil in bills:
            if(bil==5):
                # Just increase the five_changes count and the customer is good to go
                five_changes+=1
            elif(bil==10):
                # For this case I gotta return the customer with a 5 change, so five_changes will decr
                if(five_changes==0):
                    # If I don't have any five change then just return False, no other choice
                    return False
                else:
                    # Else just, a five change got used up for this customer
                    five_changes-=1
                    # I got a 10 dollar note from the customer, so upating that 
                    ten_changes+=1
            else:
                # Means the bill is 20, 20 dollar note is of no use to me, that's mean to pay me with a 20 dollar you customer...
                # Can return the customer either, three 5 dollars OR one 10 and a 5 dollar
                # Note: I will prefer to use a 10 dollar if I have that, else then go for three 5 dollar notes
                if(ten_changes!=0):
                    # Then utilise the ten change
                    if(five_changes!=0):
                        # If I get here means I can give the customer a 10 and a 5 dollar note
                        ten_changes-=1
                        five_changes-=1
                    else:
                        # Means we cannot use a ten change, and also bcz I don't have a five change, then cannot give 3 5 dollars too, so just return False
                        return False
                else:
                    # Means I don't have a 10 change, but maybe I have three 5 dollars, if not, then not possible to return the change to the customer
                    if(five_changes<3):
                        return False
                    else:
                        # when I have three or more 5 dollar notes, so just decrease them by 3
                        five_changes-=3

        # If everything was alright till here then just return True
        return True