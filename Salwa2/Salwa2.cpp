#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;



double pow_bin(double a, int b){
    double wynik = 1;
    while (b)
    {
        if (b & 1)
            wynik *= a;
        b >>= 1;
        a *= a;
    }

    return wynik;
}

double pow_i( double liczba, unsigned long long int potega){
    double wynik=liczba;
    while(potega>1) {
        wynik *= wynik;
        potega /= 2;
    }
    return wynik;

}

int main()
{
	double elapsed_secs ;
    double elapsed_secs2;
//==================a=2, b= 20*j============================
	int a=2;
    int b;
    for (int j=0 ; j<5 ; j++){
    	b=20*j;
    	//=================
	    clock_t begin = clock();
	    for(int i=0;i<10000000; i++){
	    	pow(a,b);
	    }
	    clock_t end = clock();
	    //=================
	    clock_t begin2 = clock();
	    for(int i=0;i<10000000; i++){
	    	pow_i(a,b);
	    }
	    clock_t end2 = clock();
	    //=================
	    clock_t begin3 = clock();
	    for(int i=0;i<10000000; i++){
	    	pow_bin(a,b);
	    }
	    clock_t end3 = clock();
	    //=================
	    
		double elapsed_secs = double(end - begin)/ CLOCKS_PER_SEC;
	    double elapsed_secs2 = double(end2 - begin2)/ CLOCKS_PER_SEC;
	    double elapsed_secs3 = double(end3 - begin3)/ CLOCKS_PER_SEC;
	    cout<< "a=2, b="<<b<< ", n=10000000"<<endl;
	    cout<< "wbudowana czas: " << elapsed_secs << endl;
	    cout<< "moja binarna czas: " << elapsed_secs2 << endl;
	    cout<< "moja iteracyjna czas: " << elapsed_secs3 << endl <<endl;
	    
		
	}
}
