#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <sys/types.h>

typedef struct node {
	struct node *next;
	int size;
	bool used;
	void* ptr;
}
Node;
Node* head = NULL;

//Borrowed from GFG @ https://www.geeksforgeeks.org/round-to-next-greater-multip
//le-of-8/

int rround(void* x){
	return (((uintptr_t)x+7)&(-8));
}

void *malloc(size_t size){

	Node* curr = head;
	Node* prev = head;	
	int page = sysconf(_SC_PAGESIZE);

	while(curr != NULL){
		if(curr->used==false){
			//If allocation is large enough but not large enough to split
			if(curr->size >= size && curr->size <= (size + sizeof(Node) + 1) ){
				curr->used = true;
				return curr->ptr;
			}
			else if(curr->size > size){
				Node* blank = ((void*)curr) + size + sizeof(Node);
				blank->next = curr->next;
				blank->used = false;
				blank->size = curr->size-size-sizeof(Node);
				blank->ptr = blank + 1;
				curr->size=size;
				curr->used = true;
				curr->next = blank;
				return curr->ptr;
			}
		}
	prev = curr;
	curr = curr->next;
	}

	//NOTE: sbrk() only multiples of page size
	int bytes_needed = size + sizeof(Node);
	int pages_needed = bytes_needed / page + 1;
	int total_request = pages_needed * page;
	void* ptr = sbrk(total_request);
	Node* blank = ptr;
	blank->size=size;
	blank->used = true;
	blank->ptr = ptr+sizeof(Node);

	//Do we have enough space to split?
	if( total_request > bytes_needed + sizeof(Node) + 1){
		Node* next = ((void*) blank) + size + sizeof(Node);
		next->size = total_request - size - sizeof(Node)*2;
		next->used = false;
		next->ptr = next + 1;
		next->next = NULL;
		blank->next = next;
	} else {
		//No extra node after this one
		blank->next = NULL;
	}
	if( head == NULL ){
		head = blank;
	} else {
		prev->next = blank;
	}
	return blank->ptr;
}

void free(void* ptr){
	Node* prev = head;
	Node* curr = head;
	while(curr!=NULL){
		if(curr->ptr == ptr){
			curr->used = false;
			if(prev->used == false && prev != head){
				prev->size = prev->size+curr->size+sizeof(Node);
				prev->next = curr->next;
				curr->next = NULL;
				curr = prev;
			}
			if(curr->next != NULL && curr->next->used==false){
				curr->size = curr->size+curr->next->size+sizeof(Node);
				curr->next = curr->next->next;
			}
			return;
		}
		prev = curr;
		curr = curr->next;
	}
}


void* calloc(size_t elems, size_t size){
	int tot = elems*size;
	void* ptr = malloc(tot);
	return memset(ptr,0,tot);
}

void* realloc(void* ptr, size_t size){
	Node* curr = head;
	while(curr->ptr != ptr){
		curr = curr->next;
	}
	void* new = malloc(size);
	if(curr->size>=size){
		return memcpy(new,curr->ptr,size);
	}
	else{
		return memcpy(new,curr->ptr,curr->size);
	}
}

