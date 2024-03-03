#include<stdio.h>


int func(int first, int second) {
	first = first + second;
	return first;
}

int main() {
	int sum = func(1, 4);
}
