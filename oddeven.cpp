#include <iostream> 

using namespace std; 

void check(int n)
{
    if(n%2==0)
    
    {
        
        cout<<n<<" is a Even no.";
        
    }
    else
    {
        
        cout<<n<<" is a Odd no.";
        
    }
    
}

int main() 

{ 

	int num; 	

	cout << "Enter an integer: "; 

	cin >> num; 
    
	check(num);

	return 0; 

} 
