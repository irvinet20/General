#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>

#define bufsize 100

struct arg_data{
    pthread_t thread_id;
    char salt[bufsize];
    char target[bufsize];
    char start;
    char end;
    int length;
};

int threadCount;
pthread_mutex_t lock;


void iterate( char* candidate, int place, int last, char start, char end, char* target, char* salt, struct crypt_data *data ){
        for( char i = start; i <= end; i++ ){
                candidate[place] = i;
                if ( place == last ){
					//printf("candidate: %s\n", candidate );
                                        char* result = crypt_r( candidate, salt, data);
                                        if(strcmp(result, target)==0){
                                                printf("password is: %s\n", candidate);
						exit(0);
                                        }
                }
                else{
                    iterate( candidate, place + 1, last, 'a', 'z', target, salt, data );
                }
        }
}

void* thread_entry( void* args ){
   
        struct crypt_data data;
        data.initialized = 0;

        struct arg_data *struct_ptr = args;

        char candidate[9]; //8 chars plus null terminator
        memset(candidate, '\0', 9); //Zero out string with null terms
        
        for(int j=0; j<struct_ptr->length;j++){
                        iterate( candidate, 
                                 0, 
                                 j, 
                                 struct_ptr->start, 
                                 struct_ptr->end, 
                                 struct_ptr->target, 
                                 struct_ptr->salt, 
                                 &data );
        }
}

int main( int argc, char* argv[] ){

        if( argc != 4 ){
                printf("Usage: <Threads> <Key Size> <Target> \n");
                return -1;
        }

        int threads = atoi(argv[1]);
        int keySize = atoi(argv[2]);
        char* target = argv[3];
        char salt[3];
        int x = 26/threads;
        int s;

        for(int s=0; s<2; s++){
                salt[s] = target[s];
        }
        salt[2] = '\0';
        
        struct arg_data thread[threads];
        
	char start = 'a';
	int remainder = 26 % threads;
        for(int i=0; i<threads; i++){
/*                thread[i].start = 'a'+i*x;
                thread[i].end = 'a'+x+i*2*x; */
		int range = x;
		if (i < remainder){
			range++;
		}
		thread[i].start = start;
		thread[i].end = start+range-1;
		start = start + range;
		printf("Thread %d: %c to %c\n", i, thread[i].start, thread[i].end );
        }
        for(int k=0; k < threads; k++){
                thread[k].length = keySize;
                snprintf(thread[k].target, bufsize, "%s", target);
                snprintf(thread[k].salt, bufsize, "%s", salt);
                
                int ret = pthread_create(&thread[k].thread_id, NULL, thread_entry, &thread[k]);
                if(ret != 0){
                        printf("Error creating thread:");
                        return -1;
                }
        }
        
        for(int j=0; j<threads; j++){
                pthread_join(thread[j].thread_id, NULL);
        }

        return 0;
}
