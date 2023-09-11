#include <stdio.h>
#include <stdlib.h>
int binary_search(int a[], int size, int key)
{
    int low = 1, high = size, mid;
    
    while (low <= high)
    {
        mid = (low+high)/2;
if (a[mid]== key) return mid;
else if (a[mid] < key) low = mid + 1 ; 
else high = mid - 1;

    }
    return -1;
}
 int main(void)
{
    int a[] = {5,8,10,44,67,87,89,90,101};
    int size = sizeof(a)/sizeof(a[0]);
    int key=10;
    printf("enter key to search\n");
    scanf("%d",&key);
    int index = binary_search(a,size,key);
    printf("position of the key is %d\n",index);
    return 0;
}