//Basic RLE

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>

int main( int argc, char* argv[] ){

	//check if incorrect number of arguments given
	if(argc != 5){
		printf("Error: Program expects <infile> <outfile> <compressionLength> <mode>\n");
		return -1;
	}

	char* infile = argv[1];
	char* outfile = argv[2];
	int compressionLength = atoi(argv[3]);
	int mode = atoi(argv[4]);

	//check if compressionLength is less than 1
	if(compressionLength < 1){
		printf("compression less than 1\n");
		return -1;
	}

	//check if mode is not 0 or 1
	if( mode == 0){;}

	else if(mode == 1){;}

	else{
		printf("Mode must be 0 or 1\n");
		return -1;
	}

	//open input file
	int bufSize = 1024;
	int fileFD = open(infile, O_RDONLY);
	if(fileFD < 1) {
		printf("No input file found\n");
		return -1;
	}

	int outFD = open( outfile, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    if( outFD == -1 ){
            perror("Could not open output file");
            exit(-1);
    }


	char buffer[bufSize];
	char pattern[compressionLength];
	char compare[compressionLength];
	int counter = 1;
  unsigned char Wcounter;

	read(fileFD, pattern, compressionLength);
	read(fileFD, compare, compressionLength);

	while(strlen(compare)==compressionLength){
        int result = strcmp(pattern, compare);
        if(result == 0){
            if(counter != 255){
                counter++;
            }
            else{
                Wcounter = counter;
                write(outFD, &Wcounter, 1); 
                write(outFD, pattern, compressionLength);
                counter = 1;
            }
        }

        else{
            Wcounter = counter;
            write(outFD, &Wcounter, 1); 
            write(outFD, pattern, compressionLength);
            memcpy(pattern, compare, compressionLength);
            counter = 1;
        }

        read(fileFD, compare, compressionLength);
	}
  Wcounter = counter;
	write(outFD, &Wcounter, 1); 
	write(outFD, compare, compressionLength);
	//do some write for any left out bytes and close files
}

