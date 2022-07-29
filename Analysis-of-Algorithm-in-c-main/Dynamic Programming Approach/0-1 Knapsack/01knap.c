#include<stdio.h>
#include<conio.h>
#define MAX 30
int maximum(int a, int b);
void zoknapsack(int n, int capacity);
int profits[MAX], weights[MAX];
int includeditems[MAX];
int main()
{
    int i,j,n,capacity;
    printf("Enter the number of items : ");
    scanf("%d",&n);
    printf("Enter the profits and weights of each item\n");
    for (i=0;i<n;++i)
    {
        printf("Item %d : ",i+1);
        scanf("%d %d",&profits[i],&weights[i]);
    }
    printf("Enter the capacity of knapsack : ");
    scanf("%d",&capacity);
    zoknapsack(n,capacity);
    return 0;
}

void zoknapsack(int n, int capacity)
{
    int t[n+1][capacity+1],maxprofit=0;
    int i,j,k=0;
    for (i=0;i<=n;++i)
    {
        for (j=0;j<=capacity;++j)
        {
            if (i==0 || j==0)
            {
                t[i][j]=0;
            }
            else if (j>=weights[i-1])
            {
                t[i][j]=maximum(t[i-1][j], t[i-1][j-weights[i-1]] + profits[i-1]);
            }
            else
            {
                t[i][j]=t[i-1][j];
            }
            printf("%d ",t[i][j]);
        }
        printf("\n");
    }
    for(i=1;i<=n;i++)
        includeditems[i]=0;
    int c=0;
    maxprofit=t[n][capacity];
    printf("Maximum Profit : %d",maxprofit);
    printf("\n");
    for (i=n;i>0 && maxprofit>=0;--i)
    {
        if (maxprofit == t[i-1][capacity])
        {
            continue;
        }
        else
        {
            //printf("%d ",weights[i-1]);
            maxprofit-=profits[i-1];
            capacity-=weights[i-1];
            includeditems[i]=1;
            printf("Item %d ",i);
        }
    }
    printf(" are the items included in the knapsack");
    printf("\n0/1 Array: [");
    for(i=1;i<=n;i++)
        printf("%d ",includeditems[i]);
    printf("]");
}

int maximum(int a, int b)
{
    return (a>b?a:b);
}
