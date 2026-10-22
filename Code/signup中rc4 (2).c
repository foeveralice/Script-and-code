#include<stdio.h>
#include<string.h>
int main() {
unsigned char elma[64];    
unsigned char alice[64]={0xB7,0x8E,0x74,0x49,0xDD,0x89,0xF0,0xDE,0x91,0x3C,0x3F,0x11,0xB9,0xE5,0x5A,0xCF,0xD8,0x58,0xEE,0xB2,0xF9,0x89,0x21,0x1D,0x2C,0x1A,0x7D};  
char GUET2026[56];
unsigned int i,j,k=0;
unsigned int v11=0;
unsigned int v13,v14,v15,v16=0;
unsigned char v9[256];
strcpy(GUET2026,"GUET2026");
for(i=0;i<256;++i) {
v9[i]=i;
}
for(j=0;j<256;++j) {
v16=v11;
v16=(v9[j]+v16)%256;
v11=(*(GUET2026+j%8)%256+v16)%256;
v13=v9[j];
v9[j]=v9[v11];
v9[v11]=v13;
}
j=0;
v11=0;
for(k=0;k<27;++k) {
j=(j+1)%256;
v11=(v9[j]+v11)%256;
v14=v9[j];
v9[j]=v9[v11];
v9[v11]=v14;
v15=(v9[(v9[v11]+v9[j])%256])%256;
*(elma+k)=v15^*(alice+k);
}
elma[27]='\0';
printf("%s\n",elma);
return 0;










}