#include<stdio.h>
#include<string.h>

int main() {
unsigned char amy[64]={0xB7,0x8E,0x74,0x49,0xDD,0x89,0xF0,0xDE,0x91,0x3C,0x3F,0x11,0xB9,0xE5,0x5A,0xCF,0xD8,0x58,0xEE,0xB2,0xF9,0x89,0x21,0x1D,0x2C,0x1A,0x7D};
unsigned char alice[156];    
int v9[292];
unsigned int j,k;
int *v5;
int v11,v13,v14,v15,v16 =0;

unsigned char GUET2026[56];
strcpy(GUET2026,"GUET2026");
for(j=0;j<0x100;++j)
v9[j+16]=j;
v11=0;
for(j=0;j<0x100;++j) {

v16=(uint8_t)(v9[j+16]+v11);
v11=(uint8_t)*((GUET2026+j%8)+v16);
v13=(uint8_t)v9[j+16];
v9[j+16]=v9[v11+16];
v9[v11+16]=v13;
}
j=0;
v11=0;
for(k=0;k<27;++k)
{j=(uint8_t)(j+1);
 v11=(uint8_t)(v9[j=16]+v11);
 v14=(uint8_t)(v9[j+16]);
 v9[j+16]=v9[v11+16];
 v9[v11+16]=v14;
 v15=(uint8_t)v9[(uint8_t)v9[v11+16]+v9[j+16]+16)];
 *(alice+k)=v15^*(amy+k);
}
alice[27]='\0';
printf("%s\n",alice);
return 0;






}















