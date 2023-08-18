class Solution{
public:

	bool isPalindrome(string st){
        int n=st.size();
        for(int i=0;i<n/2;i++){
            if(st[i]!=st[n-i-1]){
                return false;
            }
        }
        return true;
    }
    
    int toNum(char c){
        // will just return the int of the char provided
        return int(c)-48;
    }
    
    vector<int> genVect(string st){
        // generate a vector from a string
        vector<int> vect;
        for(int i=0;i<st.size();i++){
            vect.push_back(toNum(st[i]));
        }
        return vect;
    }
    
	vector<int> generateNextPalindrome(int num[], int n) {
	    // code here
	    vector<int> ans={1,2,3};
	    
	    // converting the arr to a string to ease the working
	    string number="";
	    for(int i=0;i<n;i++){
	        number+=to_string(num[i]);
	       // cout<<sizeof(char(num[i]))<<" and "<<sizeof(to_string(num[i]))<<endl;
	       
	       // cout<<num[i]<<" and "<<sizeof(num[i])<<": "<<endl;
	       // cout<<sizeof(to_string(num[i]))<<endl;
	    }
	   // cout<<number<<endl;
	    
	   // string answerStr="";
	   // cout<<isPalindrome(number)<<endl;
	    // now will handle the cases for the string number
        if(isPalindrome(number)){
    	    int startIndex,carry=-1;
    	    
    	    if(n%2==0){
    	        // for even len palindrome
    	        // starting traversal from the middle char in the left direction
    	        startIndex=(n/2)-1;
            }
    	    else{
    	        // for odd len palindrom
    	        
    	        /* SAME THING LIKE EVEN, JUST STARTINDEX DIFFERENT */
    	        
    	        // starting traversal from the middle char in the left direction
    	        startIndex=n/2;
    	    }
    	    
    	    for(int i=startIndex;i>-1;i--){
        	        
        	        // if there's no carry and this is not the first digit then, return
                    if(carry!=1 and i!=startIndex){
                        // cout<<"Final answer was "<<number<<endl;
                        return genVect(number);        
                    }
                    
                    int temp=toNum(number[i])+1;
                    // cout<<"curr index: "<<i<<" and temp: "<<temp<<endl;
                    // if >9 then will have to give carry to the nums at the left
                    if(temp>9){
                        if(i==0){
                            // in this case will have to add another digit to the left of the number
                            // cout<<"New digit added to the left...\n";
                            // cout<<"Are we here??\n";
                            number="1"+number;
                            // cout<<"New number: "<<number<<endl;
                            // cout<<"changing "<<i<<" and "<<n-i-1<<" to 0\n";
                            
                            number[i+1]='0';
                            number[n]='1';
                            
                            // cout<<"number update: 1's added!\n";
                            goto done;
                        }
                            // cout<<"i was "<<i<<endl;
                            // cout<<"changed the digit to 0, and moving to left to give the carry now\n";
                            number[i]='0';
                            number[n-i-1]='0';
                            // answerStr+=to_string(0);
                            // next time will again add 1 to the left digit
                            carry=1;
                    }
                    else{
                        // done just update this char, that's it
                        number[i]=char(48+temp);
                        number[n-i-1]=char(48+temp);
                        // cout<<"char updated cause it was <=9, to "<<temp<<endl;
                        // cout<<number<<endl;
                        // so that next time there won't be any carry and the func will return
                        carry=0;
                    }
                    
        	       // if(i==0){
        	       //    // cout<<"Final answer: "<<number<<endl;
        	       // }
        	    }
    	    
        }
        else{
            // when the input is not already a palindrome
            int startIndex;
            if(n%2==0){
                startIndex=(n/2)-1;
            }
            else{
                startIndex=n/2;
            }
            
            // whether any num has been increased in between or not
            bool numIncreasedInBw=false;
            for(int i=startIndex;i>-1;i--){
                // note here I don't have to handle the case of 9 increasing to 10, because 
                // digits are from 0-9 and if 9 is there then it can't be bigger than any 
                // other digit
                // num1: left number, num2: right number
                int num1=toNum(number[i]),num2=toNum(number[n-i-1]);
                if(num1>num2){
                    // make num2 equal to num1, that's it
                    number[n-i-1]=char(48+num1);
                    // cause we increased the right elem here
                    numIncreasedInBw=true;
                }
                else if(num1==num2){
                    // nothing
                }
                else if(num1<num2){
                    // when we cannot copy the left num directly to the right, cause then the number would not be sure to be greater 
                    
                    // num1+=1;
                    // number[i]=char(48+num1);
                    // number[n-i-1]=char(48+num2);
                    
                    int carry=0;
                    if(numIncreasedInBw==false){
                        // cout<<"Am I here?\n";
                        // now will have to increase from the middle
                        for(int j=startIndex;j>-1;j--){
                            
                            // increase the elem in the middle
                            int numTemp1=toNum(number[j]),numTemp2=toNum(number[n-j-1]);
                            if(numTemp1==9){
                                // will have to handle carry of this elem
                                number[j]='0';
                                number[n-j-1]='0';
                                carry=1;
                                numIncreasedInBw=true;
                            }
                            else{
                                // no problem of carry here
                                numTemp1+=1;
                                number[j]=char(48+numTemp1);
                                number[n-j-1]=char(48+numTemp1);
                                carry=0;
                                numIncreasedInBw=true;
                                break;
                            }
                            
                            
                        }
                        
                    }
                    // here i know that atleast 1 num would be increased in middle, 
                    // now can copy num1 to num2, that's it
                    number[n-i-1]=number[i];
                    
                }
            }
            
            
            
        }
	    
	    done:
	    return genVect(number);
	}



};