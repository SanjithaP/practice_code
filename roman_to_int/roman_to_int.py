class Solution {
public:
    int value(char  r){
    if (r == 'I')   
      return 1;   
    if (r == 'V')   
      return 5;   
    if (r == 'X')   
      return 10;   
    if (r == 'L')   
      return 50;   
    if (r == 'C')   
      return 100;   
    if (r == 'D')   
      return 500;   
    if (r == 'M')   
      return 1000;   
    return -1;
    }
    
    int romanToInt(string s) {
        int total=0;
        for(int i=0;i<s.size();i++){
            int s1=value(s[i]);
            int s2=value(s[i+1]);
            int s3=0;
            if(s1<s2){
              s3=s2-s1;
              i++;
            }
            else{
             s3=s1;
            }
            total+=s3;

        }
        return total;
        
    }
};