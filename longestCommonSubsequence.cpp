class Solution
{
   public:
   int dp[1001][1001] ;
   Solution()
   {
    //   for( int i = 0 ; i < 1001 ; i++ )
    //       for( int j = 0 ; j < 1001 ; j++ )
    //           dp[i][j] = -1 ;
    memset(dp,-1,sizeof(dp));
   }
   
   int lcs(int x , int y , string& s1 , string& s2 )
   { 
       if( x == 0 or y == 0 )
           return dp[x][y] = 0 ;
           
       if( dp[x][y] != -1 )
           return dp[x][y] ;
           
       if( s1[x-1] == s2[y-1] )
           return dp[x][y] = lcs( x - 1 , y - 1 , s1 , s2 ) + 1 ;
       else
           return dp[x][y] = max( lcs( x , y - 1 , s1 ,s2 ) , lcs( x - 1 , y , s1 , s2 ) ) ;
   }
};