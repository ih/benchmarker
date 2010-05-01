#include <stdio.h>

int main(){
  double j=0;
  double i=0;
  for(i=0; i<1000000;i++){
    j=j+i;
  }
  printf("%f\n", j);
  return j;
}

void print_sum(int arg1, int arg2){
  int sum = arg1+arg2;
  printf("The sum is %d\n", sum);
  return;
}
