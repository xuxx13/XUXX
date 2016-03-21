#include<iostream>
using namespace std;

// 工作集 
int main() {
  
  int a[9] = {1, 3, 0, 3, 0, 3, 1, 2, 4 };
  int b[5] = {0, 0, 0, 0, 0};
  int i, j;

  for (i = 0; i < 9; i++) 
  {
	    if (!b[a[i]]) 
		{
	    	cout<<"MISS "<<a[i]<<' ';
	    } 
		else 
		{
			cout<<"HIT "<<a[i]<<' ';
	    }
	    for (j = 0; j < 5; j++)
	        b[j] = 0;
	    for (j = (i >= 3 ? i -3 : 0); j <= i; j++)
	        b[a[j]] = 1;
	        
	    cout<<"集合  ";
	    for (j = 0; j < 5; j++) {
	       if (b[j])
	         cout<<j;
	    }
	    cout<<endl;
  }

  return 0;
}


