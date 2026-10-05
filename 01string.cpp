#include<iostream>
using namespace std;

int main(){

int n;
cin>>n;
int arr[n];

for(int i=0;i<n;i++){

cin>>arr[i];

}
int t;
cout<<"print target: ";
cin>>t;

for(int i=0;i<n;i++){
    if(arr[i]+arr[i+1]==t){
        cout<<arr[i]<<","<<arr[i+1];
    }
}

return 0;

}